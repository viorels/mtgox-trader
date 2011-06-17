#!/usr/bin/env python

import time

from settings import *

trades = exchange.get_trades()

now = time.time()
for tr in trades:
    # also print tid
    print "%s \t@ %s (%s minutes ago)" % (tr["amount"], 
                                          tr["price"], 
                                          int((now - tr["date"])/60))

