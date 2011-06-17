#!/usr/bin/env python

from settings import *

ticker = exchange.get_ticker()

if ticker:
    for key in ("last", "buy", "sell", "low", "high", "vol"):
        print "%s\t: %s" % (key, ticker[key])
else:
    print "failed, see logs"

