#!/usr/bin/env python

import time

from mtgox import MTGox
import settings

mtgox = MTGox(user=settings.MTGOX_USER, password=settings.MTGOX_PASSWORD)

wait = 60

last_trades = {}
last_bids = []
last_asks = []

while True:
    trades = mtgox.get_trades()

    now = time.time()
    for tr in trades:
        if not last_trades.has_key(tr["tid"]):
            last_trades[tr["tid"]] = tr
            # also print tid
            print "%s: %s \t@ %s (%s minutes ago)" % (tr["tid"],
                                                      tr["amount"], 
                                                      tr["price"], 
                                                      int((now - tr["date"])/60))

    time.sleep(wait)
    continue

    depth = mtgox.get_depth()

    bids = sorted(depth['bids'], key=lambda bid: bid[0])
    asks = sorted(depth['asks'], key=lambda bid: bid[0])

    print "*** Bids"
    for price, amount in bids:
        print "%s\t%s" % (price, amount)

    print "\n*** Asks"
    for price, amount in asks:
        print "%s\t%s" % (price, amount)

    time.sleep(wait)

