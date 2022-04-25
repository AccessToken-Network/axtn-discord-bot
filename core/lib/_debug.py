import json

from lib._colors import BColors
from lib.config import Config
from lib._timestamp import timestamp

#Print Debug Function in Lambda
_print_debug = lambda debug_string:\
	[print("{}{}[DEBUG] {}".format(timestamp(), BColors.CYAN, debug_string))
	 if Config.CONFIG_OBJECT['debug'] else print("", end="")]