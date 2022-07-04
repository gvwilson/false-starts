"""Create links table."""

from pathlib import Path

import ivy
import shortcodes
import yaml


@ivy.events.register(ivy.events.Event.INIT)
def links_append():
    """Add Markdown links table to Markdown files."""
    if "links" not in ivy.site.config:
        return

    links = _read_links()
    links = "\n".join([f"[{x['key']}]: {x['url']}" for x in links])

    def visitor(node):
        if node.ext == "md":
            node.text += "\n\n" + links

    ivy.nodes.root().walk(visitor)


@shortcodes.register("links")
def links_table(pargs, kwargs, node):
    """Create a table of links."""
    if "links" not in ivy.site.config:
        return "<p>NO LINKS</p>"

    links = _read_links()
    links = "\n".join(
        f'<tr><td>{x["title"]}</td><td><a href="{x["url"]}">'
        f'{x["url"]}</a></td></tr>'
        for x in links
    )
    title = "<tr><th>Link</th><th>URL</th></tr>"
    return f'<table class="links-table">\n{title}\n{links}\n</table>'


def _read_links():
    """Read links file."""
    filepath = Path(ivy.site.home(), ivy.site.config["links"])
    with open(filepath, "r") as reader:
        return yaml.safe_load(reader)
