#!/usr/bin/env python3
"""Filter logger task #1"""
from typing import List
import re


def filter_datum(fields: List[str],
                 redaction: str,
                 message: str,
                 separator: str) -> str:
    """Uses a regex to replace ocurrences of certain field
    values match everything after field plus = until separator
    """
    for field in fields:
        pattern = field + "=.+?(?=abc)*\\" + ";"
        message = re.sub(pattern, field + "=" + redaction + separator, message)
    return message

message = "name=Balou;email=balou@holberton.io;ssn=412-532-2382;password=abcdef;"
print(filter_datum(fields=("email", "password"), redaction="***", message=message, separator=";"))
