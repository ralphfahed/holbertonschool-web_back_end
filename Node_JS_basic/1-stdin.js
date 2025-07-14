process.stdout.write("Welcome to Holberton School, what is your name?\n");

process.stdin.on("data", (data) => {
  const name = data.toString().trim();
  console.log(`Your name is: ${name}`);
});

// When user ends input (Ctrl+D or piped input), trigger this
process.stdin.on("end", () => {
  console.log("This important software is now closing");
});
