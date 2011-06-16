#!/usr/bin/env python

import sys

from settings import * 

if len(sys.argv) == 3:
    oid = sys.argv[1]
    otype = sys.argv[2]
else:
    print """Usage: %s [orderid] [type]    (type: 1 for sell, 2 for buy)

Set type to anything for ExchangeBitcoins.com""" % sys.argv[0]
    exit(1)

status = exchange._cancel_order(oid=oid, type=otype)
print status

