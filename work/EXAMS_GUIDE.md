# Full worked exams (read work/AGENT_GUIDE.md first for macros/conventions)

The user wants, on the sheet, every exam question IN FULL plus a full worked answer:
the correct answer, WHY it is right, and for multiple choice WHY EACH WRONG OPTION IS WRONG.

Sources:
- Full original transcription (all question text, every answer choice, official PE solutions, Sai's
  answers, grader marks/rubrics): `work/tmp/exams/raw_exams_full_original.tex`. Verify against the page
  images when anything is unclear: practice exam `work/render/practice/pNNN.png`, official solutions
  `work/render/practice_sol/pNNN.png`, Sai's graded midterm `work/render/sai/pNNN.png`.
- Condensed answers already written: `sections/d5_exam.tex` (6.1 and 6.2) and the original
  `work/tmp/exams/d5_original.tex` — use for cross-checking, but verify every answer yourself.
- Course notes for justification: `sections/d1_concepts.tex d2_models.tex d2b_classification.tex
  d3_evaluation.tex d4_rcode.tex`. Explanations must match course material/notation; cite with \src{}.

Format for each question (inside `\begin{qbox}{PE Q7 (k pts)}` ... `\end{qbox}`):
1. Full question stem (compressed only where wording is filler; every number, variable, code line kept).
2. All answer choices, labelled, one per line or inline (A) ... (B) ... when short.
3. `\ans` the correct answer (official key for PE; grader's key for Sai).
4. Why it is right: 1-3 terse sentences.
5. Why each other option is wrong: one short line per wrong option ("(A) wrong: ...").
   For free-response/code questions: the full model answer (for code-bug questions list every bug and
   its fix; for multi-part questions answer every part).
6. Sai file only: Sai's answer, points, and the grader's comment/rubric line; where Sai lost points,
   say exactly what was missing. Use they/them for Sai if a pronoun is needed.
If the official key looks wrong or ambiguous, say so in a grey note and explain; never silently disagree.

Writing style: terse, exam-sheet density, no filler. Index densely (\ix, \ixh, \ixc) with the canonical
vocabulary; refer to the figure atlas where helpful with \fref{N} (e.g. ROC questions -> \fref{24}).

Rules: edit ONLY your own file. Scratch in work/tmp/<task-name>/. Compile check:
`tools/check_fragment.sh sections/<file>.tex distilled` (fix all errors and overfull boxes > 10pt;
\fref/\pageref warnings about undefined labels are expected in the standalone check). Delete only the
chk.XXXXXX dirs your runs printed. Final report: question count covered, any key you disagree with,
anything unreadable.
