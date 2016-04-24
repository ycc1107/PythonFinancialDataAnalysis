# Vol base
# cheng.yan

import logging
from CY.Engine import *
from CY.lib.Validation import Validation as VD

class StrategyBase:
    def __init__(self,pricingEngines = None, marketData = None):
        self.vd = VD()
        if pricingEngines == None:
            raise Exception('Strategy needs engine')
        if marketData == None:
            raise Exception('Strategy needs market data')
        logging.info('Attached {} engine(s) -- {} -- for Strategy {}'.format(len(pricingEngines),pricingEngines,self.__class__.__name__))
        self.vd.checker('Engine',pricingEngines)
        self.engines = [ eval(engine) for engine in pricingEngines]
        self.vd.checker('MaketData',marketData)
        self.marketData = marketData

    def singleGenerator(self):
        raise NotImplemented('Single Generator no implemented')

    def getPnl(self):
        pnlRes = {}
        for data in self.marketData:
            for engine in self.engines:





