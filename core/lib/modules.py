#needs a complete revamp

import sys
_sys = lambda sys_str : os.system(sys_str)
from _colors import BColors

def _osn(sys_str):
    if  os.name == "nt":
        _sys(sys_str)
    else:
        _sys("python3 -m {}".format(sys_str))

try:
    import os
    from time import sleep
except ModuleNotFoundError as e:
    print(f'Python3 missing default modules! \n {e}')

def _modules():
    try:
        import os
        import re
        import sys
        import uuid
        import socket
        import psutil
        import dotenv
        import random
        import discord
        import asyncio
        import platform
        import importlib
        import sysconfig
        from time import sleep
        from dotenv import load_dotenv
        from discord.utils import get
        from discord.utils import get
        from dotenv import load_dotenv
        from discord.ext import commands
        from discord.utils import get
    except ModuleNotFoundError:
        try:
            _osn("pip install discord.py")
            _osn("pip install python-dotenv")
            
            import os
            import re
            import sys
            import uuid
            import socket
            import psutil
            import dotenv
            import random
            import discord
            import asyncio
            import platform
            import importlib
            import sysconfig
            from time import sleep
            from dotenv import load_dotenv
            from discord.utils import get
            from discord.utils import get
            from dotenv import load_dotenv
            from discord.ext import commands
            from discord.utils import get
        except ModuleNotFoundError:
            str_input = input("Want to try again? [y/n]")
            if str_input == "y" or str_input == "Y":
                modules()
            else:
                pass

try:
    _modules()
    print("Modules: Initialized")
    
except KeyboardInterrupt:
    print(BColors.YELLOW + "\nProgram closed by user (CTRL+C)")
    exit()
    