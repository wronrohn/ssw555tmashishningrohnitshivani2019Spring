import unittest
from us07_an import us_07

class testcase(unittest.TestCase):

    def test_mbd(self):
        result=us_07(['1996-10-21',4],['2150-10-21',6],154,'I1')
        self.assertEqual(result,"Error US07:Age of person is 150 years with I1 id")

        result=us_07('NA',['1994-04-03',6],'NA','I1')
        self.assertEqual(result,"Warning US07:Birth date is not given in I1 id")

        result=us_07(['1994-06-12',4],'NA','NA','I1')
        self.assertEqual(result,0)

        result=us_07('NA','NA','NA','I1')
        self.assertEqual(result,"Warning US07:Birth date is not given in I1 id")

        result=us_07('NA','Invalid','Invalid','I1')
        self.assertEqual(result,"Warning US07:Birth date is not given and Death date is invalid in I1 id")

        result=us_07('Invalid','Invalid','Invalid','I1')
        self.assertEqual(result,"Warning US07:Birth date and Death date is invalid in I1 id")

        result=us_07(['1994-06-12',4],'Invalid','Invalid','I1')
        self.assertEqual(result,"Warning US07:Death date is invalid in I1 id")

        result=us_07(['1947-04-15',4],['1900-04-15',6],-47,'I1')
        self.assertEqual(result,"Error US07 in line 4:Birth date is after death date with I1 id")

if __name__=='__main__':
    unittest.main()