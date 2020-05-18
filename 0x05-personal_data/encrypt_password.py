#!/usr/bin/env python3
"""Encrypting Passwords"""
import bcrypt


def hash_password(pwd: str) -> bytes:
    """returns a salted, hashed password,
    which is a byte string"""
    hashed = bcrypt.hashpw(pwd.encode("utf-8"), bcrypt.gensalt())
    return hashed
