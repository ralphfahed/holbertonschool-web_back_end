const readline = require('readline');

// Create interface to read input from stdin
const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout
});

// Prompt the user
rl.question('Welcome to Holberton School, what is your name?\n', (name) => {
  console.log(`Your name is: ${name}`);
});

// When the input ends (e.g. Ctrl+D or piping input)
rl.on('close', () => {
  console.log('This important software is now closing');
});
