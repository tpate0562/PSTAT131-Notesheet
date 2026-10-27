# Dedupe + no-proofs pass (read work/AGENT_GUIDE.md first for macros/conventions)

The user asked: "remove all duplicate information and all proofs". Decisions:
1. **Part I (distilled, `sections/d*.tex`) stays complete** except proofs/derivations are removed.
2. **Part II (raw, `sections/raw_*.tex`) is trimmed**: cut every slide / passage / code chunk /
   output block whose information is ALREADY in Part I. Keep only material Part I does not cover.
3. **Proofs removed everywhere**: delete derivation steps (algebra that shows *why* a formula holds:
   bias-variance decomposition algebra, least-squares / MLE derivations, LDA discriminant derivation
   "taking logs and dropping terms...", log-odds algebra, etc.). KEEP the final formula/result, its
   assumptions, its meaning, and worked numeric examples (plugging numbers in is not a proof).

## How to trim a raw fragment
- First read ALL of Part I: `sections/d1_concepts.tex d2_models.tex d2b_classification.tex
  d3_evaluation.tex d4_rcode.tex d5_exam.tex` (one agent is concurrently stripping proofs from them;
  that does not change which facts they contain).
- Go slide by slide / block by block. For each fact, number, definition, example, table, code line,
  output value or figure detail ask: "Is this already stated in Part I (same fact, any wording)?"
  - Entirely covered -> delete the whole slide (header included).
  - Partly covered -> keep the `\slide{..}{..}{title}` header and only the uncovered content.
  - Not covered -> keep verbatim (it is still a faithful transcription).
  - Pure title/divider/"Next..." slides carry no information -> delete.
  - `\fig{}` descriptions: keep only details (numbers, curve shapes, labels) not stated in Part I;
    shorten accordingly or delete.
  - Code/output: drop chunks whose code is already shown in Part I (e.g. d4_rcode templates, d3
    yardstick outputs); keep distinct code and output values not in Part I.
  - Exams/HW: Part I d5_exam has every PE and Sai question in condensed form. Keep in raw only what
    it lacks (e.g. full answer choices, exact wording that matters, grader comments not captured).
- Never paraphrase kept raw material into new wording; trimming only.
- At the very start of each `\section` in the raw file, add one line:
  `{\color{figgray}\itshape [Slides/parts already covered in Part I are omitted: S1.3--5, S1.9, ...]}`
  listing what you dropped entirely (ranges are fine).
- Keep the index macros on whatever remains (they must stay attached to the kept words). Don't add new
  index terms unless needed. Keep `\section`/`\subsection` structure; delete a subsection if empty.
- When in doubt whether something is covered, KEEP it (accuracy > brevity).

## Rules
- Edit ONLY the files named in your task. Scratch files go in `work/tmp/<your-task-name>/`.
- Compile-check each file: `mkdir -p work/tmp && tools/check_fragment.sh sections/<file>.tex raw`
  (or `distilled`). Fix all errors and overfull boxes > 10pt. Delete ONLY the `work/tmp/chk.XXXXXX`
  directories that YOUR runs printed (by exact name) — NEVER `rm -rf work/tmp/chk.*`, other agents
  run checks in parallel.
- Final report: per file, old vs new line count, slides/blocks dropped, proofs removed, anything you
  were unsure about.
