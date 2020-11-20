import unittest
from app.models.game import Game
from app.models.player import Player

class TestGame(unittest.TestCase):
    def setUp(self):
        self.player_1 = Player("Player 1", "rock")
        self.player_2 = Player("Player 2", "scissors")
        self.game = Game(self.player_1, self.player_2)

    def test_create_game( self ):
        game_moves = self.player_1.move + " vs. " + self.player_2.move
        self.assertEqual("rock vs. scissors", game_moves)

    def test_game_draw( self):
        self.player_2 = Player("Player 2", "rock")
        self.game = Game(self.player_1, self.player_2)
        self.assertEqual(None, self.game.play_game(self.player_1, self.player_2))

    def test_game_rock_beats_scissors( self ):
        self.game = Game(self.player_1, self.player_2)
        self.assertEqual("rock", self.player_1.move)
        self.assertEqual("scissors", self.player_2.move)
        self.assertEqual("Player 1", self.game.play_game(self.player_1, self.player_2))

    def test_game_scissors_beats_paper( self ):
        self.player_1 = Player("Player 1", "paper")
        self.game = Game(self.player_1, self.player_2)
        self.assertEqual("paper", self.player_1.move)
        self.assertEqual("scissors", self.player_2.move)
        self.assertEqual("Player 2", self.game.play_game(self.player_1, self.player_2))

    def test_game_paper_beats_rock( self ):
        self.player_1 = Player("Player 1", "paper")
        self.player_2 = Player("Player 2", "rock")
        self.game = Game(self.player_1, self.player_2)
        self.assertEqual("paper", self.player_1.move)
        self.assertEqual("rock", self.player_2.move)
        self.assertEqual("Player 1", self.game.play_game(self.player_1, self.player_2))
