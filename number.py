import random

class Number:
    def __init__(self):
        self.number = random.randint(1000,9999)
        self.numb = str(self.number)

    def get_number(self):
        return self.numb