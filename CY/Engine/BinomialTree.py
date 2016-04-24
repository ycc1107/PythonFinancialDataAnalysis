# Binomial Tree
# cheng.yan

from Engine import EngineBase
import math

class BinomialTree(EngineBase):
    def __init__(self, **kwargs):
        super(BinomialTree,self).__init__(**kwargs)
        self.TIME_STEP = 100
        self.dt = self.vars['Time'] / self.TIME_STEP
        self.discountFactor =  math.exp(self.vars['Risk Free'] * self.dt * -1)

    def updateParameters(self, **kwargs):
        super( BinomialTree, self)._inputChecking( **kwargs )
        self.vars.update(kwargs)
        self._CACHE['updateMarker'] = True


    def pricing(self):
        if self._CACHE['updateMarker']:
            s = [0 for _ in xrange(self.TIME_STEP)]
            temp1 = math.exp( (self.vars['Risk Free'] + self.vars['Volatility'] ** 2) * self.dt)
            temp2 = (self.discountFactor + temp1) * 0.5
            up =  temp2 + (temp2**2 - 1)**0.5
            down  = 1.0/up
            probability = ( math.exp(self.vars['Risk Free']*self.dt)-down ) / (up - down)
            s[0] = self.vars['Spot Price']
            for i in xrange(self.TIME_STEP):
                for j in xrange(i,0,-1):
                    s[j] =  up*s[j-1]
                s[0]= down*s[0]

            vCall = [ max(s[i] - self.vars['Strike Price'] , 0 ) for i in xrange(self.TIME_STEP)]
            vPut = [ max( self.vars['Strike Price'] - s[i] , 0 ) for i in xrange(self.TIME_STEP)]
            for i in xrange(self.TIME_STEP -1,0,-1):
                for j in xrange(i):
                    vCall[j] = (probability*vCall[j-1] + (1+probability)*vCall[j]) * self.discountFactor
                    vPut[j] = (probability*vPut[j-1] + (1+probability)*vPut[j]) * self.discountFactor

            self._CACHE['Call'] = vCall[0]
            self._CACHE['Put'] = vPut[0]
            self._CACHE['updateMarker'] = False








