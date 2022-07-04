"""Headings and cross-references."""

import ivy
import shortcodes
import util


@shortcodes.register("x")
def heading_ref(pargs, kwargs, node):
    """Handle [% x slug %] section reference."""
    util.require((len(pargs) == 1) and not kwargs, "Bad 'x' shortcode")
    slug = pargs[0]
    return f'<a href="@root/FIXME/#{slug}">FIXME</a>'
