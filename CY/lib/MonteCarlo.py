# Monte Carlo
# cheng.yan

from Engine import EngineBase
import numpy as np
from random import gauss

class MonteCarlo( EngineBase ):
    def __init__(self,**kwargs):
        super( 'EngineBase', self).__init__(kwargs)

    def _updateParameters(self,**kwargs):
            self._inputChecking(kwargs)
            self.vars.update(kwargs)

    def pricing(self):
        N = 1000.0
        sfunc = '''self.vars['Spot Price'] * np.exp(( self.vars['Risk Free'] - 0.5 * self.vars['Volatility'] **2) * self.vars['Time'] +
                 self.vars['Volatility'] * np.sqrt(self.vars['Time']) * gauss(0,1.0))'''
        priceLambda = lambda x: ( max(0.0,self.vars['Strike Price'] - x ), max(0.0, x - self.vars['Strike Price'] ) )
        priceUpdate = [ priceLambda( eval (sfunc) ) for _ in xrange(N) ]
        self._CACHE['Call'] = sum( price[0] for price in priceUpdate ) / N
        self._CACHE['Put'] = sum( price[1] for price in priceUpdate ) / N
