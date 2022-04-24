from os import system

def _sys_py3(str_path):
    return lambda a: system("python3 {}".format(str_path))

def _modules():
    _sys_py3("core/lib/modules.py")

def _bot():
    _sys_py3("core/core.py")

if __name__ == "__main__":
    _modules()
    _bot()