import sys

import os

INTERP = os.path.expanduser("/var/www/u0626703/data/flaskenv/bin/python")
if sys.executable != INTERP:
   os.execl(INTERP, INTERP, *sys.argv)

sys.path.append(os.getcwd())

from start import application