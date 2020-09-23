import unittest
from .task1 import table_pifagor

class PifagorTesy(unittest.TestCase):

    def test_pifagor(self):
        self.assertEqual(table_pifagor('13 36'), 5)
        self.assertEqual(table_pifagor('15 225'), 1)
        self.assertEqual(table_pifagor('14 140'), 2)
        self.assertEqual(table_pifagor(' 36'), 5)
        self.assertEqual(table_pifagor('15 30'), 6)
        self.assertEqual(table_pifagor('15 120'), 4)
        self.assertEqual(table_pifagor('6 12'), 4)

