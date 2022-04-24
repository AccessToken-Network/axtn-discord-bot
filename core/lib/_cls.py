import os

from _sys import *

def _cls():
    if os.name == "nt":
        _sys("cls")
    else:
        _sys("clear")