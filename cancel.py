#!/usr/bin/env python

import sys

from mtgox import MTGox
import settings

if len(sys.argv) == 2:
    oid = sys.argv[1]
else:
    print "Usage: %s <order id>" % sys.argv[0]
    exit(1)

mtgox = MTGox(user=settings.MTGOX_USER, password=settings.MTGOX_PASSWORD)
status = mtgox.cancel_order(oid=oid)
print status

