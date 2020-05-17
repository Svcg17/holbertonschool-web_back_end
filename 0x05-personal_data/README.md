# 0x05. Personal data

## Learning Objectives
   - Examples of Personally Identifiable Information (PII)
   - How to implement a log filter that will obfuscate PII fields
   - How to encrypt a password and check the validity of an input password
   - How to authenticate to a database using environment variables

## Tasks
### [0. Regex-ing](./filtered_logger.py)
Write a function called filter_datum taking three required arguments: a list of strings fields, a string redaction a string message and a string separator, and returning a string.

The function should use a regex to replace ocurrences of certain field values.

For example:
```
>>> message = "name=Balou;email=balou@holberton.io;ssn=412-532-2382;password=abcdef;"
>>> filter_datum(fields=("email", "password"), redaction="***", message=message, separator=";")
"name=Balou;email=***;ssn=412-532-2382;password=***;"
```
filter_datum should be less than 5 lines long and use re.sub to perform the substitution with a single regex.

