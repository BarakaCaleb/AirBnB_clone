#!/usr/bin/python3
"""Defines a State class."""
from models.base_model import BaseModel


class State(BaseModel):
    """Represent the state.

    Attributes:
        name (str): name of the state.
    """

    name = ""
