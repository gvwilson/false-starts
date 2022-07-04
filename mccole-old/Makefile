SRC=mccole
RUN=python -m mccole -u
DOC_SRC=_docs
PORT=4000

# Show help by default.
.DEFAULT_GOAL := help

## help: show available commands
.PHONY: help
help:
	@grep -h -E '^##' ${MAKEFILE_LIST} | sed -e 's/## //g' | column -t -s ':'

## test: run unit tests
.PHONY: test
test:
	@pytest tests

## build: build and check package
.PHONY: build
build:
	python setup.py sdist bdist_wheel
	twine check dist/*

## upload: push package to PyPi Test
upload:
	twine upload --repository-url https://test.pypi.org/legacy/ dist/*

## install: build package and install locally
.PHONY: install
install:
	python setup.py install

## coverage: run available tests and report coverage
.PHONY: coverage
coverage:
	@coverage run -m pytest
	@coverage html

## docs: build sample site for publication
.PHONY: docs
docs: docs-copy
	@mkdocs build

## docs-serve: build and serve sample site for publication
.PHONY: docs-serve
docs-serve: docs-copy
	@mkdocs serve

## docs-copy: copy files into docs source directory
.PHONY: docs-copy
docs-copy:
	@${RUN} -C sample -d ${PWD}/${DOC_SRC}/sample
	@cp README.md ${DOC_SRC}/index.md
	@cp LICENSE.md ${DOC_SRC}/license.md
	@cp CODE_OF_CONDUCT.md ${DOC_SRC}/conduct.md

## sample: build sample site for testing
.PHONY: sample
sample:
	@${RUN} -C sample --onepage all.html

## sample-serve: build sample site for testing
.PHONY: sample-serve
sample-serve:
	@${RUN} -C sample --onepage all.html -r ${PORT}

## lint: run software quality checks
.PHONY: lint
lint:
	@-flake8
	@-isort --check .
	@-black --check .
	@-pydocstyle --convention=google --count ${SRC}

## reformat: reformat code in place
.PHONY: reformat
reformat:
	@isort .
	@black .

## clean: remove junk files
.PHONY: clean
clean:
	@find . -name '*~' -exec rm {} \;
	@find . -name __pycache__ -delete
	@find . -name .DS_Store -exec rm {} \;
	@rm -rf build dist htmlcov mccole.egg-info sample/_site
