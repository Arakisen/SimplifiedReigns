# Title: ...
# Author: Arakis
#
# Desc: My first project in Python
#


import random
from os import system
from msvcrt import getch

random.seed()


def generate_choice():
    groups = ["Military", "Clergy", "Peasants", "Merchants"]

    plus = random.choice(groups)
    plus_value = random.randrange(5, 26)

    groups.remove(plus)

    minus = random.choice(groups)
    minus_value = random.randrange(5, 26)

    return plus, plus_value, minus, minus_value


def print_choices(a, b):
    print("A)\n   {} will gain: {} influence".format(a[0], a[1]))
    print("   {} will lose: {} influence".format(a[2], a[3]))

    print("B)\n   {} will gain: {} influence".format(b[0], b[1]))
    print("   {} will lose: {} influence".format(b[2], b[3]))


def change_influence(dict, add_group, add_value, sub_group, sub_value):
    for a in dict:
        if a == add_group:
            dict[a] += add_value

    for b in dict:
        if b == sub_group:
            dict[b] -= sub_value

    return dict

while True:
    year = 0
    groups = {
    'Military': random.randrange(10, 91),                           # generating random values when starting new game
    'Clergy': random.randrange(10, 91),
    'Peasants': random.randrange(10, 91),
    'Merchants': random.randrange(10, 91)
    }

    while all(i > 0 for i in groups.values()) and all(i < 100 for i in groups.values()):
        system('cls')
        year += 1
        print("  Military: {} Clergy: {}".format(groups['Military'], groups['Clergy']))
        print("  Peasants: {} Merchants: {}".format(groups['Peasants'], groups['Merchants']))

        choice_a = generate_choice()
        choice_b = generate_choice()

        print_choices(choice_a, choice_b)

        choice = input("\nChoose: ")

        if choice == 'a' or choice == 'A':
            groups = change_influence(groups, choice_a[0], choice_a[1], choice_a[2], choice_a[3])

        if choice == 'b' or choice == 'B':
            groups = change_influence(groups, choice_b[0], choice_b[1], choice_b[2], choice_b[3])

    if year == 1:
        print("You have survived {} year and {} months".format(year, random.randrange(1, 12)))
    else:
        print("You have survived {} years and {} months".format(year, random.randrange(1, 12)))

    print("\n\n Do you want to play again?")

    restart = input("(Y/N)")
    if restart == 'Y' or restart == 'y':
        continue
    if restart == 'N' or restart == 'n':
        break
    else:
        print("???")

