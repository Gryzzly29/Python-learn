import random

guessing_number = random.randint(1,100)

tries = 0
guesses = False
print("Welcome to the hame to guess the number!")
print("I'm thinking in a number between 1 and 100.")

while not guesses:
    tries =  int(input("Put your number here: "))
    guesses += 1

    if tries < guessing_number:
        print("Too low, Try again.")
    elif tries > guessing_number:
        print("Too high> Try again.")
    else:
        print(f":D Congrats!,  You got it right in {tries} tries")
    guesses = True