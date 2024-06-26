"""Generate bibliography."""

from pathlib import Path

import ivy
import shortcodes
import util
from pybtex.database import parse_file
from pybtex.plugin import find_plugin


@shortcodes.register("b")
def bibliography_ref(pargs, kwargs, node):
    """Handle [% b key1 key2 %] biblography reference shortcodes."""
    util.require((len(pargs) > 0) and (not kwargs), "Bad 'b' shortcode")

    used = util.make_config("bibliography")
    used.update(pargs)

    links = [f'<a href="@root/bib/#{k}">{k}</a>' for k in pargs]
    return f"[{', '.join(links)}]"


@shortcodes.register("bibliography")
def bibliography(pargs, kwargs, node):
    """Convert bibliography to HTML."""
    util.require(not pargs, "Bad 'bibliography' shortcode")

    if (filename := ivy.site.config.get("bibliography", None)) is None:
        return '<p class="warning">No bibliography specified.</p>'
    if (stylename := ivy.site.config.get("bibliography_style", None)) is None:
        util.fail("No bibliography style specified")
    breaks = set(x.strip() for x in kwargs.get("breaks", "").split(","))

    bib = _read_bibliography(filename, stylename)

    html = find_plugin("pybtex.backends", "html")()

    def _format(key, body):
        b = " break-before" if key in breaks else ""
        return f'<p id="{key}" class="continue{b}"><strong>[{key}]</strong> {body}</p>'

    entries = [_format(entry.key, entry.text.render(html)) for entry in bib]
    return '<dl class="bibliography">\n\n' + "\n\n".join(entries) + "\n\n</dl>"


@ivy.events.register(ivy.events.Event.EXIT)
def check():
    """Check that bibliogrpahy entries are defined and used."""
    if (filename := ivy.site.config.get("bibliography", None)) is None:
        return
    if (stylename := ivy.site.config.get("bibliography_style", None)) is None:
        util.fail("No bibliography style specified")

    bib = _read_bibliography(filename, stylename)
    defined = {e.key for e in bib.entries}

    if (used := util.get_config("bibliography")) is None:
        return

    util.report("unknown bibliography references", used - defined)
    util.report("unused bibliography entries", defined - used)


def _read_bibliography(filename, style):
    """Load the bibliography file."""
    filename = Path(ivy.site.home(), filename)
    bib = parse_file(filename)

    style = find_plugin("pybtex.style.formatting", style)()
    return style.format_bibliography(bib)
