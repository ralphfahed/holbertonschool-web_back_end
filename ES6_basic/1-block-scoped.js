export default function taskBlock(trueOrFalse) {
  var task = false;
  var task2 = true;

  if (trueOrFalse) {
    let task = true;   // block scoped
    let task2 = false; // block scoped
  }

  return [task, task2];
}

