import unittest
from us02_sp.py import us02_birth_is_before_marriage

class TestProject(unittest.TestCase):
    """
    Birth should occur before marriage of an individual
    """
    def test_us02_birth_is_before_marriage(self):
        # Assure that the dates are in properformat
        # template :  us02_birth_is_before_marriage(birth_date,marriage_date)

        # if any of the two dates are "NA"
        self.assertTrue(us02_birth_is_before_marriage("NA","1985-03-02"))
        self.assertTrue(us02_birth_is_before_marriage("1985-03-02","NA"))

        # if both the dates are "NA"
        self.assertTrue(us02_birth_is_before_marriage("NA","NA"))

        # if birth date  is before the marriage date, it is true
        self.assertTrue(us02_birth_is_before_marriage("1978-11-24","1990-12-18"))

        # if birth date  is after the marriage date, it is false
        self.assertFalse(us02_birth_is_before_marriage("2019-04-13","2000-06-15"))
        


if __name__ == '__main__':
    unittest.main()
