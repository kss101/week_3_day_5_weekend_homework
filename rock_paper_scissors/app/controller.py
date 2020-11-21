from flask import render_template, request, redirect
from app import app
from app.models.game import Game
from app.models.player import Player
import random

@app.route('/')
def index():
    return render_template('index.html', title='Rock, Paper, Scissors')

@app.route('/<move1>/<move2>')
def play_a_game(move1, move2):
    player_1 = Player( "Player 1", move1 )
    player_2 = Player( "Player 2", move2 )
    game = Game( player_1, player_2 )
    winner = game.play_game( player_1, player_2 )
    return (render_template("winner.html", winner = winner, move1=move1, move2=move2))

@app.route('/welcome')
def welcome():
    return render_template('welcome.html', title='Rock, Paper, Scissors')

@app.route('/play')
def play():
    return render_template('play.html', title='Rock, Paper, Scissors')

@app.route('/select-move', methods=['POST'])
def select_move():
    player_1 = Player( "Player 1", request.form['move'] )
    player_2 = Player( "Computer", "")
    game = Game( player_1, player_2 )
    winner = game.play_game( player_1, player_2 )
    return (render_template("winner.html", winner=winner, move1=player_1.move, move2=player_2.move))



