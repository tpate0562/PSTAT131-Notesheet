# Agent guide — PSTAT 131 midterm sheet (LaTeX)

Project root: `/home/user/PSTAT131-Notesheet`
(quote paths — they contain spaces). The document is `main.tex` + `cheatsheet.sty`;
each agent writes ONE OR TWO fragment files in `sections/` (named in your task) and nothing else
in the project (scratch files go in `work/tmp/<your-name>/`). Do not edit `main.tex`,
`cheatsheet.sty`, `index_aliases.tex`, or other agents' fragments.

Midterm: Wed Oct 28 2026. Coverage (Canvas Midterm Information Page): Slide Set 1 (Intro to ML;
bias-variance tradeoff; KNN), Slide Set 2 (Linear models; feature engineering; EDA), Slide Set 3
(Logistic regression; LDA/QDA; model evaluation — up until Slide 42), Reading "ROC Curves Deep Dive",
HW 1-3, Labs 1-3. Exam = <=12 multiple choice + 4 short answer, paper notes only. R code
(tidyverse + tidymodels) may be on the exam, including reading R output and spotting bugs.
Slide Set 3 pp. 43-93 (LDA/QDA) are past the cutoff but are included because practice exam Q20,
Lab 3 and HW 3 test LDA/QDA.

## Source material (already downloaded / extracted)
- Slides (image-based PDFs, 16:9). One PNG per page + text:
  `work/render/slides{1,2,3}/pNNN.png` (view these with the Read tool — they ARE the content),
  `pNNN.ocr.txt` (tesseract OCR, decent but garbles math/plots), `pNNN.txt` (PDF text layer, usually empty).
  Slide number = PDF page number (S1.23 = Slide Set 1, page 23).
- ROC reading: `source/reading/roc_tutorial.html`, text `work/text/roc_tutorial.txt`, plots `work/html_imgs/roc/imgNN.png`.
- Labs: Rmd `source/labs/lab1/lab-1/lab 1.Rmd`, `source/labs/lab2/lab-2.Rmd`, `source/labs/lab3/lab-3.Rmd`;
  knitted output text `work/text/lab{1,2,3}_html.txt`; plots `work/html_imgs/lab{1,2,3}/`.
  (Ignore `source/labs/lab2/images/lab-1/.httr-oauth` — it is a credential file, never read or copy it.)
- Homework prompts: `source/homework/homework-1-131/homework 1-131.Rmd` (+ 231 version html
  `source/homework/homework-1-1.html`), `source/homework/homework-2/homework-2.Rmd`,
  `source/homework/homework-3/homework-3.Rmd` (+ data/ folders). Text: `work/text/hw*_html.txt`.
- Student's submissions: `source/submissions/hw1_submission.{qmd,pdf}`, `hw2_submission.{Rmd,pdf}`
  (text: `work/text/hw{1,2}_submission_pdf.txt`). HW3 is NOT submitted yet.
- Practice exam + solutions: `source/practice_exam/*.pdf`, text `work/text/practice.txt`,
  `work/text/practice_sol.txt`, page images `work/render/practice{,_sol}/pNNN.png`.
- Sai's graded midterm from last quarter: `source/sai_midterm/submission_422008762.pdf`,
  text `work/text/sai_pdftext.txt`, page images `work/render/sai/pNNN.png` (+ `.ocr.txt`).
- Syllabus: `source/../` not needed.

## Document conventions
Class: `extarticle` 9pt, `twocolumn`, letter paper, tiny margins. Raw part is typeset `\small`.
NO floats (`figure`, `table`, `\begin{figure*}`), NO `\includegraphics`, NO `\newpage`/`\clearpage`,
NO new packages, NO `\usepackage`, NO `\def`/`\newcommand` of global names (local helper macros
only inside a group, prefixed with your fragment name). Column width is ~3.6 in — keep tables narrow
(use `\begin{tabular}{@{}l r r@{}}`, `tabularx` with `\linewidth`, or `\resizebox{\linewidth}{!}{...}`).
TikZ and pgfplots ARE available (`tikzpicture`, `axis`) for small diagrams — keep them <= \linewidth wide.

Available macros (from `cheatsheet.sty`):
- `\section{..}`, `\subsection{..}`, `\subsubsection{..}` (run-in).
- `\slide{set}{page}{Slide title}` — header for one slide in a raw transcription.
- `\fig{description}` — grey italic "[Figure: ...]" describing a picture/plot/diagram on the slide:
  say what is plotted (axes, curves, colours, labels, numbers, annotations) so a reader who cannot
  see it learns everything the picture conveys.
- `\src{S1.23}` — tiny source citation (use in distilled notes: `\src{S2.40}`, `\src{Lab 3}`,
  `\src{HW2 Q4}`, `\src{PE Q7}` for practice exam, `\src{Sai Q9}`).
- Boxes (breakable): `\begin{topic}{Title}..\end{topic}` (distilled topic), `\begin{keybox}[Title]..`
  (formulas/key facts), `\begin{trap}[Title]..` (common mistakes / exam traps),
  `\begin{rawsrc}{Title}..` (optional wrapper for a raw source), `\begin{qbox}{Q3 (2 pts)}..\end{qbox}`
  (question blocks) with `\ans`, `\sol` (official solution), `\mine` (student's answer), `\grader`.
- Code: `\begin{rcode} ... \end{rcode}` (R code), `\begin{routput} ... \end{routput}` (console output,
  fixed-width). Inline code: `\rc{step\_dummy()}` (argument must be LaTeX-escaped). `\pipe` = `%>%`,
  `\npipe` = `|>`, `\assign` = `<-`.
- INSIDE rcode/routput: plain ASCII only. Replace ✔→`v`, ✖→`x`, ── or —→`--`, ’‘→`'`, “”→`"`,
  ≤→`<=`, ≥→`>=`, ×→`x`, …→`...`, µ→`mu`, non-breaking spaces→space. Long output: keep it but you may
  elide with `...` rows marked `# ... (k more rows)`. Inside listings, `(*@ ... @*)` escapes to LaTeX.
- Outside listings: escape `_ % $ # & { } ~ ^` (`\_ \% \$ \# \& \{ \} \textasciitilde{} \textasciicircum{}`);
  no raw Unicode symbols — use `$\le$`, `---`, `\textrightarrow` / `$\to$`, `$\times$`, `\'e` etc.
  Curly quotes → ``` ``..'' ```. Math in `$..$` / `\[..\]` / `align*`.

## THE INDEX (most important convention)
The index lists, for every term, the page and the grid cell (A1–H11) of each place it appears.
Positions are computed automatically from where the macro sits in the final PDF, so put each macro
exactly where the term appears in the text.
- `\ix{term}` — prints `term` AND indexes it. Use it on the actual word in running text:
  `the \ix{bias-variance tradeoff} says ...`.
- `\ixh{term}` — indexes WITHOUT printing (for when the printed wording differs, e.g.
  `Overfitting\ixh{overfitting} happens when ...`, or inside math/tables/headings' neighbourhood).
- `\ixc{code}` — prints `\texttt{code}` and indexes it as code: `\ixc{step\_dummy()}`,
  `\ixc{set\_engine("kknn")}` → prefer the bare function `\ixc{set\_engine()}` and argument names
  like `\ixc{strata}`, `\ixc{one\_hot}`, `\ixc{neighbors}`.
- `\ixch{code}` — hidden code entry. Inside `rcode`/`routput` write it via an escape at the END of the
  line where the function appears: `  step_normalize(all_numeric_predictors())  (*@\ixch{step\_normalize()}\ixch{all\_numeric\_predictors()}@*)`.
- Optional sort key: `\ix[beta hat]{$\hat\beta$}`. Give one whenever the term starts with math or a symbol.
- NEVER put `\ix*` inside `\section{}`, `\subsection{}`, `\slide{}{}{TITLE}`, `\src{}` or a box title —
  put `\ixh{...}` right after the heading instead. Never inside `$...$` math.
- Density: index every substantive mention of a key concept/function (typically 2-8 per slide /
  paragraph / code block; do not index the same term twice in the same sentence). Index BOTH
  high-level concepts (overfitting, bias, ROC curve, target leakage, confounding ...) and low-level
  terms (function names, arguments, packages, metric names, output column names like `.pred_class`,
  dataset names like `abalone`, `titanic`, `diamonds`).
- Spelling: use the canonical forms below exactly (lower case except acronyms/proper nouns, singular).
  Variants are OK if listed as aliases (e.g. `\ix{KNN}` is automatically filed under
  "k-nearest neighbors (KNN)"). New terms are welcome — follow the same style.

### Canonical vocabulary (use these spellings)
Concepts: machine learning, statistical machine learning, supervised learning, unsupervised learning,
regression, classification, prediction, inference, interpretability, flexibility, parametric model,
non-parametric model, training data, testing data, validation set, training error, testing error,
overfitting, underfitting, bias, variance, bias-variance tradeoff, irreducible error, reducible error,
mean squared error (MSE), error rate, Bayes classifier, Bayes error rate, Bayes decision boundary,
decision boundary, KNN (→ k-nearest neighbors (KNN)), Euclidean distance, distance metric,
standardization, normalization, curse of dimensionality, tuning parameter, hyperparameter,
linear regression, simple linear regression, multiple linear regression, least squares,
residual sum of squares (RSS), coefficient, intercept, slope, residual, R-squared, RMSE, MAE,
p-value, hypothesis test, t-statistic, F-statistic, standard error, confidence interval,
prediction interval, categorical predictor, dummy variable, one-hot encoding, reference level,
interaction term, hierarchical principle, nonlinear relationship, polynomial regression,
transformation, log transformation, collinearity, multicollinearity, outlier, high leverage point,
heteroscedasticity, feature engineering, feature, predictor, outcome, target leakage, identifier
variable, missing data, imputation, linear imputation, mean imputation, centering, scaling,
exploratory data analysis (EDA), histogram, boxplot, scatterplot, bar plot, density plot,
correlation, Pearson correlation, correlation matrix, skewness, class imbalance, data splitting,
training/testing split, stratified sampling, random seed, reproducibility, logistic regression,
logistic function, sigmoid, odds, log odds, logit, odds ratio, maximum likelihood, confounding,
threshold, confusion matrix, true positive, false positive, true negative, false negative, accuracy,
sensitivity, specificity, TPR, FPR, precision, ROC curve, AUC, linear discriminant analysis (LDA),
quadratic discriminant analysis (QDA), naive Bayes, discriminant function, prior probability,
posterior probability, Bayes' theorem, covariance matrix, multivariate normal distribution, tidy data,
model evaluation, model comparison, cross-validation.
R/packages (with \ixc): tidyverse, tidymodels, dplyr, ggplot2, readr, tibble, parsnip, recipes,
workflows, rsample, yardstick, kknn, discrim, MASS, klaR, corrplot, corrr, naniar, ggthemes, lm, glm.
Functions (with \ixc, include the parentheses): library(), read\_csv(), head(), glimpse(), summary(),
filter(), select(), mutate(), arrange(), group\_by(), summarise(), count(), n(), factor(), levels(),
\%>\%, |>, ggplot(), aes(), geom\_histogram(), geom\_bar(), geom\_boxplot(), geom\_point(),
geom\_smooth(), facet\_wrap(), labs(), cor(), corrplot(), set.seed(), initial\_split(), training(),
testing(), recipe(), prep(), bake(), step\_dummy(), step\_normalize(), step\_center(), step\_scale(),
step\_interact(), step\_impute\_linear(), step\_impute\_mean(), step\_poly(), step\_log(),
all\_predictors(), all\_nominal\_predictors(), all\_numeric\_predictors(), starts\_with(),
imp\_vars(), linear\_reg(), logistic\_reg(), nearest\_neighbor(), discrim\_linear(),
discrim\_quad(), naive\_Bayes(), set\_engine(), set\_mode(), workflow(), add\_recipe(),
add\_model(), fit(), predict(), augment(), tidy(), extract\_fit\_parsnip(), metric\_set(),
rmse(), rsq(), mae(), accuracy(), conf\_mat(), roc\_curve(), roc\_auc(), autoplot(),
sensitivity(), specificity(), bind\_cols(), vis\_miss().
Arguments/columns (with \ixc): strata, prop, one\_hot, neighbors, type = "prob", .pred\_class,
.pred\_Yes, .estimate, truth, estimate, mode, engine.

## Raw transcription rules (Part II fragments)
- Faithful and COMPLETE: every word on every slide/page, in order, keeping the slide's bullet
  structure (`itemize`), bold/italic emphasis, equations (LaTeX), tables (`tabular`), code (`rcode`),
  output (`routput`). Do not summarise, do not skip "boring" slides (title slides, "Next..." slides —
  one line each is fine). Correct obvious OCR garbage by looking at the image.
- Every slide starts with `\slide{set}{page}{title}`; untitled slides use a short bracketed
  description as title, e.g. `\slide{1}{10}{[untitled]}`.
- Every figure/plot/diagram gets a `\fig{...}` with the information it carries (axis labels, what
  the curves show, key numbers, colours that encode classes, annotations, arrows).
- Speaker-free additions are NOT allowed in raw sections except `\fig{}` descriptions and, where a
  slide is ambiguous, a short `{\color{figgray}\itshape [note: ...]}`.
- Labs/HW: transcribe all prose instructions + every code chunk + the important printed output
  (tables of coefficients, metrics, confusion matrices, glimpse/summary output). Plots → `\fig{}`.

## Distilled notes rules (Part I fragments)
- Goal: a dense, accurate, exam-ready reference a student flips to during an open-notes exam.
  Organised by topic with `\section`/`\subsection`, `topic`/`keybox`/`trap` boxes, bullet lists,
  formulas, tiny worked examples, and R code snippets. Use `\src{}` to cite where each fact comes from.
- Accuracy over volume: every formula and claim must match the course material (check the slides
  images when OCR is unclear). Where the course's wording/notation differs from ISLR, use the course's.
- Index generously with `\ix`/`\ixc` (every key term where it is explained).

## Compile check (required before you finish)
    cd "/home/user/PSTAT131-Notesheet"
    tools/check_fragment.sh sections/<your_file>.tex raw        # or: distilled
It compiles your fragment alone in a private temp dir and prints errors, overfull boxes, page count
and the number of index entries. Fix ALL errors. Fix overfull boxes wider than ~10pt (break long
`\texttt` / tables). You may view the PDF it reports (render a page with PyMuPDF:
`python3 -I -c "import fitz;d=fitz.open('<pdf>');d[0].get_pixmap(matrix=fitz.Matrix(1.3,1.3)).save('<png>')"`
and Read the PNG) to check layout. Delete your temp dirs (`work/tmp/chk.*` you created) when done.

## Final report (your last message)
Report: files written, page count from the check, number of index entries, anything you could
not read or were unsure about (with slide/page numbers), and any new canonical terms you introduced.
