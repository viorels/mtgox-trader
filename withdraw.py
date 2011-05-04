#!/usr/bin/env python

import sys

from mtgox import MTGox
import settings

if len(sys.argv) == 3:
    _, amount, address = sys.argv
else:
    print "Usage: %s <amount> <BTC address>" % sys.argv[0]
    exit(1)

mtgox = MTGox(user=settings.MTGOX_USER, password=settings.MTGOX_PASSWORD)
status = mtgox.withdraw(group1="BTC", btca=address, amount=amount)
print status

