#!/usr/bin/env python

#
#  Copy to settings.py, enter credentials for the 
#  exchange(s) you would like to connect to and uncomment
#  the corresponding exchange line.
#

from api import ExchB, MTGox

EXCHB_USER = 'your_username'
EXCHB_PASSWORD = 'your_password'

MTGOX_USER = 'your_username'
MTGOX_PASSWORD = 'your_password'

# uncomment the exchange you want to use
#exchange = ExchB(user=EXCHB_USER, password=EXCHB_PASSWORD)
exchange = MTGox(user=MTGOX_USER, password=MTGOX_PASSWORD)
