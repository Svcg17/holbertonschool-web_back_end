#!/usr/bin/env python3
"""Auth module
"""
import bcrypt
from db import DB
from typing import TypeVar

class Auth:
    """Auth class to interact with the authentication database.
    """

    def __init__(self):
        self._db = DB()
    
    def register_user(self, email: str, password: str) -> TypeVar('User'):
        """Creates and saves a new user given an email and a password
        """
        try:
            self._db.find_user_by(email=email)
            raise ValueError("User {} already exists.".format(email))
        except ValueError:
            raise
        except Exception:
            pwd = _hash_password(password)
            user = self._db.add_user(email, pwd)
            return user


def _hash_password(password: str) -> str:
    """Returns a hashed password
    Args:
        password: password to hash
    Return:
        a hashed string
    """
    return bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt())