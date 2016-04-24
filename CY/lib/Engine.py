# base Engine
# cheng.yan


class EngineBase(object):
    def __init__(self,**kwargs):
        self.vars = kwargs
        self._CACHE = {}
        self._updateParameters()

    def getPrice(self, name):
            return self._CACHE.get( name, None )

    def _inputChecking(self,**kwargs):
        '''
        time to maturity
        spot price
        risk free rate
        volatility
        strike price
        '''
        print self.__class__.__name__
        if self.__class__.__name__ in  ('BlackScholes','MonteCarlo'):
            names = ['Time',
                     'Spot Price',
                     'Strike Price',
                     'Volatility',
                     'Risk Free',
                     ]
            vars = kwargs if kwargs else self.vars
            if len(vars) != 5:
                raise Exception('Need 5 parameters to calculate. {} given'.format(len(vars)))

            missingPara = [ name for name in names if name not in vars ]

            if missingPara:
                raise Exception('Missing parameters {}'.format(','.join(missingPara)))

    def pricing(self):
        raise NotImplementedError('Not Implemented')

    def _updateParameters(self,**kwargs):
        raise NotImplementedError('Not Implemented')
