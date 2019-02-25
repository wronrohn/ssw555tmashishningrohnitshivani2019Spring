import unittest
import datetime
from us35_sp import us35_ppl_born_last_30days_check

class TestProject(unittest.TestCase):
    """
    List all people in a GEDCOM file who were born in the last 30 days
    """
    def test_us35_ppl_born_last_30days_check(self):
        # Assure that the dates are in properformat
        # template : us35_ppl_born_last_30days_check(birth_date,present_date)
       
        present_date = datetime.datetime.now()
        # if the birth date is NA/ present date is NA / both are NA it must be false
        self.assertFalse(us35_ppl_born_last_30days_check("NA",present_date))
        self.assertFalse(us35_ppl_born_last_30days_check("2019-02-22","NA"))
        self.assertFalse(us35_ppl_born_last_30days_check("NA","NA"))

        # If birth date is after present date
        self.assertFalse(us35_ppl_born_last_30days_check("2020-02-22",present_date))

         # if birth date is before more than 30 days in the past from current date
        self.assertFalse(us35_ppl_born_last_30days_check("2018-04-13",present_date))

        # If the birth date is within 30 days from current date, it should be true
        self.assertTrue(us35_ppl_born_last_30days_check("2019-02-22",present_date))

       
        


if __name__ == '__main__':
    unittest.main()
