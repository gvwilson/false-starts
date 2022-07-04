"""Keep track of information."""

from dataclasses import dataclass, field

from .util import TRANSLATIONS


@dataclass
class Config:
    author: str = ""
    bib: str = ""
    bib_data: list = field(default_factory=list)
    bib_keys: set = field(default_factory=set)
    builddate: str = ""
    chapters: list = field(default_factory=list)
    copy: list = field(default_factory=list)
    copyrightyear: str = ""
    domain: str = ""
    dst: str = ""
    email: str = ""
    exclude: list = field(default_factory=list)
    gloss: str = ""
    gloss_data: list = field(default_factory=list)
    gloss_keys: set = field(default_factory=set)
    lang: str = ""
    links: str = ""
    links_data: dict = field(default_factory=dict)
    pages: list = field(default_factory=list)
    repo: str = ""
    root: str = ""
    src: str = ""
    subtitle: str = ""
    template: dict = field(default_factory=dict)
    terms: dict = field(default_factory=lambda: TRANSLATIONS)
    title: str = ""
    tool: str = ""


@dataclass
class CrossRef:
    # embedded figure ID (str) to multi-part label (tuple)
    fig_id_to_index: dict = field(default_factory=dict)

    # embedded figure ID (str) to chapter slug (str)
    fig_id_to_slug: dict = field(default_factory=dict)

    # embedded heading ID (str) to multi-part label (tuple)
    hd_id_to_index: dict = field(default_factory=dict)

    # embedded heading ID (str) to chapter slug (str)
    hd_id_to_slug: dict = field(default_factory=dict)

    # embedded heading ID (str) to chapter title (str)
    hd_id_to_title: dict = field(default_factory=dict)

    # multi-part heading label (tuple) to embedded heading ID (str)
    hd_index_to_id: dict = field(default_factory=dict)

    # embedded table ID (str) to multi-part label (tuple)
    tbl_id_to_index: dict = field(default_factory=dict)

    # embedded table ID (str) to chapter slug (str)
    tbl_id_to_slug: dict = field(default_factory=dict)


@dataclass
class Info:
    """Information about a single page."""
    dst: str = ""
    html: str = ""
    lede: str = ""
    major: str = ""
    metadata: dict = field(default_factory=dict)
    slug: str = ""
    src: str = ""
    template: str = ""
    text: str = ""
    title: str = ""
    to_root: str = ""
    tokens: list = field(default_factory=list)


@dataclass
class Seen:
    """What cross-references have been seen?"""
    cite: set = field(default_factory=set)
    figure_ref: set = field(default_factory=set)
    gloss_ref: set = field(default_factory=set)
    index_ref: set = field(default_factory=set)
    table_ref: set = field(default_factory=set)
