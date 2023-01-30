import random
import math

# FIXME: Import the logging module and set level
# FIXME: Add logging for start of game

# Taking Inputs
lower = int(input("Enter Lower bound:- "))

# Taking Inputs
upper = int(input("Enter Upper bound:- "))

# generating random number between
# the lower and upper
target_number = random.randint(lower, upper)
print(
    "\n\tYou've only ",
    round(math.log(upper - lower + 1, 2)),
    " chances to guess the integer!\n",
)

# Initializing the number of guesses.
guess_count = 0

# for calculation of minimum number of
# guesses depends upon range
while guess_count < math.log(upper - lower + 1, 2):
    guess_count += 1

    # taking guessing number as input
    guess = int(input("Guess a number:- "))

    # Condition testing
    if target_number == guess:
        print("Congratulations you did it in ", guess_count, " try")
        # Once guessed, loop will break
        # FIXME: Add logging for correct guess
        break
    elif target_number > guess:
        print("You guessed too small!")
    elif target_number < guess:
        print("You Guessed too high!")

    # FIXME: Add logging for wrong guess


# If Guessing is more than required guesses,
# shows this output.
if guess_count >= math.log(upper - lower + 1, 2):
    print("\nThe number is %d" % target_number)
    print("\tBetter Luck Next time!")

# FIXME: Add logging for end of game
