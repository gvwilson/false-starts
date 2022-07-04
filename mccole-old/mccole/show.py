"""Show internal state for debugging."""


def show(options, config, xref, seen):
    """Show internal state for debugging."""
    if "bib" in options.show:
        _show_bib(options, config, seen)

    if "gloss" in options.show:
        _show_gloss(options, config, seen)

    if "index" in options.show:
        _show_index(seen)

    if "pages" in options.show:
        _show_pages(options, config)

    if "xref" in options.show:
        _show_xref(options, xref)


# ----------------------------------------------------------------------


def _show_bib(options, config, seen):
    """Show bibliography keys if requested."""
    print("Bibliography keys")
    for key in sorted([entry["ID"] for entry in config.bib_data]):
        marker = "+" if key in seen.cite else "-"
        print(f"{marker} {key}")


def _show_gloss(options, config, seen):
    """Show glossary keys if requested."""
    print("Glossary keys")
    for key in sorted([entry["key"] for entry in config.gloss_data]):
        marker = "+" if key in seen.gloss_ref else "-"
        print(f"{marker} {key}")


def _show_index(seen):
    temp = set()
    for entry in seen.index_ref:
        for key in [x.strip() for x in entry.split(";")]:
            temp.add(key)
    index = {}
    for major in temp:
        if "!" in major:
            major, minor = major.split("!")
        else:
            minor = None
        if major not in index:
            index[major] = set()
        if minor is not None:
            index[major].add(minor)
    print("Index:")
    for major in sorted(index.keys(), key=lambda x: x.lower()):
        print(f"- {major}")
        for minor in sorted(index[major], key=lambda x: x.lower()):
            print(f"  - {minor}")


def _show_pages(options, config):
    """Show page information."""
    print("Pages:")
    for info in config.pages:
        print(f"- slug: {info.slug}")
        print(f"  major: {info.major}")
        print(f"  title: {info.title}")
        print(f"  src: {info.src}")
        print(f"  dst: {info.dst}")


def _show_xref(options, xref):
    """Show cross-reference table for debugging."""
    print("Cross-references")
    for kind in xref.__dict__.keys():
        print(f"- {kind}")
        for (key, value) in getattr(xref, kind).items():
            print(f"  - {key}: {value}")
