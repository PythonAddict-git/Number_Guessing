import random

# Taking Inputs
lower = int(input("Enter Lower bound:- "))

# Taking Inputs
upper = int(input("Enter Upper bound:- "))

# generating random number between
# the lower and upper
x = random.randint(lower, upper)
total_chances = 5
print("\n\tYou've only ", total_chances, " chances to guess the integer!\n")

# Initializing the number of guesses.
count = 0


# for calculation of minimum number of
# guesses depends upon range
while count < total_chances:
    count += 1

    # taking guessing number as input
    guess = int(input("Guess a number:- "))

    # Condition testing
    if x == guess:
        print("Congratulations you did it in ",
              count, " try")
        # Once guessed, loop will break
       
        break
    elif x > guess:
        print("You guessed too small!")
    elif x < guess:
        print("You Guessed too high!")

# If Guessing is more than required guesses,
# shows this output.
    print("\tBetter Luck Next time!")

print("\nThe number is %d" % x)
    
