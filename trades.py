#!/usr/bin/env python

import time

from mtgox import MTGox
import settings

mtgox = MTGox(user=settings.MTGOX_USER, password=settings.MTGOX_PASSWORD)
trades = mtgox.get_trades()

now = time.time()
for tr in trades:
    # also print tid
    print "%s \t@ %s (%s minutes ago)" % (tr["amount"], 
                                          tr["price"], 
                                          int((now - tr["date"])/60))

