"""Pydantic models"""

from pydantic import BaseModel

class UserCreate(BaseModel):
    """Class representing user"""
    username: str
    password: str

class Token(BaseModel):
    """Class representing token"""
    access_token: str
    token_type: str
