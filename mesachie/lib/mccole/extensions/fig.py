"""Handle figures and figure references."""

from textwrap import dedent

import shortcodes
import util


@shortcodes.register("f")
def figure_ref(pargs, kwargs, node):
    """Handle [% f slug %] figure reference shortcodes."""
    util.require((len(pargs) == 1) and (not kwargs), "Bad 'f' shortcode")
    slug = pargs[0]
    cls = 'class="figref"'
    return f'<a {cls} href="FIXME">Figure&nbsp;{slug}</a>'


@shortcodes.register("figure")
def figure_def(pargs, kwargs, node):
    """Handle [% figure slug=slug img=img alt=alt caption=cap %] figure definition."""
    util.require(
        (not pargs)
        and {"slug", "img", "alt", "caption"}.issuperset(kwargs.keys()),
        "Bad 'figure' shortcode",
    )
    slug = kwargs["slug"]
    img = kwargs["img"]
    alt = kwargs["alt"]
    caption = kwargs["caption"]
    return dedent(
        f"""\
    <figure id="{slug}">
      <img src="./{img}" alt="{alt}"/>
      <figcaption markdown="1">FIXME: {caption}</figcaption>
    </figure>
    """
    )
