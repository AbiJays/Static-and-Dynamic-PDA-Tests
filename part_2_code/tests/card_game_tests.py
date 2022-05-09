import unittest
from src.card import Card
from src.card_game import CardGame

class TestCardGame(unittest.TestCase):
    
    def test_check_for_ace(self):
        self.card_game = CardGame()
        self.card1 = Card("Spades", 1)
        self.assertEqual(True, self.card_game.check_for_ace(self.card1))

