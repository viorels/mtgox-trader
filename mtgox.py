import httplib2
import simplejson
from urlparse import urlunparse
from urllib import urlencode

class MTGox:
    """MTGox API"""
    def __init__(self, user, password):
        self.user = user
        self.password = password
        self.server = "mtgox.com"
        self.functions = {"ticker": "/code/data/ticker.php",
                          "depth": "/code/data/getDepth.php",
                          "trades": "/code/data/getTrades.php",
                          "balance": "/code/getFunds.php",
                          "buy": "/code/buyBTC.php",
                          "sell": "/code/sellBTC.php",
                          "get_orders": "/code/getOrders.php",
                          "cancel_order": "/code/cancelOrder.php",
                          "withdraw": "/code/withdraw.php"}
        
        simple_funcs = ("ticker", "depth", "trades")
        for func in self.functions.keys():
            if func in simple_funcs:
                setattr(self, func, lambda func=func: self._get(func))
            else:
                setattr(self, func, lambda **args: self._post(func, args))

    def _get(self, func):
        h = httplib2.Http(cache=None)
        try:
            # TODO: timeout in a few seconds
            resp, content = h.request(self._url(func), "GET")
            content_json = simplejson.loads(content)
        except AttributeError, e: # 'NoneType' object has no attribute 'makefile'
            print "timeout/refused"
            return None
        except simplejson.decoder.JSONDecodeError, e:
            print "%s\n%s" % (e, content)
            return None
        return content_json

    def _post(self, func, **args):
        pass

    def _url(self, func, args={}, auth=False):
        scheme = 'http'
        query = args.copy()
        if auth:
            scheme = 'https'
            query["name"] = self.user
            query["pass"] = self.password
        querys = urlencode(query)
        url = urlunparse((scheme, self.server, self.functions[func], '', querys, ''))
        return url

