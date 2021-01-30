import random
from compare import Compare
from number import Number
from guess import Guess
from draw import Draw
from player import Player

draw_1 = Draw.draw_player_1()
draw_2 = Draw.draw_player_2()
player = Player()
guess = Guess()
comp = Compare()
numb = Number()
number = numb.get_number()
player = player.get_name()

class Director:
	
	def __init__(self):
	
		self.still_playing = True
	
	def start_game(self):

		while still_playing: 
            
            guess_1 = guess.guess_1(player[0])
                                
            comparison = comp.compare_num(guess_1, number)	      

            draw_1(guess_1, comparison) 

            guess_2 = guess.guess_2(player[1])

            comparison = comp.compare_num(guess_2, number)

            draw_2(guess_2, comparison)

director = Director()
director.start_game()

