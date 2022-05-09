import unittest
from src.card import Card
from src.card_game import CardGame

class TestCardGame(unittest.TestCase):
    
    def test_check_for_ace(self):
        self.card1 = Card("spades", 1)
        self.assertEqual(True, self.card_game.check_for_ace(self.card1))

    def test_