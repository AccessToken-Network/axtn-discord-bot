import datetime

from lib._colors import BColors

def timestamp():
	x = datetime.datetime.now()
	return x.strftime('{}[%d.%m.%y %H:%M:%S]'.format(BColors.CYAN))
