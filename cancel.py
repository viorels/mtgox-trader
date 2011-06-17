#!/usr/bin/env python

import sys

from settings import * 

if len(sys.argv) == 2:
    oid = sys.argv[1]
else:
    print "Usage: %s <order id>" % sys.argv[0]
    exit(1)

status = exchange.cancel_order(oid=oid)
print status

