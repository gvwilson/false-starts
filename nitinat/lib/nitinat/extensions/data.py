"""Generate pages for datasets."""

import glob
import json
from pathlib import Path

import ibis
import ivy
import shortcodes


@ivy.events.register(ivy.events.Event.INIT)
def collect():
    """Collect information about datasets."""
    if "data" not in ivy.site.config:
        return
    pattern = str(Path(ivy.site.home(), ivy.site.config["data"]["src_glob"]))
    data = []
    for filename in glob.glob(pattern):
        with open(filename, "r") as reader:
            title = Path(filename).name
            data.append(
                {
                    "title": title,
                    "src": filename,
                    "dst": _output_filename(title),
                    "data": json.load(reader),
                }
            )
    ivy.site.config["data"]["datasets"] = data


@ivy.events.register(ivy.events.Event.EXIT)
def write():
    """Write information about datasets."""
    if "data" not in ivy.site.config:
        return

    out_dir = _output_directory()
    out_dir.mkdir(mode=0o755, parents=True, exist_ok=True)

    template_path = str(
        Path(ivy.site.theme(), "templates", ivy.site.config["data"]["template"])
    )
    with open(template_path, "r") as reader:
        template = ibis.Template(reader.read())

    site = {"title": ivy.site.config["title"]}
    for dataset in ivy.site.config["data"]["datasets"]:
        dst = Path(out_dir, _output_filename(dataset["title"]))
        result = template.render({"site": site} | dataset)
        result = ivy.utils.rewrite_urls(result, dst)
        with open(dst, "w") as writer:
            writer.write(result)


@shortcodes.register("datasets")
def index(pargs, kwargs, node):
    """Generate index of datasets."""
    entries = []
    for dataset in ivy.site.config["data"]["datasets"]:
        relative = Path(ivy.site.config["data"]["out_dir"], dataset["dst"])
        entries.append(
            f'<li><a href="./{relative}">{dataset["title"]}</a></li>'
        )
    return "<ul>\n" + "\n".join(entries) + "\n</ul>"


def _output_directory():
    """Construct output directory name."""
    return Path(ivy.site.out(), ivy.site.config["data"]["out_dir"])


def _output_filename(title):
    """Construct output filename."""
    return title + ".html"
