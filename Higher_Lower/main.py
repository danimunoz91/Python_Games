import random
from game_data import data
from art import logo, vs


def randomSelect():
    compareA = random.randint(1, len(data))
    compareB = random.randint(1, len(data))
    while compareA == compareB:
        compareB = random.randint(1, len(data))
    return compareA, compareB


def dataList(a, b):
    listA = list(data[a].values())
    listB = list(data[b].values())
    return f"Compare A: {listA[0]}, a {listA[2]}, from {listA[3]}", f"Compare B: {listB[0]}, a {listB[2]}, from {listB[3]}"


def getFollowers(a, b):
    listA = list(data[a].values())
    listB = list(data[b].values())
    return listA[1], listB[1]


def game():
    flag_game = True
    score = 0
    while flag_game:
        a, b = randomSelect()
        ta, tb = dataList(a, b)
        fa, fb = getFollowers(a, b)
        print(logo)
        if score > 0:
            print(f"You're right! Current score: {score}")
        print(ta)
        print(vs)
        print(tb)
        option = input("Who has more followers? Type 'A'or'B':").lower()
        if (option == 'a' and (fa > fb)) or (option == 'b' and (fb > fa)):
            score += 1
        else:
            flag_game = False
        if not flag_game:
            print(logo)
            print(f"Sorry that's wrong. Final Score: {score}")

game()
