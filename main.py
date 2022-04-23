# Snake and Ladder Game
# mindula dilthushan
# minduladilthushan1@gmail.com
# 22-04-09
from random import random

class Lottery:

    @staticmethod
    def getLottery():
        return random.randint(1, 6)


def print_hi(game):
    print(f'Welcome, {game}')

if __name__ == '__main__':
    print_hi('Snake and Ladder Game !')



