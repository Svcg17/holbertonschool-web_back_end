# 0x12. NodeJS Basics

## Learning Objectives
   - run javascript using NodeJS
   - use NodeJS modules
   - use specific Node JS module to read files
   - use process to access command line arguments and the environment
   - create a small HTTP server using Node JS
   - create a small HTTP server using Express JS
   - create advanced routes with Express JS
   - use ES6 with Node JS with Babel-node
   - use Nodemon to develop faster


## Tasks
### [0. Executing basic javascript with Node JS ](./0-console.js)
n the file 0-console.js, create a function named displayMessage that prints in STDOUT the string argument.
```
bob@dylan:~$ cat 0-main.js
const displayMessage = require('./0-console');

displayMessage("Hello NodeJS!");

bob@dylan:~$ node 0-main.js
Hello NodeJS!
bob@dylan:~$
```

### [1. Using Process stdin ](./1-stdin.js)
Create a program named 1-stdin.js that will be executed through command line:

   - It should display the message Welcome to Holberton School, what is your name? (followed by a new line)
   - The user should be able to input their name on a new line
   - The program should display Your name is: INPUT
   - When the user ends the program, it should display This important software is now closing (followed by a new line)

Requirements:

   - Your code will be tested through a child process, make sure you have everything you need for that
```
bob@dylan:~$ node 1-stdin.js 
Welcome to Holberton School, what is your name?
Bob
Your name is: Bob
bob@dylan:~$ 
bob@dylan:~$ echo "John" | node 1-stdin.js 
Welcome to Holberton School, what is your name?
Your name is: John
This important software is now closing
bob@dylan:~$ 
```

### [2. Reading a file synchronously with Node JS ](./2-read_file.js)
Using the database database.csv (provided in project description), create a function countStudents in the file 2-read_file.js

   - Create a function named countStudents. It should accept a path in argument
   - The script should attempt to read the database file synchronously
   - If the database is not available, it should throw an error with the text Cannot load the database
   - If the database is available, it should log the following message to the console Number of students: NUMBER_OF_STUDENTS
   - It should log the number of students in each field, and the list with the following format: Number of students in FIELD: 6. List: LIST_OF_FIRSTNAMES
```
bob@dylan:~$ cat 2-main_0.js
const countStudents = require('./2-read_file');

countStudents("nope.csv");

bob@dylan:~$ node 2-main_0.js
2-read_file.js:9
    throw new Error('Cannot read the database file');
    ^

Error: Cannot read the database file
...
bob@dylan:~$
bob@dylan:~$ cat 2-main_1.js
const countStudents = require('./2-read_file');

countStudents("database.csv");

bob@dylan:~$ node 2-main_1.js
Number of students: 10
Number of students in CS: 6. List: Johann, Arielle, Jonathan, Emmanuel, Guillaume, Katie
Number of students in SWE: 4. List: Guillaume, Joseph, Paul, Tommy
bob@dylan:~$ 
```

### [3. Reading a file asynchronously with Node JS ](./3-read_file_async.js)


Using the database database.csv (provided in project description), create a function countStudents in the file 3-read_file_async.js

   - Create a function named countStudents. It should accept a path in argument (same as in 2-read_file.js)
   - The script should attempt to read the database file asynchronously
   - The function should return a Promise
   - If the database is not available, it should throw an error with the text Cannot load the database
   - If the database is available, it should log the following message to the console Number of students: NUMBER_OF_STUDENTS
   - It should log the number of students in each field, and the list with the following format: Number of students in FIELD: 6. List: LIST_OF_FIRSTNAMES
```
bob@dylan:~$ cat 3-main_0.js
const countStudents = require('./3-read_file_async');

countStudents("nope.csv")
    .then(() => {
        console.log("Done!");
    })
        .catch((error) => {
        console.log(error);
    });

bob@dylan:~$ node 3-main_0.js
Error: Cannot load the database
...
bob@dylan:~$
bob@dylan:~$ cat 3-main_1.js
const countStudents = require('./3-read_file_async');

countStudents("database.csv")
    .then(() => {
        console.log("Done!");
    })
        .catch((error) => {
        console.log(error);
    });
console.log("After!");

bob@dylan:~$ node 3-main_1.js
After!
Number of students: 10
Number of students in CS: 6. List: Johann, Arielle, Jonathan, Emmanuel, Guillaume, Katie
Number of students in SWE: 4. List: Guillaume, Joseph, Paul, Tommy
Done!
bob@dylan:~$ 
```

### [4. Create a small HTTP server using Node's HTTP module ](./4-http.js)
In a file named 4-http.js, create a small HTTP server using the http module:

   - It should be assigned to the variable app and this one must be exported
   - HTTP server should listen on port 1245
   - Displays Hello Holberton School! in the page body for any endpoint as plain text

In terminal 1:
```
bob@dylan:~$ node 4-http.js
...
```

In terminal 2:
```
bob@dylan:~$ curl localhost:1245 && echo ""
Hello Holberton School!
bob@dylan:~$ 
bob@dylan:~$ curl localhost:1245/any_endpoint && echo ""
Hello Holberton School!
bob@dylan:~$ 
```