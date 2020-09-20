import unittest
from .task2 import search_big_number

class PifagorTesy(unittest.TestCase):

    def test_pifagor(self):
        self.assertEqual(search_big_number(6,'9,13,16,91,321,456,2489,16972,99999'),321321 )
