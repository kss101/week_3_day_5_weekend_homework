class Game():

    def __init__(self, player_1, player_2):
        self.player_1 = player_1
        self.player_2 = player_2

    def play_game( self, player_1, player_2 ):
        if( self.player_1.move == self.player_2.move):
            # print("It's a draw")
            return