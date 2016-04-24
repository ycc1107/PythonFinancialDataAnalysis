import unittest
from CY.lib.Validation import Validation


class ValidationUnitTest(unittest.TestCase):
    def setUp(self):
        self.vd = Validation()
        self.intPath = 1234
        self.nonExsitPath = r'c:\\1234'
        self.nonSupportEngineName = 'TestEngine'

    def test_path_nonString(self):
        expectedVal = 'Path need to be string'
        try:
            self.vd.checker('Path',self.intPath)
        except Exception,e:
            self.assertEqual(e,expectedVal)

    def test_path_nonExists(self):
        expectedVal = 'Path not exists'
        try:
            self.vd.checker('Path',self.nonExsitPath)
        except Exception,e:
            self.assertEqual(e,expectedVal)

    def test_engine_notSupport(self):
        expectedVal = 'No engine named TestEngine'
        try:
            self.vd.checker('Engine',self.nonSupportEngineName)
        except Exception,e:
            self.assertEqual(e[0],expectedVal)



if __name__ == '__main__':
    unittest.main()