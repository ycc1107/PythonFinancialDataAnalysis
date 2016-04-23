from BlackScholes import BlackScholes as BS
from MonteCarlo import MonteCarlo as MC

testData = {
            'Time'           : 30,
            'Spot Price'     : 857.29,
            'Strike Price'   : 860,
            'Volatility'     : 0.2076,
            'Risk Free'      : 0.0014,
          }


bs = BS(testData)


bs.pricing()


print 'BlackScholes Call price {}'.format( bs.getPrice('Call') )
