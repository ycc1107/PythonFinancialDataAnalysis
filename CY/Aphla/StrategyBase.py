# Vol base
# cheng.yan

import logging
from CY.Engine import *
from CY.lib.Validation import Validation as VD

class StrategyBase:
    def __init__(self,pricingEngines = None, marketData = None):
        # positive is cash inflow
        self.SINGLE2AMOUNT = {
                'long open'     : -1,
                'short open'     :  1,
                'long cover'    :  1,
                'short cover'    : -1,
                }
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

    def _engineSetup(self):
        dummyFirstDataForEngineWarmUp = {
                    'Time'           : 1/365.0,
                    'Spot Price'     : 20.0,
                    'Strike Price'   : 30.0,
                    'Volatility'     : 0.2076,
                    'Risk Free'      : 0.0014,
                    }
        self.engines = [ engine(dummyFirstDataForEngineWarmUp) for engine in self.engines ]
        for data in self.marketData:
            [ engine.updateParameters(data) for engine in self.engines ]

    def singleGenerator(self, **kwargs):
         # the most important func
        # should return list of tuple
        # first element: single
        # second element: amount
        raise NotImplemented('Single Generator no implemented')

    def getPnl(self):
        singles = self.singleGenerator()
        pnlRes = [ self.SINGLE2AMOUNT[single[0]]*singles[1]*data for single, data in zip( singles, self.marketData) ]
        return sum(pnlRes)










