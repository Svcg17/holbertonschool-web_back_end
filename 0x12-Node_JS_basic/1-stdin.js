// Gets input from user and writes it to stdout
process.stdin.setEncoding('utf-8');

process.stdout.write('Welcome to Holberton School, what is your name?\n');
process.stdin.on('readable', () => {
  const name = process.stdin.read();
  console.log(name)
  if (name) process.stdout.write(`Your name is: ${name}\r`);
});
// if stdout process in stream comes from the terminal, end process
if (process.stdout.isTTY) {
  process.stdin.on('end', () => {
    process.stdout.write('This important software is now closing\n');
  });
}
