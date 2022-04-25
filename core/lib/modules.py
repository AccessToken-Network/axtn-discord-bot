_sys = lambda sys_str : os.system(sys_str)

def _osn(sys_str):
    if  os.name == "nt":
        _sys(sys_str)
    else:
        _sys("python3 -m ".format(sys_str))

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
            _osn("pip install discord.py")
            _osn("pip install python-dotenv")
            
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