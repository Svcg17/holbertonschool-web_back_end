#!/usr/bin/env python3
"""API authentication
"""
from flask import request
from typing import List, TypeVar

class Auth():
    """Manages API authentication
    """
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """Returns true if a route requires authorization,
        false otherwise.
        """
        if not path or not excluded_paths:
            return True
        if path[-1] != '/':
            path = path + '/'
        if path in excluded_paths:
            return False
        
        return True
    
    def authorization_header(self, request=None) -> str:
        """
        """
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """
        """
        return None
