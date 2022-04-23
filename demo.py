import random
import sys


def Move(value):


    snake_squares = {16: 4, 22: 10, 33: 20, 48: 24, 62: 56, 78: 69, 74: 60, 91: 42, 97: 6}
    ladder_squares = {3: 12, 7: 23, 11: 25, 21: 56, 47: 53, 60: 72, 80: 96}
    Throw = random.randint(1, 6)

    num = value + Throw
    if num > 100:
        print("BAD LUCK, YOU CANT MOVE, YOU NEED A {} TO WIN".format(100 - value))
        return value
    if num == 100:
        return num

    if num in snake_squares:

        print(snake_squares[num])
        num = snake_squares[num]

    elif num in ladder_squares:
        num = ladder_squares[num]

    return num
