#!/usr/bin/env python

import sys

from settings import *

if len(sys.argv) in (2, 3):
    amount = sys.argv[1]
    ask = sys.argv[2] if len(sys.argv) == 3 else None
else:
    print "Usage: %s <amount> [ask]" % sys.argv[0]
    exit(1)

status = exchange.sell_btc(amount=amount, price=ask)
print status

