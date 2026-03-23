"""
Guessing game

User must guess a number between 1 and 100
On each number guessed, output higher or lower
track number to guess
track the numbers the user has guessed
create a directory called game_data
    inside dir, game1, game2, gameN => however many times user has played

        inside each directory
            number_to_guess.txt
            user_guesses.txt
            result.txt: if user won and how many guesses it took

"""
import os
import random

root_dir = os.getcwd()
root_dir = os.path.join(root_dir, "game_data")

if not os.path.exists(root_dir):
    os.makedirs(root_dir)

subfolders = os.listdir(root_dir)

num_subfolders = len(subfolders)

game_num = num_subfolders + 1

os.mkdir(os.path.join(root_dir, f"game{game_num}"))

num_min = 1
num_max = 10
num_to_guess = random.randint(num_min, num_max)
user_guesses = []

print(f"Your job is to guess a number between {num_min} and {num_max}: ")

while num_to_guess not in user_guesses:
    user_guesses.append(int(input(f"Enter a number between {num_min} and {num_max}: ")))
    guessed_num = user_guesses[-1]
    if guessed_num == num_to_guess:
        print("Congrats! You correctly guessed the number")
    elif guessed_num > num_to_guess:
        print("Guess a LOWER number")
    else:
        print("Guess a HIGHER number")

fo1 = open( os.path.join(root_dir, "number_to_guess.txt"), "w"    )
fo1.write(str(num_to_guess))
fo1.close()

fo2 = open( os.path.join(root_dir, "user_guesses.txt"), "w" )
fo2.writelines(  [ f"{guess}\n"  for guess in user_guesses  ]  )
fo2.close()

fo3 = open(os.path.join(root_dir, "result.txt"), "w")
result = "won" if num_to_guess in user_guesses else "lost"
fo3.write(f"The user {result}.\nThe user guessed {len(user_guesses)} times.")