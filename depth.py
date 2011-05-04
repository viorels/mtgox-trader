#!/usr/bin/env python

from mtgox import MTGox
import settings

mtgox = MTGox(user=settings.MTGOX_USER, password=settings.MTGOX_PASSWORD)
depth = mtgox.get_depth()

bids = sorted(depth['bids'], key=lambda bid: bid[0])
asks = sorted(depth['asks'], key=lambda bid: bid[0])

print "*** Bids"
for price, amount in bids:
    print "%s\t%s" % (price, amount)

print "\n*** Asks"
for price, amount in asks:
    print "%s\t%s" % (price, amount)

