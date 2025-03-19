"""AyudaEnPython: https://www.facebook.com/groups/ayudapython
"""
from enum import Enum


class Threshold(float, Enum):
    INFLUENCE = 70
    RATIO = 0.5
    INTERACTION = 50


def is_famous(followers: int, following: int, likes: int) -> bool:
    influence = (followers / (followers + following)) * 100
    ratio = following / followers
    interaction = (likes / followers) * 100
    if (
        influence > Threshold.INFLUENCE.value
        and ratio < Threshold.RATIO.value
        and interaction > Threshold.INTERACTION.value
    ):
        return "es"
    return "no es"


def main():
    print(f"Calculador de fama en TikTok\n{'='*28}\n")
    user = input("¿Cuál es el nombre de usuario en TikTok?\n> ")
    followers = int(input(f"¿Cuántos seguidores tiene '{user}'?\n> "))
    following = int(input(f"¿A cuántos(as) sigue '{user}'?\n> "))
    likes = int(input(f"¿Cuántos 'Me Gusta' tiene '{user}'?\n> "))
    state = is_famous(followers, following, likes)
    print("\nResultado:")
    print(f"'{user}' {state} famoso(a) en TikTok.")


if __name__ == "__main__":
    main()
