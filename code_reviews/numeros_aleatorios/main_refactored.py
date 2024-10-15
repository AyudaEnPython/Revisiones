"""AyudaEnPython: https://www.facebook.com/groups/ayudapython
"""
from random import sample


def generate(n, min_=0, max_=48):
    return sample(range(min_, max_+1), n)


print(generate(5))
