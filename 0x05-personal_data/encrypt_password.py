#!/usr/bin/env python3
"""Encrypting Passwords"""
import bcrypt


def hash_password(password: str) -> str:
    """returns a salted, hashed password,
    which is a byte string"""
    hashed = bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt())
    return hashed
