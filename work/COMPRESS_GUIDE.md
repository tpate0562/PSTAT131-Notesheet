# Compression pass for Part II (raw) — read work/AGENT_GUIDE.md first for macros/conventions

User request: "remove any unnecessary sentences / compress the text down while retaining information
for all the raw data". Part II has already been trimmed to what Part I does not cover
(see work/DEDUPE_GUIDE.md); now make what remains as short as possible WITHOUT losing information.

## Do
- Delete sentences that carry no information: pleasantries, motivation/filler ("I understand that not
  all students...", "Let's take a look", "As you can see", "Now we will..."), restatements of the
  previous sentence, transitions, instructions about the RStudio UI that are not exam-relevant,
  Rmd header/knitr boilerplate notes, link-only lines with no content, empty "[untitled]" slides.
- Compress wordy prose into terse notes/fragments: "We can see that the median price is higher for
  ideal cuts" -> "Median price higher for Ideal cut." Merge short bullets; use symbols (->, =, <, >).
- Compress `\fig{}` descriptions to the information they carry: numbers, axes, what trend/shape,
  which class/colour is which. Drop visual decoration ("hand-drawn", "colourful", "photo of ...")
  unless it is the content. A figure that only illustrates text already stated -> delete it.
- Code/output: keep code lines and output values that carry information; drop repeated/boilerplate
  lines (e.g. `library()` calls already shown elsewhere in your file, `head()` of a table already
  printed, tibble header lines like `# A tibble: 6 x 4` can stay short). Long outputs: keep the
  informative rows/columns, mark elisions with `# ...`.
- Keep the `\slide{}{}{}` / `\subsection` structure only where it helps navigation; merge tiny
  consecutive slides on the same topic under one header if that saves space (keep slide numbers,
  e.g. `\slide{1}{30--32}{...}`).
- Keep the grey "[... omitted: ...]" note at the top of each section, but shorten it.

## Do NOT
- Do not drop any fact, number, definition, answer choice, rubric item, code line with distinct
  behaviour, or output value that is not stated elsewhere in your file or in Part I.
- Do not change numbers, code semantics, or the meaning of answer choices/prompts. Exam question
  wording (answer choices, prompts) may be compressed but must stay unambiguous.
- Do not remove index macros that are attached to kept content; when you delete text, its index
  macros go with it; when you rewrite a sentence, keep the \ix/\ixh/\ixc of the terms still present.
- Do not edit files other than those named in your task. Scratch: work/tmp/<task-name>/.

## Check
`mkdir -p work/tmp && tools/check_fragment.sh sections/<file>.tex raw` — fix all errors and
overfull boxes > 10pt. Delete ONLY the chk.XXXXXX dirs your runs printed (never `rm -rf work/tmp/chk.*`).
Final report: per file old -> new line count and check page count, and anything uncertain.
