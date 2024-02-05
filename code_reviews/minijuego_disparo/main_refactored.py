"""AyudaEnPython: https://www.facebook.com/groups/ayudapython
"""
from random import choice


class Entity:

    def __init__(self, name, lives):
        self.name = name
        self.lives = lives

    def _is_alive(self):
        return self.lives > 0

    def hit(self, other):
        other.lives -= 1

    def __str__(self):
        status = (
            f"has {self.lives} lives" if self._is_alive()
            else "has been killed"
        )
        return f"{self.name} {status}." 


class Monster(Entity):

    def __init__(self):
        super().__init__("Monster", 3)


class Alien(Entity):

    def __init__(self):
        super().__init__("Alien", 5)


def main():
    rounds = 5
    entities = [Monster(), Alien()]
    for _ in range(rounds):
        attacker = choice(entities)
        defender = entities[1 - entities.index(attacker)]
        attacker.hit(defender)
    for entity in entities:
        print(entity)


if __name__ == "__main__":
    main()
