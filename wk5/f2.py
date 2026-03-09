"""
number guessing game
ask the user a max of 7 times to guess a number
between 1 and 10

- generate a random number between 1 and 10
- start loop
- track the guesses in a list variable
- if user guesses duplicate number: alert via message
"""
import random
num_to_guess = random.randint(1, 10)
print(num_to_guess)  # just for demo purposes
track_guesses = []
for i in range(1, 8):
    user_guess = int(input("Enter guess number " + str(i) + " of 7: "))
    if user_guess in track_guesses:
        print("You already incorrected guessed the number of", user_guess)
    if user_guess == num_to_guess:
        print("You won, the correct number to guess was", num_to_guess)
        break  # escape or stop the loop on current iteration
    print(user_guess, "is incorrect. Please try again.")
    track_guesses.append(user_guess)
