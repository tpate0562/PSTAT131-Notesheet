# Build:  latexmk main.tex      (pdflatex -> makeindex with the grid style -> pdflatex)
$pdf_mode = 1;
$makeindex = 'makeindex -s ixgrid.ist %O -o %D %S';
$max_repeat = 6;
