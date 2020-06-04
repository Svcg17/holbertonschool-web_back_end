#!/usr/bin/env python3
"""Auth module
"""
import bcrypt
from db import DB
from typing import TypeVar
import uuid


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

    def valid_login(self, email: str, password: str) -> bool:
        """Validate credentials
        """
        try:
            user = self._db.find_user_by(email=email)
            password = password.encode("utf-8")
            return (bcrypt.checkpw(password, user.hashed_password))
        except Exception:
            return False

    def create_session(self, email: str) -> str:
        """Creates a session ID based on a user
        """
        user = self._db.find_user_by(email=email)
        s_id = _generate_uuid()
        self._db.update_user(user.id, session_id=s_id)
        return s_id

    def get_user_from_session_id(self, session_id: str) -> str:
        """Returns a user based on its session_id
        """
        try:
            if not session_id:
                return None
            return self._db.find_user_by(session_id=session_id)
        except Exception:
            return None

    def destroy_session(self, user_id: int) -> None:
        """Updates the corresponding user id to None
        """
        try:
            self._db.update_user(user_id=user_id, session_id=None)
            return None
        except Exception:
            raise

    def get_reset_password_token(self, email: str) -> str:
        """Reset a users' password
        """
        try:
            user = self._db.find_user_by(email=email)
            s_id = _generate_uuid()
            self._db.update_user(user.id, reset_token=s_id)
            return s_id
        except Exception:
            raise ValueError

    def update_password(self, reset_token: str, password: str) -> None:
        """Uses a reset token to find the corresponding user and
        updates that user's password with a new one
        """
        try:
            user = self._db.find_user_by(reset_token=reset_token)
            password = _hash_password(password)
            self._db.update_user(user.id, hashed_password=password,
                                 reset_token=None)
            return None
        except Exception:
            raise ValueError


def _hash_password(password: str) -> str:
    """Returns a hashed password
    Args:
        password: password to hash
    Return:
        a hashed string
    """
    return bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt())

def _generate_uuid() -> str:
        """Returns a string representation of a new UUID.
        """
        return str(uuid.uuid1())
