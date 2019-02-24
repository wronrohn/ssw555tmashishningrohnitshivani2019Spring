import unittest
from us04_an import us_04

class testcase(unittest.TestCase):

    def test_mbd(self):
        result=us_04(['1994-06-12',4],['1994-04-03',6],'F1')
        self.assertEqual(result,"Error US04 in line 6:Marriage date occurs after Divorce date in F1 family")

        result=us_04('NA',['1994-04-03',6],'F1')
        self.assertEqual(result,"Warning US04:Marriage date is not given in F1 family")

        result=us_04(['1994-06-12',4],'NA','F1')
        self.assertEqual(result,0)

        result=us_04('NA','NA','F1')
        self.assertEqual(result,"Warning US04:Marriage date is not given in F1 family")

        result=us_04('NA','Invalid','F1')
        self.assertEqual(result,"Warning US04:Marriage date is not given and Divorce date is invalid in F1 family")

        result=us_04('Invalid','Invalid','F1')
        self.assertEqual(result,"Warning US04:Marriage date and Divorce date is invalid in F1 family")

        result=us_04(['1994-06-12',4],'Invalid','F1')
        self.assertEqual(result,"WarningUS04:Divorce date is invalid in F1 family")

        result=us_04(['1977-12-06',4],['1980-12-08',6],'F2')
        self.assertEqual(result,0)

if __name__=='__main__':
    unittest.main()