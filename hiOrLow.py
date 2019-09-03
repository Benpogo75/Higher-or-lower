import random

guess = int(input("Pick an integer between 1 and 100 "))
randnum = random.randint(1,100)
while guess != randnum:
    if guess > randnum:
        print("Lower")
        guess = int(input())
    if guess < randnum:
        print("Higher")
        guess = int(input())
if guess == randnum:
    print("You win")
