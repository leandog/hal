import hal
import sys

if sys.version_info < (3, 0):
    reload(sys)
    sys.setdefaultencoding('utf8')
else:
    raw_input = input

h = hal.Hal()
if h.connect():
    h.process(threaded=False)
