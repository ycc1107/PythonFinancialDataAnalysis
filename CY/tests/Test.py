import unittest
from CY.lib.BlackScholes import BlackScholes as BS
from CY.lib.MonteCarlo import MonteCarlo as MC


class EngineUnitTest(unittest.TestCase):
    def setUp(self):
        self.tol = 1e-10
        self.testUnderlying = {
                    'Time'           : 1/365.0,
                    'Spot Price'     : 20.0,
                    'Strike Price'   : 30.0,
                    'Volatility'     : 0.2076,
                    'Risk Free'      : 0.0014,
                    }
        self.bsEngine = BS(**self.testUnderlying)
        self.mcEngine = MC(**self.testUnderlying)
        self.bsEngine.pricing()
        self.mcEngine.pricing()

    def test_BlackScholesEngine_call(self):
        callPrice = self.bsEngine.getPrice('Call')
        val = callPrice - self.tol
        self.assertLessEqual( val , 0)

    def test_BlackScholesEngine_put(self):
        putPrice  = self.bsEngine.getPrice('Put')
        self.assertGreaterEqual( putPrice , 0)

    def test_MonteCarloEngine_call(self):
        callPrice = self.mcEngine.getPrice('Call')
        val = callPrice - self.tol
        self.assertLessEqual( val , 0)

    def test_MonteCarloEngine_put(self):
        putPrice  = self.mcEngine.getPrice('Put')
        self.assertGreaterEqual( putPrice , 0)


if __name__ == '__main__':
    unittest.main()