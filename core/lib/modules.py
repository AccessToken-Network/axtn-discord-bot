_sys = lambda sys_str : os.system(sys_str)

def _osn(sys_str):
    if  os.name == "nt":
        _sys(sys_str)
    else:
        _sys(sys_str)

try:
    import os
    from time import sleep
except ModuleNotFoundError:
    print('Python3 missing default modules!')

def _modules():
    try:
        import dotenv
        import discord
        from time import sleep
        from dotenv import load_dotenv
        from discord.utils import get
        from discord.utils import get
        from dotenv import load_dotenv
        from discord.ext import commands
        from discord.utils import get
    except ModuleNotFoundError:
        try:
            if 