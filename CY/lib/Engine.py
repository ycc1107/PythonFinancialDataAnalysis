# base Engine
# cheng.yan


class EngineBase:
    def __inti__(self,**kwargs):
        self.vars = kwargs
        self._CACHE = {}
        self._updateParameters()

    def getPrice(self, name):
            return self._CACHE.get( name, None )
    def _inputChecking(self):
        raise NotImplementedError('Not Implemented')

    def pricing(self):
        raise NotImplementedError('Not Implemented')

    def _updateParameters(self,**kwargs):
        raise NotImplementedError('Not Implemented')
