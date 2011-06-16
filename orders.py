#!/usr/bin/env python

import time

from settings import *

orders = exchange.get_orders()

now = time.time()
for order in orders:
    order["type_text"] = {1: "sell", 2: "buy", "Sell": "sell", "Buy": "buy"}[order["type"]]
    if "status" in order:
       order["status_text"] = {1: "active", 
                               2: "not enough funds"}[int(order["status"])]
    else:
       order["status_text"] = "active"
    order["ago"] = int((now - int(order["date"]))/60)
    print ("%(oid)s %(type_text)s %(amount)s at %(price)s %(ago)s minutes ago, "
           "%(status_text)s" % order)


