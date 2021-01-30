class Draw:
    def __init__(self):
        self.player_1('')
        self.player_2('')

    def draw_player_1(self, guess, response):
        self.player_1 += (f"{guess}, {response}")
        print(self.player_1)
        
    def draw_player_2(self, guess, response):
        self.player_2 += (f"{guess}, {response}")
        print(self.player_2)