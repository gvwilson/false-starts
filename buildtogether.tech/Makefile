# Show help by default.
.DEFAULT_GOAL := help

## help: show available commands
.PHONY: help
help:
	@grep -h -E '^##' ${MAKEFILE_LIST} | sed -e 's/## //g' | column -t -s ':'

## build: rebuild example site
.PHONY: build
build:
	ivy build

## serve: build and serve the site
.PHONY: serve
serve:
	ivy watch

## validate: run html5validator on generated files
.PHONY: validate
validate:
	@html5validator --root docs \
	--ignore \
	'Attribute "markdown" not allowed on element' \
	'Attribute "key" not allowed on element "span"'

## lint: run software quality checks
.PHONY: lint
lint:
	@-flake8
	@-isort --check .
	@-black --check .
	@-pydocstyle --convention=google --count nexus

## reformat: reformat code in place
.PHONY: reformat
reformat:
	@isort .
	@black .

## spelling: compare words with known problems
.PHONY: spelling
spelling:
	@cat docs/*.html docs/*/*.html | aspell -H list | bin/diffset data/words.txt

## clean: remove junk files
.PHONY: clean
clean:
	@find . -name '*~' -exec rm {} \; # Emacs backup files
	@find . -name .DS_Store -exec rm {} \; # Mac preview cache
	@find . -name '*.pyc' -exec rm {} \; # Python bytecode files
	@find . -name __pycache__ -exec rmdir {} \; # Ditto
	@rm -rf ./build ./dist # Build directories
