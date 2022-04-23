# Snake and Ladder Game
# mindula dilthushan
# minduladilthushan1@gmail.com
# 22-04-23

import random
import time

print('Welcome Snake & Ladder Game !')

snakeAddress = {27: 5, 40: 3, 43: 18, 54: 31, 66: 45, 76: 58, 89: 53, 99: 41}
ladderAddress = {4: 25, 13: 46, 33: 49, 42: 63, 50: 69, 62: 81, 74: 92}


def ladder(data):
    if (data in ladderAddress.keys()):
        print("\033[1m" + "ඉනිමගක් සෙට් වුනා 😁" + "\033[0m")
        return ladderAddress[data]
    else:
        return data


def snake(data):
    if (data in snakeAddress.keys()):
        print("\033[1m" + "නයෙක් හිටියා 🐍" + "\033[0m")
        return snakeAddress[data]
    else:
        return data


def game_end(data):
    return (data >= 100)


def game_play():
    player_name = "\033[1m" + "Mindula" + "\033[0m"
    score = 0

    while (1):

        if (1 == 0):
            print(player_name, "ඔයාගේ දැන් ලකුණු :", score)
            break

        time.sleep(1)
        random_data = random.randint(1, 6)
        print("දාදු කැටේ අගය :", random_data)
        score += random_data
        score = ladder(score)
        score = snake(score)

        if score > 100:
            score = 100

        print(player_name, "ඔයාගේ ලකුණු :", score)

        if (game_end(score)):
            print(player_name, "ඔයා තරගය දිනුම්... සුභ පැතුම් !")
            exit()


game_play()
