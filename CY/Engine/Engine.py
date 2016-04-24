# base Engine
# cheng.yan


class EngineBase(object):
    def __init__(self,**kwargs):
        self.vars = kwargs
        self._inputChecking(**kwargs)
        self._findPriceFunc()
        self._CACHE = {}
        self._CACHE['updateMarker'] = True

    def _findPriceFunc(self):
        optionFunc = { 'Volatility': 'getVol', 'Risk Free': 'getRiskFree', }
        if self.targetPara[0] in optionFunc:
            getattr( self, optionFunc[ self.targetPara[0] ] )()

    def _inputChecking(self,**kwargs):
        '''
        time to maturity
        spot price
        risk free rate
        volatility
        strike price
        '''
        if self.__class__.__name__ in  ('BlackScholes','MonteCarlo','BinomialTree'):
            names = ['Time',
                     'Spot Price',
                     'Strike Price',
                     'Volatility',
                     'Risk Free',
                     'Price'
                     ]
            vars = kwargs if kwargs else self.vars

            if len(vars) != 5:
                raise Exception('Need 5 parameters to calculate. {} given'.format(len(vars)))

            self.targetPara = [ name for name in names if name not in vars ]

            if len( self.targetPara ) > 1:
                raise Exception('Missing too many parameters {}'.format(self.targetPara))

            if any([ True for para in self.targetPara if para not in ['Volatility', 'Risk Free','Price']]):
                raise Exception('Missing critical parameter {}'.format(self.targetPara))

    def updateParameters(self, **kwargs):
            raise NotImplementedError('Not Implemented')

    def getPrice(self, name):
        self.pricing()
        return self._CACHE.get( name, None )

    def pricing(self):
        raise NotImplementedError('Not Implemented')

    def getGreek(self):
        pass

    def getVol(self):
        pass

    def getRiskFree(self):
        pass
