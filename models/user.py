#!/usr/bin/python3
"""
    Class User inherit from BaseModel
"""

from models.base_model import BaseModel


class User(BaseModel):
    """
        Class User

        ATTRIBUTS
        =============

            email: public, user's email

            first_name: public, first name of user

            last_name: public, last name of user

            password: public, password of user

            **kwargs: **kwargs of class BaseModel

    """

    email = ""
    first_name = ""
    last_name = ""
    password = ""
