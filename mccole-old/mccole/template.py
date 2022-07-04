"""Evaluate page templates to fill in content."""

import logging
import os
from datetime import datetime
from glob import glob
from types import SimpleNamespace as SN

from .util import LOGGER_NAME

# Where templates live.
TEMPLATE_DIR = "_template"

LOGGER = logging.getLogger(LOGGER_NAME)


def fill_template(config, xref, info, site, html):
    """Fill in page template if present."""
    template_name = info.metadata.get("template", None)
    if template_name is None:
        template_name = info.template
    if template_name is None:
        LOGGER.error(f"No template in {info.src}.")
        return html

    template = config.template.get(template_name, None)
    if template is None:
        LOGGER.error(f"Unknown template {template_name} in {info.src}.")
        return html

    LOGGER.debug(f"filling {template_name} for {info.src}")

    site.toc = lambda level: _toc(config, xref, level=level)
    page = SN(
        content=lambda: html,
        keyterms=lambda: _keyterms(config, info),
        lede=lambda: _lede(config, info),
        title=lambda: f'<h1 id="{info.slug}">{info.title}</h1>',
        to_root=lambda: info.to_root,
        toc=lambda: _toc(config, xref, major=info.major)
    )

    return _fill(template_name, template, site, page)


def load_templates(config):
    """Load page templates."""
    config.template = {}
    for filename in glob(f"{TEMPLATE_DIR}/*.html"):
        label = os.path.basename(filename)
        with open(filename, "r") as reader:
            text = reader.read()
            if "'''" in text:
                LOGGER.warning(f"Template {filename} contains triple quote '''.")
            config.template[label] = text


def make_site_object(config, seen):
    """Make object with site values for evaluation."""
    now = datetime.today().strftime("%Y-%m-%d")
    subtitle = (
        f'<h2 class="subtitle">{config.subtitle}</h2>'
        if config.subtitle
        else ""
    )
    site = SN(
        author=lambda: config.author,
        builddate=lambda: now,
        copyrightyear=lambda: config.copyrightyear,
        domain=lambda: config.domain,
        email=lambda: config.email,
        lang=lambda: config.lang,
        repo=lambda: config.repo,
        title=lambda: config.title,
        subtitle=lambda: subtitle,
        tool=lambda: config.tool
    )

    if "foot.html" in config.template:
        site.foot = lambda root: _fill(
            "foot.html",
            config.template["foot.html"],
            site,
            SN(root=root)
        )
    else:
        site.foot = lambda root: ""

    if "head.html" in config.template:
        site.head = lambda root: _fill(
            "head.html",
            config.template["head.html"],
            site,
            SN(root=root)
        )
    else:
        site.head = lambda root: ""

    if "stats.html" in config.template:
        filled = _fill("stats.html", config.template["stats.html"], site, SN())
        site.stats = lambda: filled
    else:
        site.stats = lambda: ""

    return site


# ----------------------------------------------------------------------


def _fill(template_name, template, site, page):
    """Do filling in a function of its own to control variables in scope."""
    if "'''" in template:
        LOGGER.error(f"{template_name} contains '''")
        return ""

    filler = f"f'''{template}'''"
    try:
        return eval(filler, {}, {"site": site, "page": page})
    except AttributeError as exc:
        LOGGER.error(f"{template_name}: {exc}")
        return ""


def _keyterms(config, info):
    """Create list of key terms."""
    lang = config.lang
    to_root = info.to_root
    entries = [x for x in config.gloss_data if x.key in info.keyterms]
    if not entries:
        return ""

    entries.sort(key=lambda x: x[lang, "term"].lower())
    entries = [
        f'<a href="{to_root}/glossary/#{x.key}">{x[lang, "term"]}</a>'
        for x in entries
    ]
    return f'<div class="keyterms"><p>{", ".join(entries)}</p></div>\n'


def _lede(config, info):
    """Include chapter lede (if any)."""
    if not info.lede:
        return ""
    return f'<div class="lede"><p>{info.lede}</p></div>'


def _toc(config, xref, level=None, major=None):
    """Make a table of contents."""
    # Page-level ToC.
    if major is not None:
        indexes = [x for x in xref.hd_index_to_id if (x[0] == major) and (len(x) == 2)]
        if not indexes:
            return ""
        labels = [xref.hd_index_to_id[i] for i in indexes]
        titles = [xref.hd_id_to_title[lbl] for lbl in labels]
        combined = list(zip(indexes, labels, titles))
        links = [
            f'<li><a href="#{label}">{title}</a></li>' for (index, label, title) in combined
        ]
        links = "\n".join(links)
        html = f'<ol class="toc">\n{links}\n</ol>\n'
        return html

    # Whoops.
    assert level in {1, 2}

    # Site-level ToC
    if level == 1:
        interesting = [info for info in config.pages if info.major is not None]
        if not interesting:
            return ""
        combined = [(info.slug, info.major, xref.hd_id_to_title.get(info.slug, None), info.lede or "")
                    for info in interesting]
        refs = [
            f'<tr><td class="toc-index">{major}</td>'
            f'<td><a href="./{slug}/">{title}</a></td>'
            f"<td>{lede}</td></tr>"
            for (slug, major, title, lede) in combined
            if (title is not None)
        ]
        refs = "\n".join(refs)
        return f'<table class="toc">\n{refs}\n</table>\n'

    # All-in-one ToC.
    entries = ['<ol class="toc">']
    for info in config.pages:
        # Skip unnumbered entries.
        slug = info.slug
        if slug not in xref.hd_id_to_title:
            continue
        major = info.major
        title = xref.hd_id_to_title[slug]
        entries.append(f'<li value="{major}"><a href="#{slug}">{title}</a>')
        entries.append(_toc(config, xref, major=major))
        entries.append("</li>")
    entries.append("</ol>")
    return "\n".join(entries)
