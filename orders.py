#!/usr/bin/env python

from mtgox import MTGox
import settings

mtgox = MTGox(user=settings.MTGOX_USER, password=settings.MTGOX_PASSWORD)
orders = mtgox.get_orders()
print orders

