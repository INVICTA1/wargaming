import unittest
from .task2 import tactical_number

class TacticalNumberTest(unittest.TestCase):

    def test_tactical_number(self):
        self.assertEqual(tactical_number((17, ['89', '5', '9', '584', '84', '6', '44', '89','75'])), 662)
        self.assertEqual(tactical_number((25, ['89', '6', '87', '84', '8454', '64', '78', '9','789'])), 2222)
        self.assertEqual(tactical_number((17500, ['10000', '10250', '15000', '15000', '7500', '7000', '8000', '9000','10000'])), 95)
        self.assertEqual(tactical_number((17, ['1', '2', '9578', '584', '824', '6313', '444', '859'])), 111111111111111111)
        self.assertEqual(tactical_number((17, ['89', '578', '9578', '584', '824', '6313', '444', '859'])), 1)
