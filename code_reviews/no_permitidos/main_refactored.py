"""AyudaEnPython: https://www.facebook.com/groups/ayudapython
"""
NOT_ALLOWED = "!\"#$%&\\\'()*+,-./:;<=>?@[]^_`{|}~©®°¦±¼½¾"


def sol(s):
    return "".join(c for c in s if c not in NOT_ALLOWED)


def main():
    entrada = input("Entrada: ")
    print(sol(entrada))


if __name__ == "__main__":
    main()
