from CY.Engine.BlackScholes import BlackScholes as BS
from CY.Engine.MonteCarlo import MonteCarlo as MC
from CY.Engine.BinomialTree import BinomialTree as BT

testUnderlying = {
                    'Time'           : 1/365.0,
                    'Spot Price'     : 20.0,
                    'Strike Price'   : 30.0,
                    'Volatility'     : 0.2076,
                    'Risk Free'      : 0.0014,
                    }

bsEngine = BS(**testUnderlying)
bsEngine.pricing()

mcEngine = MC(**testUnderlying)
mcEngine.pricing()

btEngine = BT(**testUnderlying)
btEngine.pricing()
