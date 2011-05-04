
from httplib2 import Http
import simplejson as json
from simplejson.decoder import JSONDecodeError
from urlparse import urlunparse
from urllib import urlencode

class ServerError(Exception):
    def __init__(self, ret):
        self.ret = ret
    def __str__(self):
        return "Server error: %s" % self.ret

class UserError(Exception):
    def __init__(self, errmsg):
        self.errmsg = errmsg
    def __str__(self):
        return self.errmsg

class MTGox:
    """MTGox API"""
    def __init__(self, user, password):
        self.user = user
        self.password = password
        self.server = "mtgox.com"
        self.timeout = 10
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
        data = None
        headers = {}
        if method == "GET":
            url = self._url(action)
        if method == "POST":
            url = self._url(action, scheme="https")
            query["name"] = self.user
            query["pass"] = self.password
            data = urlencode(query)
            headers['Content-type'] = 'application/x-www-form-urlencoded'

        h = Http(cache=None, timeout=self.timeout)
        try:
            #print "%s %s\n> |%s|" % (method, url, data)
            resp, content = h.request(url, method, headers=headers, body=data)
            #print "< %s (%s)" % (content, resp)
            if resp["status"] == "200":
                data = json.loads(content)
                if "error" in data:
                    raise UserError(data["error"])
                else:
                    return data 
            else:
                raise ServerError(content)
        except AttributeError, e: # 'NoneType' object has no attribute 'makefile'
            raise ServerError("timeout/refused")
        except JSONDecodeError, e:
            raise ServerError("%s: %s" % (e, content))

    def _url(self, action, scheme="http", args={}):
        url = urlunparse((scheme,
                          self.server,
                          self.actions[action],
                          '',
                          urlencode(args),
                          ''))
        return url

