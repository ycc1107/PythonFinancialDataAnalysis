# black scholes
# cheng.yan

from Engine import EngineBase
import numpy as np
import scipy.stats as ss


class BlackScholes(EngineBase):
    def __init__(self,**kwargs):
        super( BlackScholes, self).__init__(**kwargs)

    def _d1(self):
        self._CACHE['d1'] = ( np.log(self.vars['Spot Price']/self.vars['Strike Price']) + (self.vars['Risk Free'] + self.vars['Volatility']**2/2) * self.vars['Time'] ) /(self.vars['Volatility']*np.sqrt(self.vars['Time']))

    def _d2(self):
        self._CACHE['d2'] = ( np.log(self.vars['Spot Price']/self.vars['Strike Price']) + (self.vars['Risk Free'] - self.vars['Volatility']**2/2) * self.vars['Time'] ) /(self.vars['Volatility']*np.sqrt(self.vars['Time']))

    def _updateParameters(self,**kwargs):
            self._inputChecking(**kwargs)
            self.vars.update(kwargs)
            self._d1()
            self._d2()

    def pricing(self):
        cnd1 = ss.norm.cdf( self._CACHE['d1'] )
        cnd2 = ss.norm.cdf( self._CACHE['d2'] )
        pnd1 = ss.norm.cdf( -1 * self._CACHE['d1'] )
        pnd2 = ss.norm.cdf( -1 * self._CACHE['d2'] )
        self._CACHE['Call'] = self.vars['Spot Price'] * cnd1 - self.vars['Strike Price'] * np.exp( -1 * self.vars['Volatility'] * self.vars['Time']) *  cnd2
        self._CACHE['Put']  = self.vars['Strike Price'] * np.exp( -1 * self.vars['Volatility'] * self.vars['Time']) *  pnd2 - self.vars['Spot Price'] * pnd1









