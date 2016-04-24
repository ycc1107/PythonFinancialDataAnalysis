from BlackScholes import BlackScholes as BS
from MonteCarlo import MonteCarlo as MC

testData = {
            'Time'           : 30/365.0,
            'Spot Price'     : 857.29,
            'Strike Price'   : 860,
            'Volatility'     : 0.2076,
            'Risk Free'      : 0.0014,
          }


bs = BS(**testData)
mc = MC(**testData)

bs.pricing()
print 'BlackScholes Call price {}'.format( bs.getPrice('Call') )
print 'BlackScholes Put price {}'.format( bs.getPrice('Put') )

mc.pricing()
print 'MonteCarlo Call price {}'.format( mc.getPrice('Call') )
print 'MonteCarlo Put price {}'.format( mc.getPrice('Put') )