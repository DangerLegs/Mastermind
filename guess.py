class Guess: 
    def guess_1(self, player_1):
        self.guess = input(f"{player_1}'s turn. What is your guess? ")
        return self.guess

    def guess_2(self, player_2):
        self.guess = input(f"{player_2}'s turn. What is your guess? ")