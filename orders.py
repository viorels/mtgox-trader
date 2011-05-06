#!/usr/bin/env python

import time

from mtgox import MTGox
import settings

mtgox = MTGox(user=settings.MTGOX_USER, password=settings.MTGOX_PASSWORD)
orders = mtgox.get_orders()

now = time.time()
for order in orders:
    order["type_text"] = {1: "sell", 2: "buy"}[order["type"]]
    order["status_text"] = {1: "active", 
                            2: "not enough funds"}[int(order["status"])]
    order["ago"] = int((now - int(order["date"]))/60)
    print ("%(oid)s %(type_text)s %(amount)s at %(price)s %(ago)s minutes ago, "
           "%(status_text)s" % order)

