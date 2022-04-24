import os

from _sys import _sys

def _cls():
    if os.name == "nt":
        _sys("cls")
    else:
        _sys("clear")