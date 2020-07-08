// import { start } from "repl";
// returns a string of all the set values that start with a specific string (startString).
export default function cleanSet(set, startString) {
  let string = '';
  if (startString !== '') {
    set.forEach((val) => {
      if (val.includes(startString)) string = string.concat(`-${val.split(startString)[1]}`);
    });
    string = string.substring(1);
  }
  return string;
}

/* console.log(cleanSet(new Set(['bonjovi', 'bonaparte', 'bonappetit', 'banana']), 'bon'));
console.log(cleanSet(new Set(['bonjovi', 'bonaparte', 'bonappetit', 'banana']), '')); */
