#!/usr/bin/env python3
"""Filter logger task #1"""
from typing import List
import re
import logging
import sys


class RedactingFormatter(logging.Formatter):
    """A RedactingFormatter Class
    Args:
        fields: fields in messageto replace with redaction
    """
    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: List[str]):
        super(RedactingFormatter, self).__init__(self.FORMAT)
        self.fields = fields

    def format(self, record: logging.LogRecord) -> str:
        record.msg = filter_datum(self.fields, self.REDACTION,
                                  record.getMessage(), self.SEPARATOR)
        formatter = logging.Formatter(self.FORMAT)
        return formatter.format(record)


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
