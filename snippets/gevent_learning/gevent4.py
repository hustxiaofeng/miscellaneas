from gevent.monkey import patch_all
patch_all()

import time

def compute(x, y):
    print "Compute %s + %s ..." % (x, y)
    time.sleep(1.0)
    return x + y

def print_sum(x, y):
    result = compute(x, y)
    print "%s + %s = %s" % (x, y, result)

print_sum(1, 2)