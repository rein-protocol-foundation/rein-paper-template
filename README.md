# rein-paper-template

English | [Chinese](README-zh.md)

The Rein Protocol Foundation LaTeX paper template for author accepted manuscripts, technical reports, and preprints. It uses the Foundation's R mark, full name, and warm black/orange palette.

## Template previews

First-page screenshots of the single-column and double-column layouts. Click an image to view it at full size.

| Single column · Author–year citations | Double column · Numeric citations |
| --- | --- |
| [![Single-column paper template preview](docs/previews/single-column.png)](docs/previews/single-column.png) | [![Double-column paper template preview](docs/previews/double-column.png)](docs/previews/double-column.png) |
| [View full single-column PDF](output/REIN-single-column.pdf) | [View full double-column PDF](output/REIN-double-column.pdf) |

## Create your own paper repository

Click **Use this template → Create a new repository** to create a paper repository under your own account or organization.

## Use with Overleaf

Download `output/REIN-complete-Overleaf-kit.zip` and upload it to Overleaf. Select **pdfLaTeX** as the compiler:

- `main.tex`: single-column layout with author–year citations.
- `main-double.tex`: double-column layout with numeric citations.

For just one layout, download `REIN-single-column-Overleaf.zip` or `REIN-double-column-Overleaf.zip`. Both standalone packages use `main.tex` as their entry point. The `output/` directory also contains PDF previews of both layouts.

## Adapt the template for your paper

1. Edit `paper-info-single.tex` or `paper-info-double.tex` with your title, actual authors, affiliations, email, short title, and keywords.
2. Set `\reinstatus{...}` to your manuscript's actual status and enter its version. Use `\reinstatus{AUTHOR ACCEPTED MANUSCRIPT}` only after acceptance; the default `RESEARCH TEMPLATE` does not claim acceptance.
3. Replace the instructional examples in `sections/single/` or `sections/double/` with your paper. Replace `references.bib`, figures, and experimental results with your own material.
4. Add the actual conference or journal name, year, DOI, and required publication notices. Follow the publisher's author-version and formatting policies; this template does not replace an official camera-ready style.
5. Optionally enable `\reinproject[label]{URL}`, `\reingithub{URL}`, and `\reindataset[label]{URL}`. These links are hidden by default. Do not use the Foundation homepage as a substitute for a paper's research artifacts.

Foundation website: https://rein-protocol.org. Example authors and email addresses are placeholders, not actual authors or research results.

## Optional features

- `\reinorcid{actual ORCID}`: add an ORCID link after an author's name.
- `\reinpartner{Institution name}{assets/partner-logo.pdf}`: add a partner institution's logo; hidden by default.
- `\reinacknowledgments{...}`: add acknowledgments.
- `anonymous` class option: hide template-managed authors, affiliations, logos, resource links, acknowledgments, and identifying metadata. Review the body text, self-citations, and your own images separately.
- `monochrome` class option: use grayscale styling for the paper; the official logo retains its original brand colors.

Both layouts use `reinpaper.cls`. Template commands use the `\rein` prefix; `\star` remains a mathematical symbol.

## Build and package locally

```bash
git clone https://github.com/rein-protocol-foundation/rein-paper-template.git
cd rein-paper-template
python3 scripts/build.py
python3 scripts/package.py
```

Building requires `latexmk` and pdfLaTeX from TeX Live/MacTeX. Alternatively, run `python3 scripts/build.py --engine tectonic`. Intermediate files go into the ignored `build/` directory; PDFs and self-contained ZIP packages go into `output/`. Packages exclude private material, build caches, and third-party papers.

## Provenance

See [PROVENANCE.md](PROVENANCE.md) for the upstream source, pinned revision, and licensing status. Provenance notes do not appear in the typeset paper. This template is independent of the website code and requires neither Node.js nor Next.js.
