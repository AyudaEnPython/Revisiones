"""AyudaEnPython: https://www.facebook.com/groups/ayudapython
"""

print(f"Calculador de fama en TikTok\n{'='*28}\n")
user = input("¿Cuál es el nombre de usuario en TikTok?\n> ")
followers = int(input(f"¿Cuántos seguidores tiene '{user}'?\n> "))
following = int(input(f"¿A cuántos(as) sigue '{user}'?\n> "))
likes = int(input(f"¿Cuántos 'Me Gusta' tiene '{user}'?\n> "))

influence = (followers / (followers + following)) * 100
ratio = following / followers
interaction = (likes / followers) * 100

if influence > 70 and ratio < 0.5 and interaction > 50:
    state = "es"
else:
    state = "no es"

print("\nResultado:")
print(f"'{user}' {state} famoso(a) en TikTok.")
