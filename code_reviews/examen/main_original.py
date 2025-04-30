"""AyudaEnPython: https://www.facebook.com/groups/ayudapython
"""
personajes_principales = [
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

def calcular_nivel_medio(personajes):
    suma = 0
    contador = 0
    for personaje in personajes:
        if personaje[5]:
            suma += personaje[4]
            contador += 1
    media = suma // contador
    return media

def filtrar_equipo(personajes):
    equipo = []
    for personaje in personajes:
        if personaje[5]:
            equipo.append(personaje)
    return equipo

def obtener_clases(personajes):
    clases = set()
    for personaje in personajes:
        clases.add(personaje[2])
    return clases

def contar_razas(personajes):
    conteo_razas = {}
    for personaje in personajes:
        raza = personaje[3]
        if raza in conteo_razas:
            conteo_razas[raza] += 1
        else:
            conteo_razas[raza] = 1
    return conteo_razas

def verificar_existencia_raza(personajes, raza):
    for personaje in personajes:
        if personaje[3] == raza:
            return True
    return False

def personaje_mayor_nivel(personajes, clase=None):
    nombre = None
    maximo = 0
    for personaje in personajes:
        if clase == None or personaje[2] == clase:
            if personaje[4] > maximo:
                nombre = personaje[0]
                maximo = personaje[4]
    return nombre

def incrementar_nivel(personajes, nombre):
    for i in range(len(personajes)):
        if personajes[i][0] == nombre:
            personajes[i] = (personajes[i][0],
                             personajes[i][1],
                             personajes[i][2],
                             personajes[i][3],
                             personajes[i][4] + 1,
                             personajes[i][5])

def encontrarPersonajesConEdad(personajes):
    nombre = input("Introduzca el nombre:")

    for personaje in personajes:
        if personaje[0] == nombre:
            real = personaje[1]
            break

    jugando = True

    while(jugando):
        edad = int(input("Introduzca una edad:"))

        if edad == 0:
            print("Interrupción por el jugador")

        if real < edad:
            print(nombre, "es menor")
        elif real > edad:
            print(nombre, "es mayor")
        else:
            print("Exacto", nombre, "tiene", edad)
            jugando = False

print(calcular_nivel_medio(personajes_principales))
print(filtrar_equipo(personajes_principales))
print(obtener_clases(personajes_principales))
print(contar_razas(personajes_principales))
print(verificar_existencia_raza(personajes_principales, "Human"))
print(verificar_existencia_raza(personajes_principales, "Gnome"))
print(personaje_mayor_nivel(personajes_principales))
print(personaje_mayor_nivel(personajes_principales, "Druid"))
print(personajes_principales)
incrementar_nivel(personajes_principales, "Gale")
print(personajes_principales)
encontrarPersonajesConEdad(personajes_principales)
