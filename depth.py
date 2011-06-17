#!/usr/bin/env python

from settings import *

depth = exchange.get_depth()

bids = sorted(depth['bids'], key=lambda bid: bid[0])
asks = sorted(depth['asks'], key=lambda bid: bid[0])

print "*** Bids"
for price, amount in bids:
    print "%s\t%s" % (price, amount)

print "\n*** Asks"
for price, amount in asks:
    print "%s\t%s" % (price, amount)

