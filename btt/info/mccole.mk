# Standard McCole theme Makefile.
.DEFAULT: commands

# Local configuration.
CONFIG := ./config.py
ABBREV := $(shell python ${CONFIG} --abbrev)
BUILD_DATE := $(shell date '+%Y-%m-%d')
STEM := ${ABBREV}-${BUILD_DATE}

# Direct variables.
EXAMPLES := $(patsubst %/Makefile,%,$(wildcard src/*/Makefile))
HTML := info/head.html info/foot.html
INFO := info/bibliography.bib info/credits.yml info/glossary.yml info/links.yml
FIG_SVG := $(wildcard src/*/*.svg)
IVY := $(wildcard lib/mccole/*/*.*)
TEX := info/head.tex info/foot.tex
TEX_COPY := info/krantz.cls info/dedication.tex
SRC := $(wildcard *.md) $(wildcard src/*.md) $(wildcard src/*/index.md) $(wildcard src/*/slides.html)

# Calculated variables.
DOCS := docs/index.html $(patsubst src/%.md,docs/%.html,$(wildcard src/*/index.md))
FIG_PDF := $(patsubst src/%.svg,docs/%.pdf,${FIG_SVG})

# Miscellaneous variables.
PORT := 4000

## commands: show available commands
commands:
	@grep -h -E '^##' ${MAKEFILE_LIST} \
	| sed -e 's/## //g' \
	| column -t -s ':'

## build: rebuild site without running server
build: ./docs/index.html
./docs/index.html: ${SRC} ${INFO} ${IVY} config.py
	ivy build && touch $@

## serve: build site and run server
.PHONY: serve
serve:
	ivy watch --port ${PORT}

## single: create single-page HTML
single: docs/all.html
docs/all.html: ./docs/index.html ${HTML} bin/single.py
	python ./bin/single.py \
	--head info/head.html \
	--foot info/foot.html \
	--root docs \
	--title "$$(python ${CONFIG} --title)" \
	--tagline "$$(python ${CONFIG} --tagline)" \
	> docs/all.html

## latex: create LaTeX document
latex: docs/${STEM}.tex
docs/${STEM}.tex: docs/all.html bin/html2tex.py ${CONFIG} ${TEX} ${TEX_COPY}
	python ./bin/html2tex.py \
	--head info/head.tex \
	--foot info/foot.tex \
	< docs/all.html \
	> docs/${STEM}.tex
	python ${CONFIG} --latex > docs/config.tex
	cp ${TEX_COPY} docs

## pdf: create PDF document
pdf: docs/${STEM}.tex ${FIG_PDF}
	cp info/bibliography.bib docs
	cd docs && pdflatex ${STEM}
	cd docs && biber ${STEM}
	cd docs && makeindex ${STEM}
	cd docs && pdflatex ${STEM}
	cd docs && pdflatex ${STEM}

## pdf-once: create PDF document with a single compilation
pdf-once: docs/${STEM}.tex ${FIG_PDF}
	cd docs && pdflatex ${STEM}

## diagrams: convert diagrams from SVG to pdf
diagrams: ${FIG_PDF}
docs/%.pdf: src/%.svg
	draw.io --export --crop --output $@ $<

## clean: clean up stray files
clean:
	@find . -name '*~' -exec rm {} \;
	@find . -name '*.bkp' -exec rm {} \;
	@find . -type d -name __pycache__ | xargs rm -r
	@rm -f \
	docs/*.aux \
	docs/*.bbl \
	docs/*.bcf \
	docs/*.blg \
	docs/*.idx \
	docs/*.ilg \
	docs/*.ind \
	docs/*.log \
	docs/*.out \
	docs/*.pdf \
	docs/*.run.xml \
	docs/*.tex \
	docs/*.toc

## lint: check project structure
.PHONY: lint
lint: clean build
	@python ./bin/lint.py \
	--config config.py

## examples: re-run examples
.PHONY: examples
examples:
	@for d in ${EXAMPLES}; do echo ""; echo $$d; make -C $$d; done

## spelling: check spelling against known words
.PHONY: spelling
spelling:
	@make wordlist \
	| python ./bin/post_spellcheck.py info/wordlist.txt

## wordlist: make a list of unknown and unused words
.PHONY: wordlist
wordlist: ./docs/index.html
	@cat ${DOCS} \
	| python ./bin/pre_spellcheck.py \
	| aspell -H list \
	| sort \
	| uniq

## count: words per file
.PHONY: count
count:
	@wc -w ${SRC} | sort -n

## valid: run html5validator on generated files
.PHONY: valid
valid: docs/all.html
	@html5validator --root docs ${DOCS} \
	--ignore \
	'Attribute "ix-key" not allowed on element "span"' \
	'Attribute "ix-ref" not allowed on element "a"' \
	'Attribute "markdown" not allowed on element'

## profile: profile compilation
.PHONY: profile
profile:
	python bin/run_profile.py

## release: create archive of standard files
.PHONY: release
release:
	zip -r mccole.zip \
	CODE_OF_CONDUCT.md \
	CONTRIBUTING.md \
	LICENSE.md \
	Makefile \
	bin \
	info/dom.yml \
	info/*.html \
	info/*.tex \
	lib \
	src/bibliography \
	src/conduct \
	src/contents \
	src/credits \
	src/glossary \
	src/license \
	src/links \
	src/syllabus \
	-x "*__pycache__*"

## publisher: create archive to send to publisher
.PHONY: publisher
publisher:
	zip -r ${STEM}.zip \
	docs/${STEM}.tex \
	docs/bibliography.bib \
	docs/config.tex \
	docs/dedication.tex \
	docs/krantz.cls \
	docs/*/*.pdf

## export: export files for publishing on the web
.PHONY: export
export:
	@zip -r ${STEM}-docs.zip \
	${DOCS} \
	docs/*.css \
	docs/*.ico \
	docs/*.svg \
	$(patsubst src/%.svg,docs/%.svg,${FIG_SVG})

## vars: show variables
.PHONY: vars
vars:
	@echo ABBREV ${ABBREV}
	@echo BUILD_DATE ${BUILD_DATE}
	@echo DOCS ${DOCS}
	@echo FIG_SVG ${FIG_SVG}
	@echo FIG_PDF ${FIG_PDF}
	@echo HTML ${HTML}
	@echo INFO ${INFO}
	@echo IVY ${IVY}
	@echo SRC ${SRC}
	@echo STEM ${STEM}
	@echo TEX ${TEX}
