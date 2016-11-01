"""The heart and soul of the interactive fiction engine: description."""

from enum import Enum
from typing import Callable

class DescType(Enum):

    """
    The different types of description.

    long_: if something is described for the first time
    short: if you've seen something often enough that you don't really notice it
        anymore, except for changes, or stuff that catches the eye
    far: something is far away
    examine: look closely, examine can involve touching and have side effects
    """

    long_ = 1
    short = 2
    far = 3
    examine = 4

_description = {}

def add_desc(identity: str, type_: DescType, desc_func: Callable) -> None:
    """Register description callable."""
    if identity not in _description:
        _description[identity] = {}
    if type_ in _description[identity]:
        # TODO: warn - overwriting callable
        pass
    _description[identity][type_] = desc_func
