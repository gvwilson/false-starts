import ivy
import shortcodes
import yaml


@ivy.events.register(ivy.events.Event.INIT)
def links_append():
    """Add Markdown links table to Markdown files."""
    if "links" not in ivy.site.config:
        return

    with open(ivy.site.config["links"], "r") as reader:
        links = yaml.safe_load(reader)
    links = "\n".join([f"[{x['slug']}]: {x['url']}" for x in links])

    def visitor(node):
        if node.ext == "md":
            node.text += "\n\n" + links

    ivy.nodes.root().walk(visitor)


@shortcodes.register("links")
def links_table(pargs, kwargs, node):
    """Create a table of links."""
    if "links" not in ivy.site.config:
        return "<p>NO LINKS</p>"

    with open(ivy.site.config["links"], "r") as reader:
        links = yaml.safe_load(reader)
    links = "\n".join(
        f'<tr><td>{x["title"]}</td><td><a href="{x["url"]}">'
        f'{x["url"]}</a></td></tr>'
        for x in links
    )
    title = "<tr><th>Link</th><th>URL</th></tr>"
    return f'<table class="links-table">\n{title}\n{links}\n</table>'
