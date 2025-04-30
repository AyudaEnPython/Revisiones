"""AyudaEnPython: https://www.facebook.com/groups/ayudapython
"""
from prototools import int_input, menu_input

data = [
    ("Astarion", 239, "Rogue", "Elf", 3, True),
    ("Shadowheart", 40, "Cleric", "Half-Elf", 5, True),
    ("Wyll", 25, "Warlock", "Human", 2, False),
    ("Gale", 35, "Wizard", "Human", 5, True),
    ("Karlach", 32, "Barbarian", "Tiefling", 6, False),
    ("Lae'zel", 20, "Fighter", "Githyanki", 4, True),
    ("Jaheira", 150, "Druid", "Half-Elf", 6, False),
    ("Halsin", 350, "Druid", "Elf", 7, False),
    ("Minsc", 130, "Ranger", "Human", 5, False),
    ("Minthara", 250, "Paladin", "Drow", 8, False),
    ("Dark Urge", 30, "Sorcerer", "Dragonborn", 1, False),
]


def max_level(data, class_=None):
    _d = sorted(data, key=lambda x: x[-2], reverse=True)
    if not class_:
        return _d[0][0]
    for n, _, k, *_ in _d:
        if class_ == k:
            return n


def increment(data, name):
    for i, (n, *before, lvl, w) in enumerate(data):
        if name == n:
            data[i] = (n, *before, lvl+1, w)
            return


def verify(data, race):
    return race in [r for _, _, _, r, *_ in data]


def _find_character(data):
    character = menu_input(
        [n for n, *_ in data], prompt="Ingresar nombre: \n", numbers=True,
    )
    for n, age, *_ in data:
        if n == character:
            return n, age


def guess_game(name, age):
    while True:
        user_guess = int_input("Edad: ", gt=0)
        if user_guess == age:
            print(f"Exacto! {name} tiene {age}")
            return
        print(f"{name} es {'menor' if user_guess > age else 'mayor'}")


def main():
    print(f"Nivel promedio: {sum(lvl for (*_, lvl, _) in data) // len(data)}")
    print(f"Jugadores: {', '.join(n for n, *_, w in data if w)}")
    print(f"Clases: {', '.join(set(k for _, _, k, *_ in data))}")
    print(
        {k:[k for _, _, _, k, *_ in data].count(k) for _, _, _, k, *_ in data }
    )
    print(f"Human: {verify(data, 'Human')}")
    print(f"Gnome: {verify(data, 'Gnome')}")
    print(f"Máximo nivel: {max_level(data)}")
    print(f"Máximo nivel (Druid): {max_level(data, 'Druid')}")
    increment(data, "Gale")
    guess_game(*_find_character(data))


if __name__ == "__main__":
    main()
