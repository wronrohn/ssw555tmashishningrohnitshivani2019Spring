import unittest
from main import Gedcom

class TestErrorLineNumber(unittest.TestCase):
    gedcom = Gedcom("GEDCOM_input.ged")
    gedcom.validate_all()
