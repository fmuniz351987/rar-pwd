#! /usr/bin/python3

from itertools import product

max_combinations = int(input())

words = []
while True:
    try:
        words.append(input())
    except EOFError:
        break
for r in range(1, max_combinations):
    for password in product(words, repeat=r):
        print(''.join(password))

