import random

class Game():

    def __init__(self, player_1, player_2):
        self.player_1 = player_1
        self.player_2 = player_2

    def play_game( self, player_1, player_2 ):
        if self.player_2.name == "Computer" and self.player_2.move == "":
            self.player_2.move = self.play_against_computer()
           # print("Computer's move is: ", self.player_2.move)

        if( self.player_1.move == self.player_2.move):
            # print("It's a draw!")
            return
        elif(( self.player_1.move == "rock" and self.player_2.move =="paper" ) or ( self.player_1.move == "paper" and self.player_2.move =="rock" )):
            # print("paper wins")
            result = "paper"
        
        elif(( self.player_1.move == "scissors" and self.player_2.move =="paper" ) or ( self.player_1.move == "paper" and self.player_2.move =="scissors" )):
            # print("scissors wins")
            result= "scissors"

        else:
            # print("rock wins")
            result= "rock"

        if result == self.player_1.move:
            #print("Winner is: ", player_1.name)
            return player_1.name
        else:
            #print("Winner is: ", player_2.name)
            return player_2.name

    def play_against_computer( self ):
        computer_move = random.randint( 1, 3 )
        if computer_move == 1:
            move = 'rock'
        elif computer_move == 2:
            move = 'paper'
        else:
            move = 'scissors'
        return move
        