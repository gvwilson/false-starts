SITE=./docs
LANGUAGE=en
PORT=4000

.DEFAULT: commands

## commands: show available commands
commands:
	@grep -h -E '^##' ${MAKEFILE_LIST} | sed -e 's/## //g' | column -t -s ':'

## build: rebuild site without running server
.PHONY: build
build:
	ivy build

## serve: build site and run server
.PHONY: serve
serve:
	ivy watch

## latex: create LaTeX document.
.PHONY: latex
latex:
	python bin/single-html.py docs/index.html > ./docs/all.html
	python bin/tex.py --head tex/head.tex --foot tex/foot.tex < ./docs/all.html > docs/all.tex
	echo '*.pdf' > docs/.gitignore
	cp data/bibliography.bib docs/bibliography.bib

## pdf: create PDF document.
.PHONY: pdf
pdf:
	cp tex/krantz.cls docs
	cd docs && pdflatex all
	cd docs && biber all
	cd docs && makeindex all
	cd docs && pdflatex all
	cd docs && pdflatex all

## ----

## clean: clean up stray files
clean:
	@find . -name '*~' -exec rm {} \;

## validate: run html5validator on generated files
validate: ${HOME_PAGE}
	@html5validator --root docs --ignore \
	'Attribute "markdown" not allowed' \
	'Attribute "index-key" not allowed on element "span"' \
	'Attribute "index-ref" not allowed on element "a"'

# Local commands if available.
-include local.mk
