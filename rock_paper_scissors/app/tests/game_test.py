import unittest
from app.models.game import Game
from app.models.player import Player

class TestGame(unittest.TestCase):
    def setUp(self):
        self.player_1 = Player("Player 1", "Rock")
        self.player_2 = Player("Player 2", "Paper")
        self.game = Game(self.player_1, self.player_2)

    def test_create_game( self ):
        game_moves = self.player_1.move + " vs. " + self.player_2.move
        self.assertEqual("Rock vs. Paper", game_moves)

    def test_game_draw( self):
        self.player_2 = Player("Player 2", "Rock")
        self.game = Game(self.player_1, self.player_2)
        self.assertEqual(None, self.game.play_game(self.player_1, self.player_2))
