# Binomial Tree
# cheng.yan

from Engine import EngineBase

class BinomialTree(EngineBase):
    def __init__(self, kwargs):
        TIME_STEP = 100
        super(BinomialTree,self).__init__(**kwargs)
        self.dt = self.vars['Time'] / TIME_STEP

    def _updateParameters(self,**kwargs):
        super( BinomialTree, self)._inputChecking( **kwargs )
        self.vars.update(kwargs)

    def _getPrice(self,step):
        pass

    def pricing(self):
        pass





