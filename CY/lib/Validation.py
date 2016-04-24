# all validation function
# cheng.yan

import os
import pkgutil

class Validation:
    def _engineChecker(self,val):
        if val not in [ name for _, name, _ in pkgutil.iter_modules(['CY.Engine']) ]:
            raise Exception('No engine named {}'.format(val))

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