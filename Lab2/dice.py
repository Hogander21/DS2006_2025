import random

# Will wait for the user to press enter to finish their input.
input("Press enter to roll the dice!")

# Roll the dice
result = random.randint(1,6)

# Show the result
print("You rolled a", result, "on a D20")
