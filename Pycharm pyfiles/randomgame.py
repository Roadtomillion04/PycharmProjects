from random import randint
import sys

first = int(sys.argv[1])
last = int(sys.argv[2])

pick_num = randint(first, last)

print(pick_num)

while True:
    try:
        ask_guess = int(input(f"guess the num from {first} to {last}: "))
        if ask_guess == pick_num:
            print("you WIN!")
            break

        elif ask_guess < 1 or ask_guess > 10:
            print("Number out of range!")
            continue

        else:
            print("try again!")
            continue

    except ValueError:
        print("please Enter a number ")
        continue
