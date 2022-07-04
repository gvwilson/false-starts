"""Handle glossary references and glossary."""

from pathlib import Path

import ivy
import shortcodes
import util
import yaml


@shortcodes.register("g")
def glossary_ref(pargs, kwargs, node):
    """Handle [% g slug "text" %] glossary reference shortcodes."""
    util.require((len(pargs) == 2) and (not kwargs), "Bad 'g' shortcode")
    slug = pargs[0]
    text = pargs[1]
    cls = 'class="glossref"'
    return f'<a {cls} href="@root/gloss/#{slug}" markdown="1">{text}</a>'


@shortcodes.register("glossary")
def glossary(pargs, kwargs, node):
    """Convert glossary to Markdown."""
    util.require((not pargs) and (not kwargs), "Bad 'glossary' shortcode")
    if (filename := ivy.site.config.get("glossary", None)) is None:
        return '<p class="warning">No glossary specified.</p>'
    if (lang := ivy.site.config.get("lang", None)) is None:
        return '<p class="warning">No language specified.</p>'

    filename = Path(ivy.site.home(), filename)
    with open(filename, "r") as reader:
        glossary = yaml.safe_load(reader) or {}

    try:
        glossary.sort(key=lambda x: x[lang]["term"].lower())
    except KeyError as exc:
        util.fail(f"Glossary entries missing key, term, or {lang}: {exc}.")

    return "\n\n".join(
        _as_markdown(glossary, lang, entry) for entry in glossary
    )


def _as_markdown(glossary, lang, entry):
    """Convert a single glossary entry to Markdown."""
    cls = 'class="glosskey"'
    first = f'<span {cls} id="{entry["key"]}">{entry[lang]["term"]}</span>'

    if "acronym" in entry[lang]:
        first += f" ({entry[lang]['acronym']})"

    body = util.MULTISPACE.sub(entry[lang]["def"], " ").rstrip()

    if "ref" in entry[lang]:
        seealso = util.TRANSLATIONS[lang]["seealso"]
        try:
            refs = [f"[{glossary[r]}](#{r})" for r in entry[lang]["ref"]]
        except KeyError as exc:
            util.fail(
                f"Unknown glossary cross-ref key in {entry['key']}: {exc}"
            )
        body += f"<br/>{seealso}: {', '.join(refs)}."

    result = f"{first}\n:   {body}"
    return result
