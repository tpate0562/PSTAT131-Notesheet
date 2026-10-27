#!/bin/bash
# Usage: tools/check_fragment.sh sections/<name>.tex [raw|distilled]
# Compiles ONE fragment standalone in a private temp dir (safe to run in parallel),
# runs makeindex, and reports LaTeX errors, overfull boxes, pages and index entries.
set -u
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
FRAG="$(cd "$(dirname "$1")" && pwd)/$(basename "$1")"
MODE="${2:-raw}"
T="$(mktemp -d "$ROOT/work/tmp/chk.XXXXXX")"
cp "$ROOT/cheatsheet.sty" "$ROOT/ixgrid.ist" "$ROOT/index_aliases.tex" "$T/"
[ -d "$(dirname "$FRAG")/figs" ] && cp -R "$(dirname "$FRAG")/figs" "$T/" 2>/dev/null
NAME="$(basename "$FRAG" .tex)"
cat > "$T/t.tex" <<TEX
\documentclass[9pt,twocolumn]{extarticle}
\usepackage{cheatsheet}
\input{index_aliases}
\graphicspath{{$ROOT/}{$ROOT/sections/}}
\begin{document}${GRID:+\gridlinestrue}
\ixwritealiases
\sheetpart{Test}{TEST: \detokenize{$NAME}}
\ix$MODE
\input{$FRAG}
\printgridindex
\end{document}
TEX
cd "$T"
pdflatex -interaction=nonstopmode -halt-on-error t.tex > run1.out 2>&1
makeindex -q -s ixgrid.ist t.idx >/dev/null 2>&1
pdflatex -interaction=nonstopmode -halt-on-error t.tex > run2.out 2>&1
STATUS=$?
echo "== fragment: $FRAG"
echo "== temp dir: $T  (PDF: $T/t.pdf)"
if grep -q "^!" t.log; then
  echo "== ERRORS:"; grep -n -A6 "^!" t.log | head -60
else
  echo "== no LaTeX errors (exit $STATUS)"
fi
echo "== overfull hboxes: $(grep -c 'Overfull \\hbox' t.log)  (worst 5:)"
grep 'Overfull \\hbox' t.log | sort -t'(' -k2 -rn | head -5
echo "== missing chars: $(grep -c 'Missing character' t.log)"
echo "== pages: $(grep -o 'Output written on t.pdf ([0-9]* page' t.log | grep -o '[0-9]* page')"
echo "== index entries written: $(grep -c indexentry t.idx 2>/dev/null)"
grep -i "makeindex\|Warning" t.ilg 2>/dev/null | head -5
