# all validation function
# cheng.yan
# Des: all validation related function/class

import os
import pkgutil

class Validation:
    def _engineChecker(self,val):
        allEngineName = [ name for _, name, _ in pkgutil.iter_modules(['CY.Engine']) ]
        if any( [ True for v in val if v not in allEngineName ] ):
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



def ParametersChecker(*types):
    ''' This decorator for function parameters type check'''
    def wrapper(func):
        assert len(types) == func.func_code.co_argcount
        def newFunc(*args,**kwargs):
            for arg, t in zip(args,types):
                assert isinstance(arg,t), 'Type %s is not match %s'%(args, t)
            return func(*arg, **kwargs)
        newFunc.func_name = func.func_name
        return newFunc
    return wrapper