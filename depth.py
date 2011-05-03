#!/usr/bin/env python

import httplib2
import simplejson
import time

h = httplib2.Http(cache=None)
resp, content = h.request("http://mtgox.com/code/data/getDepth.php", "GET")
depth = simplejson.loads(content)

bids = sorted(depth['bids'], key=lambda bid: bid[0])
asks = sorted(depth['asks'], key=lambda bid: bid[0])

print "*** Bids"
for price, amount in bids:
    print "%s\t%s" % (price, amount)

print "\n*** Asks"
for price, amount in asks:
    print "%s\t%s" % (price, amount)

