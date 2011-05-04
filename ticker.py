#!/usr/bin/env python

from mtgox import MTGox
import settings

mtgox = MTGox(user=settings.MTGOX_USER, password=settings.MTGOX_PASSWORD)
ticker = mtgox.get_ticker()

if ticker:
    for key in ("last", "buy", "sell", "low", "high", "vol"):
        print "%s\t: %s" % (key, ticker[key])
else:
    print "failed, see logs"

