# Owner: Cheng.Yan cheng.yan@nyu.edu
# Des: store market data

class MarketDataBase():
    def __init__(self):
        pass

    def getAllData(self):
        raise NotImplementedError()

    def getAllDataRange(self):
        raise NotImplementedError()

    def getVolData(self):
        raise NotImplementedError()

    def getVolRange(self):
        raise NotImplementedError()

    def getOrderBook(self):
        raise NotImplementedError()


class ChinaMarketData(MarketDataBase):
     def getAllData(self):
        raise NotImplementedError()

    def getAllDataRange(self):
        raise NotImplementedError()

    def getVolData(self):
        raise NotImplementedError()

    def getVolRange(self):
        raise NotImplementedError()

    def getOrderBook(self):
        raise NotImplementedError()
