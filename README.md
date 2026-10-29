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

### Install dependencies first

These tools are **not assumed to be installed with your operating system**. The scripts do not install dependencies automatically.

- **Python 3**: install from [python.org](https://www.python.org/downloads/) or your OS package manager. Both scripts use only the Python standard library; no `pip install` or `requirements.txt` is needed.
- **A TeX toolchain**: choose one of the options below. LaTeX packages and fonts are separate from Python libraries.
- **Git**: needed only for `git clone`; downloading and extracting this repository's ZIP is an alternative.

**Option A: TeX Live / MacTeX (pdfLaTeX).** On macOS, install the full [MacTeX distribution](https://tug.org/mactex/). On Linux or Windows, follow the [TeX Live installation guide](https://tug.org/texlive/quickinstall.html) and select the full scheme. This includes the LaTeX packages and fonts used by the template; a minimal TeX installation may not. Reopen your terminal after installation and ensure the TeX binary directory is on `PATH`.

Verify before building:

```bash
python3 --version
latexmk -v
pdflatex --version
bibtex --version
```

On Windows, use `py -3` in place of `python3` throughout these instructions if that is your Python launcher.

**Option B: Tectonic.** Follow the [official installation instructions](https://tectonic-typesetting.github.io/book/latest/installation/). On macOS with Homebrew already installed:

```bash
brew install tectonic
tectonic --version
```

Tectonic downloads required TeX resources during compilation, so the first build needs internet access. `--offline` uses cached resources only and will fail if any required resource is missing. Tectonic uses a different engine from pdfLaTeX, so typography and line breaks can differ.

### Compile the PDFs

```bash
git clone https://github.com/rein-protocol-foundation/rein-paper-template.git
cd rein-paper-template
python3 scripts/build.py
```

The script selects `latexmk` first, or Tectonic if `latexmk` is unavailable. To select Tectonic explicitly:

```bash
python3 scripts/build.py --engine tectonic
```

If a build reports a missing `.sty` file or font, install it through your TeX distribution's package manager (not `pip`), or use the full distribution above. Compilation logs are saved under `build/<layout>/compile.log`. Missing executables must be installed and available on `PATH` before retrying.

### Package for Overleaf (optional)

```bash
python3 scripts/package.py
```

Packaging needs **only Python 3** and does not compile or refresh PDFs. Run the build step first if you changed the paper and want updated PDF previews. Intermediate build files go into the ignored `build/` directory; PDFs and ZIP packages go into `output/`. Overleaf packages are English-only and exclude private material, build caches, and third-party papers.

If you use Overleaf, upload one of the provided ZIPs and select **pdfLaTeX**; you do not need to install Python or TeX locally.

## Provenance

See [PROVENANCE.md](PROVENANCE.md) for the upstream source, pinned revision, and licensing status. Provenance notes do not appear in the typeset paper. This template is independent of the website code and requires neither Node.js nor Next.js.
