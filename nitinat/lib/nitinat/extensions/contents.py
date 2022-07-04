import ivy


@ivy.events.register(ivy.events.Event.INIT)
def collect_titles():
    """Collect page titles."""
    info = {}
    ivy.nodes.root().walk(
        lambda node: info.setdefault(node.slug, node.meta["title"])
    )
    chapters = [(slug, info[slug]) for slug in ivy.site.config["chapters"]]
    appendices = [(slug, info[slug]) for slug in ivy.site.config["appendices"]]
    ivy.site.config["titles"] = {"chapters": chapters, "appendices": appendices}
