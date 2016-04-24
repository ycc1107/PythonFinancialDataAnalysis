# all validation function
# cheng.yan

import os
class Validation:
    def _engineChecker(self,val):
        pass
    def _pathChecker(self,val):
        if not isinstance(val,str):
            raise Exception('Path need to be string')
        if not os.path.exists(val):
            raise Exception('Path not exists')

    def _marketDataChecker(self,val):
        pass

    def checker(self,name,val):
        CHECKABLE_NAMES = {'Engine'     : '_engineChecker',
                          'MarketData'  : '_marketDataChecker',
                           'Path'       : '_marketDataChecker',}
        if not name or not val:
            raise Exception('Validation needs name and value')
        if name not in CHECKABLE_NAMES:
            raise NotImplemented( 'Validation can not check {}'.format(name) )

        getattr( self, CHECKABLE_NAMES[ name ])( val )