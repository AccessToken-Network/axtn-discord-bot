import datetime

from ._colors import BColors
from ._config import Config

#Print Debug Function in Lambda

_print_debug = lambda debug_string:\
	[print("{}{}[DEBUG] {}".format(timestamp(), BColors.CYAN, debug_string))
	 if Config.CONFIG_OBJECT['debug'] else print("", end="")]