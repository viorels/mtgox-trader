#!/usr/bin/env python

import httplib2
import simplejson

h = httplib2.Http(cache=None)
try:
    resp, content = h.request("http://mtgox.com/code/data/ticker.php", "GET")
except AttributeError, e: # 'NoneType' object has no attribute 'makefile'
    print "timeout/refused"
    exit(1)

try:
    ticker = simplejson.loads(content)
except simplejson.decoder.JSONDecodeError, e:
    print "%s\n%s" % (e, content)
    exit(2)

if resp["status"] == '200':
    keys = ("last", "buy", "sell", "low", "high", "vol")
    for key in keys:
        print "%s\t: %s" % (key, ticker["ticker"][key])
else:
    print "Unexpected response: %s\n%s" % (resp, content)

