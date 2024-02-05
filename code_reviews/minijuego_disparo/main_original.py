"""AyudaEnPython: https://www.facebook.com/groups/ayudapython
"""
class Enemy:
    name=""
    lives=0
    def __init__(self, name, lives):
        self.name = name
        self.lives = lives
    
    def hit(self):
        self.lives -= 1
        if self.lives <= 0:
            print(self.name + 'killed')
        else:
            print(self.name + 'has'+str(self.lives) + 'lives')

class Monster:
    def __init__(self):
        super().__init__('Monster', 3)

class Alien:
    def __init__(self) -> None:
        super().__init__('Alien', 5)

m = Monster()
a = Alien()

while True:
    x = input()
    if x == 'exit':
        break