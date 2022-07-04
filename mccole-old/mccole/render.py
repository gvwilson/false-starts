"""Convert token streams to HTML."""

import logging

from markdown_it.presets import commonmark
from markdown_it.renderer import RendererHTML
from markdown_it.utils import OptionsDict

from .bib import bib_to_html
from .gloss import gloss_to_html
from .include import inclusion_to_html
from .patterns import (
    BREAK,
    CITE,
    CODE_CLOSE,
    CODE_OPEN,
    COMMENT,
    DIV_CLASS_MARKDOWN,
    DIV_CLASS_SPECIAL,
    DIV_CLOSE,
    EM_CLOSE,
    EM_OPEN,
    FIGURE,
    FIGURE_CAP,
    FIGURE_ID,
    FIGURE_INFO,
    FIGURE_REF,
    GLOSS_REF,
    GLOSS_INDEX,
    HEADING_CLASS,
    HEADING_ID,
    INCLUSION,
    INDEX_DEF,
    LINECOUNT,
    SECTION_CLOSE,
    SECTION_OPEN,
    SECTION_REF,
    STRONG_CLOSE,
    STRONG_OPEN,
    SUP_CLOSE,
    SUP_OPEN,
    TABLE_BODY,
    TABLE_CAP,
    TABLE_ID,
    TABLE_RAW,
    TABLE_REF,
    TABLE_START,
)
from .util import LOGGER_NAME, MISSING, err, loc, make_inclusion_filename, make_md

LOGGER = logging.getLogger(LOGGER_NAME)


def render(config, xref, seen, info, noisy=True):
    """Turn token stream into HTML."""
    options = OptionsDict(commonmark.make()["options"])
    renderer = McColeRenderer(config, xref, seen, info, noisy)
    return renderer.render(info.tokens, options, {})


# ----------------------------------------------------------------------


class McColeRenderer(RendererHTML):
    """Translate token stream to HTML."""

    def __init__(self, config, xref, seen, info, noisy=True):
        """Remember settings and cross-reference information."""
        super().__init__(self)
        self.config = config
        self.xref = xref
        self.seen = seen
        self.info = info
        self.noisy = noisy
        self.section = None

    # ------------------------------------------------------------------

    def heading_open(self, tokens, idx, options, env):
        """Add IDs to headings if requested."""
        inline = tokens[idx + 1]
        assert inline.type == "inline"
        for child in inline.children:
            if child.type == "text":
                match = HEADING_CLASS.search(child.content)
                if match:
                    heading_class = match.group(3)
                    child.content = child.content.replace(match.group(2), "")
                    tokens[idx].attrSet("class", heading_class)

                match = HEADING_ID.search(child.content)
                if match:
                    heading_id = match.group(3)
                    child.content = child.content.replace(match.group(2), "")
                    tokens[idx].attrSet("id", heading_id)

        result = RendererHTML.renderToken(self, tokens, idx, options, env)
        return result

    def html_block(self, tokens, idx, options, env):
        """Look for special entries for bibliography, glossary, etc."""
        for (pat, method) in (
            (COMMENT, self._comment),
            (DIV_CLASS_MARKDOWN, self._div_markdown),
            (DIV_CLASS_SPECIAL, self._div_special),
            (FIGURE, self._figure),
            (INCLUSION, self._inclusion),
            (SECTION_OPEN, self._section),
            (SECTION_CLOSE, self._copy),
            (TABLE_RAW, self._raw_table),
            (TABLE_START, self._table),
            (DIV_CLOSE, self._copy),  # must come last
        ):
            match = pat.search(tokens[idx].content)
            if match:
                return method(tokens, idx, match)
        return self.html_inline(tokens, idx, options, env)

    def html_inline(self, tokens, idx, options, env):
        """Fill in span elements with cross-references."""
        token = tokens[idx]
        for (pat, method) in (
            (BREAK, self._copy),
            (CODE_OPEN, self._copy),
            (CODE_CLOSE, self._copy),
            (EM_OPEN, self._copy),
            (EM_CLOSE, self._copy),
            (CITE, self._cite),
            (COMMENT, self._comment),
            (FIGURE_REF, self._figure_ref),
            (GLOSS_REF, self._gloss_ref),
            (GLOSS_INDEX, self._gloss_index),
            (INDEX_DEF, self._index_def),
            (LINECOUNT, self._linecount),
            (SECTION_REF, self._section_ref),
            (STRONG_OPEN, self._copy),
            (STRONG_CLOSE, self._copy),
            (SUP_OPEN, self._copy),
            (SUP_CLOSE, self._copy),
            (TABLE_REF, self._table_ref),
        ):
            match = pat.search(token.content)
            if match:
                return method(tokens, idx, match)

        # Text for citations generated by `_cite`, so ignore closing tag.
        if tokens[idx].content == "</cite>":
            return ""

        # Closing spans for glossary and index references are retained.
        if tokens[idx].content == "</span>":
            return "</span>"

        self._error(f"Unknown HTML {loc(self.info, token)}: {token.content}")
        return str(tokens[idx].content)

    # ------------------------------------------------------------------

    def _cite(self, tokens, idx, match):
        """Translate bibliographic citations."""
        token = tokens[idx + 1]
        assert token.type == "text"
        keys = [k.strip() for k in token.content.split(",")]
        self._check_for_unknown("citation", "bib_keys", token, *keys)
        self.seen.cite.update(keys)
        refs = [f'<a href="../bibliography/#{k}">{k}</a>' for k in keys]
        token.content = ""  # Erase citation key text so it won't be echoed.
        return f"[{', '.join(refs)}]"

    def _comment(self, tokens, idx, match):
        """Copy comments verbatim for now."""
        return tokens[idx].content

    def _copy(self, tokens, idx, match):
        """Copy HTML verbatim."""
        return tokens[idx].content

    def _div_markdown(self, tokens, idx, match):
        """Starting a 'div' that contains Markdown."""
        cls = match.group(1)
        return f'<div class="{cls}">'

    def _div_special(self, tokens, idx, match):
        """A 'div' that marks a special section."""
        what = match.group(1)
        if what == "bibliography":
            return bib_to_html(self.config)
        elif what == "glossary":
            return gloss_to_html(self.config, self.seen)
        elif what == "links":
            return self._links(self.config)
        LOGGER.error(f"Unrecognized special div class '{what}'")
        return tokens[idx].content

    def _figure(self, tokens, idx, match):
        """Generate a figure."""
        text = tokens[idx].content

        figure_id = FIGURE_ID.search(text)
        if figure_id:
            figure_id = figure_id.group(1)
            label = self.xref.fig_id_to_index.get(figure_id, None)
            if label:
                label = ".".join(str(i) for i in label)
            else:
                label = self._report_unknown("figure ID", figure_id, tokens[idx])
        else:
            label = None

        original = FIGURE_CAP.search(text)
        if not original:
            self._error(f"Figure missing caption: {text}", tokens[idx])
        elif label:
            original = original.group(1)
            term = self._choose_term("figure")
            fixed = f"{term}&nbsp;{label}: {original}"
            text = text.replace(original, fixed)

        info = FIGURE_INFO.search(text)
        if not info:
            self._error(f"Badly-formatted img tag: {text}", tokens[idx])
        elif self.section:
            fixed = f'<img src="{self.section}/{info.group(1)}" alt="{info.group(2)}"/>'
            text = text.replace(info.group(0), fixed)

        return text

    def _figure_ref(self, tokens, idx, match):
        """Fill in figure reference."""
        key = match.group(1)
        self.seen.figure_ref.add(key)
        label = self._make_crossref_label("fig_id_to_index", key, "figure")
        href = self._make_crossref_href("figure", "fig_id_to_slug", key, tokens[idx])
        return f'<a class="figref" href="{href}">{label}</a>'

    def _gloss_ref(self, tokens, idx, match):
        """Fill in glossary definition."""
        key = match.group(1)
        self._check_for_unknown("glossary", "gloss_keys", tokens[idx], key)
        self.seen.gloss_ref.add(key)
        return f'<span g="{key}">'

    def _gloss_index(self, tokens, idx, match):
        """Fill in glossary+index definition."""
        gloss_key = match.group(1)
        index_key = match.group(2)
        self._check_for_unknown("glossary", "gloss_keys", tokens[idx], gloss_key)
        self.seen.gloss_ref.add(gloss_key)
        self.seen.index_ref.add(index_key)
        return f'<span g="{gloss_key}" i="{index_key}">'

    def _inclusion(self, tokens, idx, match):
        """Fill in file inclusion."""
        return inclusion_to_html(self.info, match.group(1), self.section)

    def _index_def(self, tokens, idx, match):
        """Fill in index definition."""
        key = match.group(1)
        self.seen.index_ref.add(key)
        return f'<span i="{key}">'

    def _linecount(self, tokens, idx, match):
        """Count lines in file."""
        filename = make_inclusion_filename(self.info, match.group(1), self.section)
        try:
            with open(filename, "r") as reader:
                return str(len(reader.readlines()))
        except OSError:
            self._error(f"Unable to open {filename} to count lines", tokens[idx])
            return MISSING

    def _raw_table(self, tokens, idx, match):
        """Pass raw tables through unaltered."""
        return tokens[idx].content

    def _section(self, tokens, idx, match):
        """Sections in single-page version."""
        self.section = match.group(1)
        return tokens[idx].content

    def _section_ref(self, tokens, idx, match):
        """Fill in section reference."""
        section_id = match.group(1)
        label = self.xref.hd_id_to_index.get(section_id, None)
        if label:
            word = self._choose_term("section", label)
            label = ".".join(str(i) for i in label)
            label = f"{word}&nbsp;{label}"
        else:
            # Error reporting handled elsewhere
            label = MISSING
        href = self._make_crossref_href(
            "section", "hd_id_to_slug", section_id, tokens[idx]
        )
        return f'<a class="secref" href="{href}">{label}</a>'

    def _table(self, tokens, idx, match):
        """Parse a table nested inside a div."""
        opening, caption, body = self._get_table_fields(tokens[idx])
        md = make_md()
        html = md.render(body)
        if not html:
            return MISSING
        return html.replace("<table>", f"{opening}{caption}")

    def _table_ref(self, tokens, idx, match):
        """Fill in table reference."""
        key = match.group(1)
        self.seen.table_ref.add(key)
        label = self._make_crossref_label("tbl_id_to_index", key, "table")
        term = self._choose_term("table")
        href = self._make_crossref_href("table", "tbl_id_to_slug", key, tokens[idx])
        return f'<a class="tblref" href="{href}">{label}</a>'

    # ------------------------------------------------------------------

    def _check_for_unknown(self, kind, lookup_key, token, *item_keys):
        """Report any missing keys."""
        missing = [k for k in item_keys if k not in getattr(self.config, lookup_key)]
        if missing:
            missing = ", ".join(missing)
            self._report_unknown(kind, missing, token)

    def _choose_term(self, kind, label=None):
        """Choose appropriate word for part of document."""
        terms = self.config.terms[self.config.lang]
        if kind in {"figure", "table"}:
            return terms[kind]
        if kind == "section":
            if len(label) > 1:
                return terms["section"]
            if label[0].isdigit():
                return terms["chapter"]
            return terms["appendix"]
        self._error(f"Unknown kind of term {kind}")
        return MISSING

    def _error(self, message, token=None):
        """Potentially report an error message."""
        if not self.noisy:
            return
        if token is None:
            LOGGER.error(message)
            return
        err(message, self.info, token)

    def _get_table_fields(self, token):
        """Extract and format table information."""
        content = token.content
        table_id = TABLE_ID.search(content)
        cap = TABLE_CAP.search(content)
        body = TABLE_BODY.search(content)

        if table_id:
            table_id = table_id.group(1)
            label = self.xref.tbl_id_to_index.get(table_id, None)
        else:
            table_id = MISSING
            label = None

        if label:
            label = ".".join(str(i) for i in label)
        else:
            label = self._report_unknown("table ID", table_id, token)

        if cap:
            cap = cap.group(1)
        else:
            self._error(f"Table missing caption", token)
            cap = MISSING

        if body:
            body = body.group(1)
        else:
            self._error(f"Table missing body", token)
            body = ""

        opening = f'<table id="{table_id}">'
        caption = f"<caption>Table&nbsp;{label}: {cap}</caption>"
        return opening, caption, body

    def _links(self, config):
        """Create a links table."""
        links = config.links_data
        links.sort(key=lambda x: x["title"].lower())
        links = [
            f'<tr><td>{x["title"]}</td><td><a href="{x["url"]}">{x["url"]}</a></td></tr>'
            for x in links
        ]
        return "\n".join(
            [
                '<table class="links">',
                "<tr><th>Title</th><th>URL</th></tr>",
                "\n".join(links),
                "</table>",
            ]
        )

    def _make_crossref_href(self, kind, lookup_key, item_key, token):
        """Make cross-reference URL."""
        slug = getattr(self.xref, lookup_key).get(item_key, None)
        if slug is None:
            self._error(f"Unknown {kind} key {item_key}", token)
            return MISSING
        elif slug == self.info.slug:
            return f"#{item_key}"
        else:
            return f"{self.info.to_root}/{slug}/#{item_key}"

    def _make_crossref_label(self, lookup_key, item_key, kind):
        """Make cross-reference label text."""
        label = getattr(self.xref, lookup_key).get(item_key, None)
        if label:
            label = ".".join(str(i) for i in label)
        else:
            label = MISSING
        prefix = self._choose_term(kind)
        return f"{prefix}&nbsp;{label}"

    def _report_unknown(self, kind, missing_id, token):
        self._error(f"Unknown {kind} key {missing_id}", token)
        return MISSING
