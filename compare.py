class Compare:
    def compare_num(self, guess, number):
        self.guessed = list(guess)
        self.numb = list(number)
        print(self.guessed, self.numb)
        response = ""
        for i in range(len(self.numb)):
            if self.guessed[i] == self.numb[i]:
                response += 'x '
            else:
                response += "O "
        return(response)
        if "O " not in response:
            print("YOU WIN!")
            quit()