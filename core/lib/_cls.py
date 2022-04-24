import os

def _cls():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")