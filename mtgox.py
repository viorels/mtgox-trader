
from httplib2 import Http
import simplejson as json
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
        self.actions = {"_get_ticker": ("GET", "/code/data/ticker.php"),
                        "get_depth": ("GET", "/code/data/getDepth.php"),
                        "get_trades": ("GET", "/code/data/getTrades.php"),
                        "get_balance": ("POST", "/code/getFunds.php"),
                        "buy_btc": ("POST", "/code/buyBTC.php"),
                        "sell_btc": ("POST", "/code/sellBTC.php"),
                        "_get_orders": ("POST", "/code/getOrders.php"),
                        "_cancel_order": ("POST", "/code/cancelOrder.php"),
                        "_withdraw": ("POST", "/code/withdraw.php")}
        
        for action, (method, _) in self.actions.items():
            def _handler(action=action, **args):
                return self._request(action, method=method, args=args)
            setattr(self, action, _handler)

    def get_ticker(self):
        return self._get_ticker()["ticker"]

    def get_orders(self):
        return self._get_orders()["orders"] # can also return balance

    def cancel_order(self, oid, typ=None):
        orders = self.get_orders()
        if typ is None:
            order = [o for o in orders if o["oid"] == oid]
            if order:
                typ = order[0]["type"]
            else:
                raise UserError("unknown order/type")
        return self._cancel_order(oid=oid, type=typ)


    def withdraw(self, amount, btca, group1="BTC"):
        return self._withdraw(amount=amount, btca=btca, group1=group1)["status"] # can also return balance

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
            if resp.status == 200:
                data = json.loads(content)
                if "error" in data:
                    raise UserError(data["error"])
                else:
                    return data 
            else:
                raise ServerError(content)
        except AttributeError, e: # 'NoneType' object has no attribute 'makefile'
            raise ServerError("timeout/refused")
        except ValueError, e:
            raise ServerError("%s: %s" % (e, content))

    def _url(self, action, scheme="http", args={}):
        url = urlunparse((scheme,
                          self.server,
                          self.actions[action][1], # path
                          '',
                          urlencode(args),
                          ''))
        return url

