import setuptools

from mccole import __version__ as version

resource_files = [
    f"data/{f}"
    for f in [
        "mccole.css",
        "mccole.js",
        "bibliography.html",
        "foot.html",
        "glossary.html",
        "head.html",
        "index.html",
        "page.html",
        "titled.html",
    ]
]

setuptools.setup(
    name="mccole",
    version=version,
    url="https://github.com/gvwilson/mccole",
    author="Greg Wilson",
    author_email="gvwilson@third-bit.com",
    description="A simple publishing system",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    packages=setuptools.find_packages(exclude=["*test*"]),
    include_package_data=True,
    scripts=["bin/mccole"],
    install_requires=[
        "bibtexparser>=1.2.0",
        "markdown-it-py>=2.0.0",
        "mdit-py-plugins>=0.3.0",
        "python-frontmatter>=1.0.0"
    ],
    package_data={"": resource_files},
    classifiers=[
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.9",
    ],
)
