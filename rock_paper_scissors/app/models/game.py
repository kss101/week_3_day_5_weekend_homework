class Game():

    def __init__(self, player_1, player_2):
        self.player_1 = player_1
        self.player_2 = player_2

    def play_game( self, player_1, player_2 ):
        if( self.player_1.move == self.player_2.move):
            print("It's a draw!")
            return
        elif(( self.player_1.move == "rock" and self.player_2.move =="paper" ) or ( self.player_1.move == "paper" and self.player_2.move =="rock" )):
            print("paper wins")
            result = "paper"
        
        elif(( self.player_1.move == "scissors" and self.player_2.move =="paper" ) or ( self.player_1.move == "paper" and self.player_2.move =="scissors" )):
            print("scissors wins")
            result= "scissors"

        else:
            print("rock wins")
            result= "rock"

        if result == self.player_1.move:
            return player_1.name
        else:
            return player_2.name