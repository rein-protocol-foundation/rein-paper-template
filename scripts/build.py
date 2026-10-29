#!/usr/bin/env python3
"""Build both papers with latexmk/pdfLaTeX, using Tectonic when latexmk is unavailable.

Usage: python3 scripts/build.py [--engine /path/to/tectonic] [--offline]
Build logs and intermediates are retained in build/. Final PDFs go in output/.
"""
import argparse
import re
from pathlib import Path
import shutil
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[1]

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--engine", help="latexmk or Tectonic executable")
    parser.add_argument("--offline", action="store_true",
                        help="Tectonic: use cached TeX resources only")
    parser.add_argument("--bundle", help="Tectonic: optional local TeX resource bundle")
    args = parser.parse_args()
    engine = (shutil.which(args.engine) if args.engine else
              shutil.which("latexmk") or shutil.which("tectonic"))
    if not engine:
        sys.exit("TeX compiler not found or not executable. Install full TeX Live/MacTeX "
                 "(latexmk, pdflatex, bibtex), or Tectonic, and add it to PATH. "
                 "See README.md: Build and package locally. "
                 "Python/pip does not install these tools.")
    if "latexmk" in Path(engine).name:
        missing = [tool for tool in ("pdflatex", "bibtex") if not shutil.which(tool)]
        if missing:
            sys.exit("Missing TeX tools on PATH: " + ", ".join(missing) +
                     ". Install full TeX Live/MacTeX and reopen your terminal. "
                     "See README.md: Build and package locally.")
        if args.offline or args.bundle:
            parser.error("--offline and --bundle require --engine tectonic")
    output = ROOT / "output"
    output.mkdir(exist_ok=True)
    sources = [p for p in [ROOT / "main.tex", ROOT / "main-double.tex"] if p.exists()]
    for path in sources:
        source = path.name
        label = "double-column" if "[twocolumn" in path.read_text() else "single-column"
        target = ROOT / "build" / label
        target.mkdir(parents=True, exist_ok=True)
        if "latexmk" in Path(engine).name:
            cmd = [engine, "-pdf", "-interaction=nonstopmode", "-halt-on-error",
                   f"-outdir={target}", source]
        else:
            cmd = [engine, "--keep-logs", "--keep-intermediates",
                   "--outdir", str(target)]
            if args.offline:
                cmd.append("--only-cached")
            if args.bundle:
                cmd.extend(["--bundle", args.bundle])
            cmd.append(source)
        print(f"Building {label} with {Path(engine).name} ...", flush=True)
        run = subprocess.run(cmd, cwd=ROOT, text=True, stdout=subprocess.PIPE,
                             stderr=subprocess.STDOUT)
        (target / "compile.log").write_text(run.stdout)
        print(run.stdout, end="")
        if run.returncode:
            sys.exit(run.returncode)
        pdf = target / (Path(source).stem + ".pdf")
        if not pdf.is_file():
            sys.exit(f"Compiler returned without producing {pdf}")
        tex_log = target / (Path(source).stem + ".log")
        if tex_log.exists():
            log_text = tex_log.read_text(errors="replace")
            if re.search(r"(?:Reference|Citation) .* undefined|There were undefined", log_text):
                sys.exit(f"Unresolved references or citations; inspect {tex_log}")
        bib_log = target / (Path(source).stem + ".blg")
        if bib_log.exists() and re.search(
            r"I couldn't open|I found no |error message", bib_log.read_text(errors="replace")
        ):
            sys.exit(f"BibTeX reported an error; inspect {bib_log}")
        destination = output / f"REIN-{label}.pdf"
        shutil.copy2(pdf, destination)
        print(f"Created {destination.relative_to(ROOT)}", flush=True)

if __name__ == "__main__":
    main()
