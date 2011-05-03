#!/usr/bin/env python

import httplib2
import simplejson
import time

h = httplib2.Http(cache=None)
resp, content = h.request("http://mtgox.com/code/data/getTrades.php", "GET")
trades = simplejson.loads(content)

now = time.time()
for tr in trades:
    # also print tid
    print "%s \t@ %s (%s minutes ago)" % (tr["amount"], 
                                          tr["price"], 
                                          int((now - tr["date"])/60))

