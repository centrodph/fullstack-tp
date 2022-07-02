export const calculateScore = (questions, answers) => {
  let total = 0;
  let ok = 0;
  console.log(questions, answers);
  if (!questions || !questions.length) return "--";
  questions.forEach((q) => {
    if (answers[q.id]) {
      const op = q.options.find((o) => String(o.id) === String(answers[q.id]));
      if (op && op.correct) ok++;
      total++;
    }
  });
  return `${(ok * 100) / total}/100`;
};
