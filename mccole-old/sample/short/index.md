---
template: page.html
---

<div class="centered" markdown="1">

For my mother, Doris Wilson,<br/>
who taught hundreds of children to read and to believe in themselves.<br/>

And for my brother Jeff, who did not live to see it finished.<br/>
"Remember, you still have a lot of good times in front of you."<br/>

All royalties from the sale of this book are being donated to<br/>
the Carpentries,<br/>
a volunteer organization that teaches<br/>
foundational coding and data science skills<br/>
to researchers worldwide.

</div>

<table>
<tr><td>left</td><td>right</td></tr>
<tr><td>left</td><td>right</td></tr>
</table>

This is \\(e^x\\) math<sup>With a footnote</sup>.

This <strong>L</strong>etter is emphasized.

<cite>UNKNOWN,CITATIONS</cite>

<!-- comment -->

Self-reference: <a section="short-section"/>.

Cross-references: <a section="file-backup"/> and <a section="unit-test-structure"/> and <a section="glossary"/>.

Glossary: <span g="gloss_key">text</span>

Index: <span i="index term">text</span>

Glossary plus index: <span g="gloss_key" i="index term">text</span>

Index wrapping link: <span i="index term">[name][acorn]</span>

Citation: <cite>Oram2007</cite> with text following
including text on the next line.

Bad figure: <a figure="no-such-figure"/>

Bad table: <a table="no-such-table"/>

> ### Blockquote
>
> This is a paragraph.
>
> So is this.

1. item
1. item
1. item
1. item
1. item
1. item
1. item
1. item
1. item
1. item
1. item
1. item
1. item
1. item
1. item
1. item

Long enough to wrap around.
Long enough to wrap around.
Long enough to wrap around.
Long enough to wrap around.
Long enough to wrap around.
Long enough to wrap around.
Long enough to wrap around.
Long enough to wrap around.

File inclusion:

<div class="include" file="test.py" />

Keep alpha:

<div class="include" file="test.txt" keep="alpha" />

Omit beta:

<div class="include" file="test.txt" omit="beta" />

Keep beta omit gamma:

<div class="include" file="test.txt" keep="beta" omit="gamma" />

Multi-inclusion of `.py` and `.out`

<div class="include" pat="multi.*" fill="py out" />

```python
for word in code:
    print f"{word} is formatted"
```

## Section heading {#short-section}

Figure reference: <a figure="short-figure"/>

<figure id="short-figure">
  <img src="figures/short.svg" alt="Short caption" />
  <figcaption>Long version of short caption.</figcaption>
</figure>

Table reference: <a table="short-table"/>

<div class="table" id="short-table" cap="Short table caption.">
| Meaning | Selector |
| ------- | -------- |
| Element with tag `"elt"` | `elt`    |
| Element with `class="cls"` | `.cls`   |
| Element with `id="ident"` | `#ident`   |
| `child` element inside a `parent` element | `parent child` |
</div>
