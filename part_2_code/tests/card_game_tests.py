import unittest
from src.card import Card
from src.card_game import CardGame

class TestCardGame(unittest.TestCase):
    
    def test_check_for_ace_true(self):
        card1 = Card("spade", 1)
        check_for_ace(card1)
        self.assertEqual()