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
        self.actions = {"ticker": "/code/data/ticker.php",
                        "depth": "/code/data/getDepth.php",
                        "trades": "/code/data/getTrades.php",
                        "balance": "/code/getFunds.php",
                        "buy": "/code/buyBTC.php",
                        "sell": "/code/sellBTC.php",
                        "get_orders": "/code/getOrders.php",
                        "cancel_order": "/code/cancelOrder.php",
                        "withdraw": "/code/withdraw.php"}
        
        simple_actions = ("ticker", "depth", "trades")
        for action in self.actions.keys():
            def _handler(action=action, **args):
                if action in simple_actions:
                    return self._request(action)
                else:
                    return self._request(action, method="POST", args=args)
            setattr(self, action, _handler)

    def _request(self, action, method="GET", args={}):
        query = args.copy()
        if method == "GET":
            url = self._url(action)
            data = None
        if method == "POST":
            url = self._url(action, scheme="https")
            query["name"] = self.user
            query["pass"] = self.password
            data = urlencode(query)

        h = httplib2.Http(cache=None)
        try:
            # TODO: timeout in a few seconds
            print "%s %s\n> %s" % (method, url, data)
            resp, content = h.request(url, method, data)
            print "< %s" % content
            content_json = simplejson.loads(content)
        except AttributeError, e: # 'NoneType' object has no attribute 'makefile'
            print "timeout/refused"
            return None
        except simplejson.decoder.JSONDecodeError, e:
            print "%s\n%s" % (e, content)
            return None
        return content_json

    def _url(self, action, scheme="http", args={}):
        url = urlunparse((scheme,
                          self.server,
                          self.actions[action],
                          '',
                          urlencode(args),
                          ''))
        return url

