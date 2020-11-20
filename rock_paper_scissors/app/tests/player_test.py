import unittest
from app.models.player import Player

class TestPlayer(unittest.TestCase):
    def setUp(self):
        self.player_1 = Player("Player 1", "Rock")

    def test_create_player( self ):
         self.assertEqual("Player 1", self.player_1.name)