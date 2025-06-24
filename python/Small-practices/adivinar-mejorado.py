import random 

def play():
    secret_number = random.randint(1,100)
    tries = 0
    corect = False

    print("I'm thinking about a number between 1 and 100, try guessint it!")

    while not corect:
        try:
            input_number = int(input("Guess the number here: "))
            tries += 1

            if input_number < secret_number:
                print("Too low, Try again.")
            elif input_number > secret_number:
                print("Too high> Try again.")
            else:
                print(f":D Congrats!,  You got it right in {tries} tries")
                corect = True

        except ValueError:
            print("xxxxxxxxx, PLEASE TRY WITH A VALID NUMBER")

while True:
    play()
    play_again = input("You want to paly again? (y/n)").lower()
    if play_again != 'y':
        print("Thanks for playing, see you later")
        break