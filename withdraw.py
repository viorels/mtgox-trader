#!/usr/bin/env python

import sys

from settings import *

if len(sys.argv) == 3:
    _, amount, address = sys.argv
else:
    print "Usage: %s <amount> <BTC address>" % sys.argv[0]
    exit(1)

status = exchange.withdraw(group1="BTC", btca=address, amount=amount)
print status

