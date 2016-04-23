# black scholes
# cheng.yan

from Engine import EngineBase
import numpy as np
import scipy.stats as ss

class BlackScholes(EngineBase):
    def __init__(self,**kwargs):
        super( 'EngineBase', self).__init__(kwargs)

    def _inputChecking(self,para = None):
        '''
        time to maturity
        spot price
        risk free rate
        volatility
        strike price
        '''
        names = ['Time',
                 'Spot Price',
                 'Strike Price',
                 'Volatility',
                 'Risk Free',
                 ]
        vars = para if para else self.vars
        if len(vars) != 5:
            raise Exception('Need 5 parameters to calculate. {} given'.format(len(vars)))

        missingPara = [ name for name in names if name not in vars ]

        if missingPara:
            raise Exception('Missing parameters {}'.format(','.join(missingPara)))

    def _d1(self):
        self._CACHE['d1'] = ( np.log(self.vars['Spot Price']/self.vars['Strike Price']) + (self.vars['Risk Free'] + self.vars['Volatility']**2/2) * self.vars['Time'] ) /(self.vars['Volatility']*np.sqrt(self.vars['Time']))

    def _d2(self):
        self._CACHE['d2'] = ( np.log(self.vars['Spot Price']/self.vars['Strike Price']) + (self.vars['Risk Free'] - self.vars['Volatility']**2/2) * self.vars['Time'] ) /(self.vars['Volatility']*np.sqrt(self.vars['Time']))

    def _updateParameters(self,**kwargs):
            self._inputChecking(kwargs)
            self.vars.update(kwargs)
            self._d1()
            self._d2()

    def pricing(self):
        cnd1 = ss.norm.csf( self._CACHE['_d1'] )
        cnd2 = ss.norm.csf( self._CACHE['_d2'] )
        pnd1 = ss.norm.csf( -1 * self._CACHE['_d1'] )
        pnd2 = ss.norm.csf( -1 * self._CACHE['_d2'] )
        self._CACHE['Call'] = self.vars['Spot Price'] * cnd1 - self.vars['Strike Price'] * np.exp( -1 * self.vars['Volatility'] * self.vars['Time']) *  cnd2
        self._CACHE['Put']  = self.vars['Strike Price'] * np.exp( -1 * self.vars['Volatility'] * self.vars['Time']) *  pnd2 - self.vars['Spot Price'] * cnd1









