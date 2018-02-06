
import random

highest = 10
answer = random.randint(1, highest)

print("Please guess a number between 1 and {}: ".format(highest))
guess = 0
while guess != answer:
    guess = int(input())
    if guess == 0:
        print("Fire escape")
        break
    elif guess < answer:
        print("Please guess higher")
    elif guess > answer:  # guess must be greater than number
        print("Please guess lower")

    if guess == answer:
        print("Well done, you guessed it")
        break
