import random

# Enter your number
def ask_number_to_guess(nb_min, nb_max):
    number_guess = 0
    while number_guess == 0:
        number_in = input(f"Guess the number between {nb_min} and {nb_max} :")
        try:
            number_guess = int(number_in)
        except:
            print("Error : You must enter a number")
        else:
            if number_guess < nb_min or number_guess > nb_max:
                print(f"Error: The number must be between {nb_min} and {nb_max} . try again")
                number_guess = 0
    return number_guess

NUMBER_MIN = 1
NUMBER_MAX = 10
GUESS = random.randint(NUMBER_MIN, NUMBER_MAX)
NUMBER_TRY_MAX = 4

"""
number = 0
number_try = NUMBER_TRY_MAX
while not number == GUESS and number_try > 0:
    print(f"It's remain {number_try} try")
    number = ask_number_to_guess(NUMBER_MIN, NUMBER_MAX)
    if number == GUESS:
        print("Congratulation you guess the rigth")
    elif number > GUESS:
        print("The number is inferior")
        number_try -=1
    else:
        print("The number is superior")
        number_try -=1

if number_try == 0:
    print(f"You lost!, the correct number is {GUESS}")"""

win = False
for i in range(0, NUMBER_TRY_MAX):
    number_try = NUMBER_TRY_MAX - i
    print(f"It's remain {number_try} try")
    number = ask_number_to_guess(NUMBER_MIN, NUMBER_MAX)
    if number == GUESS:
        print("Congratulation you guess the rigth")
        win = True
        break
    elif number > GUESS:
        print("The number is inferior")
    else:
        print("The number is superior")

if not win:
    print(f"You lost!, the correct number is {GUESS}")