from os import system


def _sys_py3(str_path):
    return lambda a: system("python3 {}".format(str_path))

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
            _bot()
        elif not config['quickstart']
            _modules()
    
        

if __name__ == "__main__":
    _quickstart_check()
    _modules()