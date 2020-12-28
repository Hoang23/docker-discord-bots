import typing
import random

class Coin:

    def __init__(self, rigged=False):
        self.rigged = rigged


    def flip(self):
        rand = random.randint(1, 2)
        if rand == 1:
            return "Heads"
        elif rand == 2:
            return "Tails"


    def __repr__(self):
        return f'{type(self).__name__}(rigged={self.rigged})'   


# inherits from coin class - can use both flip method and rig method
class RiggedCoin(Coin):
    def __init__(self, rigged = True):
        super().__init__(rigged)


    def rig(self):
        if self.rigged == False:
            rand = random.randint(1, 2)
            if rand == 1:
                return "Heads"
            elif rand == 2:
                return "Tails"
        else:
            return "Heads"

    
    def changeStatus(self, status):
        status.lower()
        status.strip()
        if status == "james" or status == "rigged" or status == "rig":
            self.rigged = True
        elif status == "good" or status == "fair":
            self.rigged = False


    def __repr__(self):
        return f'{type(self).__name__}(rigged={self.rigged})'
