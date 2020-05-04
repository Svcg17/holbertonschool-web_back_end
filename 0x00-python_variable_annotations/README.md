# 0x00. Python Variable Annotations

## Learning Objectives
  -  Type annotations in Python 3
  -  How you can use type annotations to specify function signatures and variable types
  -  Duck typing
  -  How to validate your code with mypy

## Requirements
 -   Allowed editors: vi, vim, emacs
 -   All your files will be interpreted/compiled on Ubuntu 18.04 LTS using python3 (version 3.7)
 -   All your files should end with a new line
 -   The first line of all your files should be exactly #!/usr/bin/env python3
 -   A README.md file, at the root of the folder of the project, is mandatory
 -   Your code should use the pycodestyle style (version 2.5.)
 -   All your files must be executable
 -   The length of your files will be tested using wc
 -   All your modules should have a documentation (python3 -c 'print(__import__("my_module").__doc__)')
 -   All your classes should have a documentation (python3 -c 'print(__import__("my_module").MyClass.__doc__)')
 -   All your functions (inside and outside a class) should have a documentation (python3 -c 'print(__import__("my_module").my_function.__doc__)' and python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)')

## Tasks

### [0. Basic annotations - add](./0-add.py)
Write a type-annotated function add that takes a float a and a float b as arguments and returns their sum as a float.
```
user:~/holbertonschool-web_back_end/0x00-python_variable_annotations$ cat 0-main.py
#!/usr/bin/env python3
add = __import__('0-add').add

print(add(1.11, 2.22) == 1.11 + 2.22)
print(add.__annotations__)

user:~/holbertonschool-web_back_end/0x00-python_variable_annotations$ ./0-main.py
True
{'a':  <class 'float'>, 'b': <class 'float'>, 'return': <class 'float'>}
```


