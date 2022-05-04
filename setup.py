import json

from os import system
from core.lib._colors import BColors

_sys_py3 = lambda str_path : system("python3 {}".format(str_path))

def _modules():
    _sys_py3("core/lib/modules.py")

def _bot():
    _sys_py3("core/core.py")

def _quickstart_check():
    import json
    try:
        config_file = open('core/lib/_config.json')
        config = json.load(config_file)
        if config['quickstart']:
            print("AXTN: Quickstart Active")
            _bot()
        elif not config['quickstart']:
            print("AXTN: Quicktstart not Active")
            _modules()
    except:
        print("Something went wrong!")
        
if __name__=="__main__":
    try:
        _quickstart_check()
        _modules()
    except KeyboardInterrupt:
        print(BColors.YELLOW + "\nProgram closed by user (CTRL+C)")
        exit()