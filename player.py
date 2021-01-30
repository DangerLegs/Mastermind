class Player:
    def __init__(self):
        self._name = []

    def get_name(self):
        for n in range(2):
            name = input(f"Enter a name for player {n + 1}: ")
            if name not in self._name:
                self._name.append(name)
        return(self._name)

