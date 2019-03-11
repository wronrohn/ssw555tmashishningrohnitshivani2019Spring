import unittest
from us_rs import us_rs 
from main import Gedcom
from us04_an import parse_data_04

class TestCase(unittest.TestCase):
    
    
    gedcom = Gedcom("GEDCOM_input.ged")
    fam = gedcom.storeFam()
    ind = gedcom.storeInd()

    
    
    def test_checkLineNumber(self):
        
        self.assertFalse(us_rs.siblingCount(self.fam))

if __name__ == "__main__":
    unittest.main()