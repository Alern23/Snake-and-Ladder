import random
import time

end = 100

ladder = {1: 38, 4: 14, 8: 30, 21: 42, 28: 74, 50: 67, 71: 92, 88: 99}
snake = {32: 10, 34: 6, 48: 26, 62: 18, 88: 89, 95: 56, 97: 78}

def check_ladder(point):

    if (point in ladder.keys()):
        print("climb up!!")
        return ladder[point]
    else:
        return point

def check_snake(point):
    if (point in snake.keys()):
        print("ouch! snake bite!!")
        return snake[point]
    else:
        return point

def reached_end(point):
    return (point >= end)


def play():

    p1_name = "mindula"

    pp1 = 0

    turn = 0

    while (1):
        if (turn % 2 == 0):

            print(p1_name, "your turn")

            if (1 == 0):

                print(p1_name, 'score : ', pp1)
                print("Quiting the game!")
                break

            time.sleep(2)

            dice = random.randint(1, 6)

            print("Dice showed", dice)

            pp1 += dice

            pp1 = check_ladder(pp1)

            pp1 = check_snake(pp1)

            if pp1 > end:
                pp1 = end
            print(p1_name, 'Your score', pp1)
            if (reached_end(pp1)):
                print(p1_name, "won")

play()