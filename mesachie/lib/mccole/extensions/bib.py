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
    keys = [f'<a href="@root/bib/#{k}">{k}</a>' for k in pargs]
    return f"[{', '.join(keys)}]"


@shortcodes.register("bibliography")
def bibliography(pargs, kwargs, node):
    """Convert bibliography to HTML."""
    util.require((not pargs) and (not kwargs), "Bad 'bibliography' shortcode")
    if (filename := ivy.site.config.get("bibliography", None)) is None:
        return '<p class="warning">No bibliography specified.</p>'
    if (style := ivy.site.config.get("bibliography_style", None)) is None:
        return '<p class="warning">No bibliography style specified.</p>'

    # Set up Pybtex.
    html = find_plugin("pybtex.backends", "html")()
    style = find_plugin("pybtex.style.formatting", style)()

    # Format a single bibliography entry.
    def _format(key, body):
        return f'<dt id="{key}">{key}</dt>\n<dd>{body}</dd>'

    # Generate HTML.
    filename = Path(ivy.site.home(), filename)
    bib = parse_file(filename)
    formatted = style.format_bibliography(bib)
    entries = [
        _format(entry.key, entry.text.render(html)) for entry in formatted
    ]
    return '<dl class="bibliography">\n\n' + "\n\n".join(entries) + "\n\n</dl>"
