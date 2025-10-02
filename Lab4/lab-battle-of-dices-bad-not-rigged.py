# Battle of Dices is going to be an amazing 2 player game, 
# where two players face each other using only their sheer luck! 
# 
# The rules are:
# 
# Each player throws one D6.
# The player with the highest roll wins the round.  
# The first player to win 3 times is the winner.
#
# Our main task today is to implement the code necessary to bring this
# amazing game alive!

import random

print("🎲 Welcome to Battle of Dices! 🎲")

# Variables to keep track of the score:
player1_wins = 0
player2_wins = 0

round = 1

# Round 1
input("\nPress ENTER to roll the dice...")

player1_roll_r1 = random.randint(1, 100)
player2_roll_r1 = random.randint(1, 100)



print("Player 1 rolled: ", player1_roll_r1)
print("Player 2 rolled: ", player2_roll_r1)

input("\nPress ENTER to continue...")

# So far so good right? But how to check who got the highest roll?

if player1_roll_r1 > player2_roll_r1:
    player1_wins += 1
    print("Player 1 wins this round!")
    print("Because ", player1_roll_r1," is greater than ", player2_roll_r1)
elif player1_roll_r1 < player2_roll_r1:
    player2_wins = player2_wins + 1
    print("Player 2 wins this round!")
    print("Because ", player2_roll_r1," is greater than ", player1_roll_r1)
else:
    print("Amaaazzinng! This round has a tie!")

# We can print the game score:
print("The game score is Player1 ", player1_wins, " vs. ", player2_wins, " Player 2.")

# Now we need to check if either player won.
if player1_wins == 3:
    print("Player 1 is the new GOD of Dice!")
    print(f"Player1 result! {player1_roll_r1}")
    print(f"Player2 result! {player2_roll_r1}")
    exit() # If someone win we exit out of the game
elif player2_wins == 3:
    print("Player 2 is the new GOD of Dice!")
    print(f"Player1 result! {player1_roll_r1}")
    print(f"Player2 result! {player2_roll_r1}")
    exit() # If someone win we exit out of the game
else:
    print("This heated Battle of Dices is still going on! Who will win in the end? ")
# Since none of them would have won after 1 round, we could copy this code several times
# until we have enough times to make sure someone wins.

input("\nPress ENTER to roll the dice...")

player1_roll_r2 = random.randint(1, 100)
player2_roll_r2 = random.randint(1, 100)

print("Player 1 rolled: ", player1_roll_r2)
print("Player 2 rolled: ", player2_roll_r2)

input("\nPress ENTER to continue...")

# So far so good right? But how to check who got the highest roll?

if player1_roll_r2 > player2_roll_r2:
    player1_wins += 1
    print("Player 1 wins this round!")
    print("Because ", player1_roll_r2," is greater than ", player2_roll_r2)
elif player1_roll_r2 < player2_roll_r2:
    player2_wins = player2_wins + 1
    print("Player 2 wins this round!")
    print("Because ", player2_roll_r2," is greater than ", player1_roll_r2)
else:
    print("Amaaazzinng! This round has a tie!")

# We can print the game score:
print("The game score is Player1 ", player1_wins, " vs. ", player2_wins, " Player 2.")

# Now we need to check if either player won.
if player1_wins == 3:
    print("Player 1 is the new GOD of Dice!")
    print(f"Player1 result! {player1_roll_r1} {player1_roll_r2}")
    print(f"Player2 result! {player2_roll_r1} {player2_roll_r2}")
    exit() # If someone win we exit out of the game
elif player2_wins == 3:
    print("Player 2 is the new GOD of Dice!")
    print(f"Player1 result! {player1_roll_r1} {player1_roll_r2}")
    print(f"Player2 result! {player2_roll_r1} {player2_roll_r2}")
    exit() # If someone win we exit out of the game
else:
    print("This heated Battle of Dices is still going on! Who will win in the end? ")
input("\nPress ENTER to roll the dice...")

player1_roll_r3 = random.randint(1, 100)
player2_roll_r3 = random.randint(1, 100)

print("Player 1 rolled: ", player1_roll_r3)
print("Player 2 rolled: ", player2_roll_r3)

input("\nPress ENTER to continue...")

# So far so good right? But how to check who got the highest roll?

if player1_roll_r3 > player2_roll_r3:
    player1_wins += 1
    print("Player 1 wins this round!")
    print("Because ", player1_roll_r3," is greater than ", player2_roll_r3)
elif player1_roll_r3 < player2_roll_r3:
    player2_wins = player2_wins + 1
    print("Player 2 wins this round!")
    print("Because ", player2_roll_r3," is greater than ", player1_roll_r3)
else:
    print("Amaaazzinng! This round has a tie!")

# We can print the game score:
print("The game score is Player1 ", player1_wins, " vs. ", player2_wins, " Player 2.")

# Now we need to check if either player won.
if player1_wins == 3:
    print("Player 1 is the new GOD of Dice!")
    print(f"Player1 result! {player1_roll_r1} {player1_roll_r2} {player1_roll_r3}")
    print(f"Player2 result! {player2_roll_r1} {player2_roll_r2} {player2_roll_r3}")
    exit() # If someone win we exit out of the game
elif player2_wins == 3:
    print("Player 2 is the new GOD of Dice!")
    print(f"Player1 result! {player1_roll_r1} {player1_roll_r2} {player1_roll_r3}")
    print(f"Player2 result! {player2_roll_r1} {player2_roll_r2} {player2_roll_r3}")
    exit() # If someone win we exit out of the game
else:
    print("This heated Battle of Dices is still going on! Who will win in the end? ")
input("\nPress ENTER to roll the dice...")

player1_roll_r4 = random.randint(1, 100)
player2_roll_r4 = random.randint(1, 100)

print("Player 1 rolled: ", player1_roll_r4)
print("Player 2 rolled: ", player2_roll_r4)

input("\nPress ENTER to continue...")

# So far so good right? But how to check who got the highest roll?

if player1_roll_r4 > player2_roll_r4:
    player1_wins += 1
    print("Player 1 wins this round!")
    print("Because ", player1_roll_r4," is greater than ", player2_roll_r4)
elif player1_roll_r4 < player2_roll_r4:
    player2_wins = player2_wins + 1
    print("Player 2 wins this round!")
    print("Because ", player2_roll_r4," is greater than ", player1_roll_r4)
else:
    print("Amaaazzinng! This round has a tie!")

# We can print the game score:
print("The game score is Player1 ", player1_wins, " vs. ", player2_wins, " Player 2.")

# Now we need to check if either player won.
if player1_wins == 3:
    print("Player 1 is the new GOD of Dice!")
    print(f"Player1 result! {player1_roll_r1} {player1_roll_r2} {player1_roll_r3} {player1_roll_r4}")
    print(f"Player2 result! {player2_roll_r1} {player2_roll_r2} {player2_roll_r3} {player2_roll_r4}")
    exit() # If someone win we exit out of the game
elif player2_wins == 3:
    print("Player 2 is the new GOD of Dice!")
    print(f"Player1 result! {player1_roll_r1} {player1_roll_r2} {player1_roll_r3} {player1_roll_r4}")
    print(f"Player2 result! {player2_roll_r1} {player2_roll_r2} {player2_roll_r3} {player2_roll_r4}")
    exit() # If someone win we exit out of the game
else:
    print("This heated Battle of Dices is still going on! Who will win in the end? ")
input("\nPress ENTER to roll the dice...")

player1_roll_r5 = random.randint(1, 100)
player2_roll_r5 = random.randint(1, 100)

print("Player 1 rolled: ", player1_roll_r5)
print("Player 2 rolled: ", player2_roll_r5)

input("\nPress ENTER to continue...")

# So far so good right? But how to check who got the highest roll?

if player1_roll_r5 > player2_roll_r5:
    player1_wins += 1
    print("Player 1 wins this round!")
    print("Because ", player1_roll_r5," is greater than ", player2_roll_r5)
elif player1_roll_r5 < player2_roll_r5:
    player2_wins = player2_wins + 1
    print("Player 2 wins this round!")
    print("Because ", player2_roll_r5," is greater than ", player1_roll_r5)
else:
    print("Amaaazzinng! This round has a tie!")

# We can print the game score:
print("The game score is Player1 ", player1_wins, " vs. ", player2_wins, " Player 2.")

# Now we need to check if either player won.
if player1_wins == 3:
    print("Player 1 is the new GOD of Dice!")
    print(f"Player1 result! {player1_roll_r1} {player1_roll_r2} {player1_roll_r3} {player1_roll_r4} {player1_roll_r5}")
    print(f"Player2 result! {player2_roll_r1} {player2_roll_r2} {player2_roll_r3} {player2_roll_r4} {player2_roll_r5}")
    exit() # If someone win we exit out of the game
elif player2_wins == 3:
    print("Player 2 is the new GOD of Dice!")
    print(f"Player1 result! {player1_roll_r1} {player1_roll_r2} {player1_roll_r3} {player1_roll_r4} {player1_roll_r5}")
    print(f"Player2 result! {player2_roll_r1} {player2_roll_r2} {player2_roll_r3} {player2_roll_r4} {player2_roll_r5}")
    exit() # If someone win we exit out of the game
else:
    print("This heated Battle of Dices is still going on! Who will win in the end? ")
input("\nPress ENTER to roll the dice...")

player1_roll_r6 = random.randint(1, 100)
player2_roll_r6 = random.randint(1, 100)

print("Player 1 rolled: ", player1_roll_r6)
print("Player 2 rolled: ", player2_roll_r6)

input("\nPress ENTER to continue...")

# So far so good right? But how to check who got the highest roll?

if player1_roll_r6 > player2_roll_r6:
    player1_wins += 1
    print("Player 1 wins this round!")
    print("Because ", player1_roll_r6," is greater than ", player2_roll_r6)
elif player1_roll_r6 < player2_roll_r6:
    player2_wins = player2_wins + 1
    print("Player 2 wins this round!")
    print("Because ", player2_roll_r6," is greater than ", player1_roll_r6)
else:
    print("Amaaazzinng! This round has a tie!")

# We can print the game score:
print("The game score is Player1 ", player1_wins, " vs. ", player2_wins, " Player 2.")

# Now we need to check if either player won.
if player1_wins == 3:
    print("Player 1 is the new GOD of Dice!")
    print(f"Player1 result! {player1_roll_r1} {player1_roll_r2} {player1_roll_r3} {player1_roll_r4} {player1_roll_r5} {player1_roll_r6}")
    print(f"Player2 result! {player2_roll_r1} {player2_roll_r2} {player2_roll_r3} {player2_roll_r4} {player2_roll_r5} {player2_roll_r6}")
    exit() # If someone win we exit out of the game
elif player2_wins == 3:
    print("Player 2 is the new GOD of Dice!")
    print(f"Player1 result! {player1_roll_r1} {player1_roll_r2} {player1_roll_r3} {player1_roll_r4} {player1_roll_r5} {player1_roll_r6}")
    print(f"Player2 result! {player2_roll_r1} {player2_roll_r2} {player2_roll_r3} {player2_roll_r4} {player2_roll_r5} {player2_roll_r6}")
    exit() # If someone win we exit out of the game
else:
    print("This heated Battle of Dices is still going on! Who will win in the end? ")
input("\nPress ENTER to roll the dice...")

player1_roll_r7 = random.randint(1, 100)
player2_roll_r7 = random.randint(1, 100)

print("Player 1 rolled: ", player1_roll_r7)
print("Player 2 rolled: ", player2_roll_r7)

input("\nPress ENTER to continue...")

# So far so good right? But how to check who got the highest roll?

if player1_roll_r7 > player2_roll_r7:
    player1_wins += 1
    print("Player 1 wins this round!")
    print("Because ", player1_roll_r7," is greater than ", player2_roll_r7)
elif player1_roll_r7 < player2_roll_r7:
    player2_wins = player2_wins + 1
    print("Player 2 wins this round!")
    print("Because ", player2_roll_r7," is greater than ", player1_roll_r7)
else:
    print("Amaaazzinng! This round has a tie!")

# We can print the game score:
print("The game score is Player1 ", player1_wins, " vs. ", player2_wins, " Player 2.")

# Now we need to check if either player won.
if player1_wins == 3:
    print("Player 1 is the new GOD of Dice!")
    print(f"Player1 result! {player1_roll_r1} {player1_roll_r2} {player1_roll_r3} {player1_roll_r4} {player1_roll_r5} {player1_roll_r6} {player1_roll_r7}")
    print(f"Player2 result! {player2_roll_r1} {player2_roll_r2} {player2_roll_r3} {player2_roll_r4} {player2_roll_r5} {player2_roll_r6} {player2_roll_r7}")
    exit() # If someone win we exit out of the game
elif player2_wins == 3:
    print("Player 2 is the new GOD of Dice!")
    print(f"Player1 result! {player1_roll_r1} {player1_roll_r2} {player1_roll_r3} {player1_roll_r4} {player1_roll_r5} {player1_roll_r6} {player1_roll_r7}")
    print(f"Player2 result! {player2_roll_r1} {player2_roll_r2} {player2_roll_r3} {player2_roll_r4} {player2_roll_r5} {player2_roll_r6} {player2_roll_r7}")
    exit() # If someone win we exit out of the game
else:
    print("This heated Battle of Dices is still going on! Who will win in the end? ")
input("\nPress ENTER to roll the dice...")

player1_roll_r8 = random.randint(1, 100)
player2_roll_r8 = random.randint(1, 100)

print("Player 1 rolled: ", player1_roll_r8)
print("Player 2 rolled: ", player2_roll_r8)

input("\nPress ENTER to continue...")

# So far so good right? But how to check who got the highest roll?

if player1_roll_r8 > player2_roll_r8:
    player1_wins += 1
    print("Player 1 wins this round!")
    print("Because ", player1_roll_r8," is greater than ", player2_roll_r8)
elif player1_roll_r8 < player2_roll_r8:
    player2_wins = player2_wins + 1
    print("Player 2 wins this round!")
    print("Because ", player2_roll_r8," is greater than ", player1_roll_r8)
else:
    print("Amaaazzinng! This round has a tie!")

# We can print the game score:
print("The game score is Player1 ", player1_wins, " vs. ", player2_wins, " Player 2.")

# Now we need to check if either player won.
if player1_wins == 3:
    print("Player 1 is the new GOD of Dice!")
    print(f"Player1 result! {player1_roll_r1} {player1_roll_r2} {player1_roll_r3} {player1_roll_r4} {player1_roll_r5} {player1_roll_r6} {player1_roll_r7} {player1_roll_r8}")
    print(f"Player2 result! {player2_roll_r1} {player2_roll_r2} {player2_roll_r3} {player2_roll_r4} {player2_roll_r5} {player2_roll_r6} {player2_roll_r7} {player2_roll_r8}")
    exit() # If someone win we exit out of the game
elif player2_wins == 3:
    print("Player 2 is the new GOD of Dice!")
    print(f"Player1 result! {player1_roll_r1} {player1_roll_r2} {player1_roll_r3} {player1_roll_r4} {player1_roll_r5} {player1_roll_r6} {player1_roll_r7} {player1_roll_r8}")
    print(f"Player2 result! {player2_roll_r1} {player2_roll_r2} {player2_roll_r3} {player2_roll_r4} {player2_roll_r5} {player2_roll_r6} {player2_roll_r7} {player2_roll_r8}")
    exit() # If someone win we exit out of the game
else:
    print("This heated Battle of Dices is still going on! Who will win in the end? ")
input("\nPress ENTER to roll the dice...")

player1_roll_r9 = random.randint(1, 100)
player2_roll_r9 = random.randint(1, 100)

print("Player 1 rolled: ", player1_roll_r9)
print("Player 2 rolled: ", player2_roll_r9)

input("\nPress ENTER to continue...")

# So far so good right? But how to check who got the highest roll?

if player1_roll_r9 > player2_roll_r9:
    player1_wins += 1
    print("Player 1 wins this round!")
    print("Because ", player1_roll_r9," is greater than ", player2_roll_r9)
elif player1_roll_r9 < player2_roll_r9:
    player2_wins = player2_wins + 1
    print("Player 2 wins this round!")
    print("Because ", player2_roll_r9," is greater than ", player1_roll_r9)
else:
    print("Amaaazzinng! This round has a tie!")

# We can print the game score:
print("The game score is Player1 ", player1_wins, " vs. ", player2_wins, " Player 2.")

# Now we need to check if either player won.
if player1_wins == 3:
    print("Player 1 is the new GOD of Dice!")
    print(f"Player1 result! {player1_roll_r1} {player1_roll_r2} {player1_roll_r3} {player1_roll_r4} {player1_roll_r5} {player1_roll_r6} {player1_roll_r7} {player1_roll_r8} {player1_roll_r9}")
    print(f"Player2 result! {player2_roll_r1} {player2_roll_r2} {player2_roll_r3} {player2_roll_r4} {player2_roll_r5} {player2_roll_r6} {player2_roll_r7} {player2_roll_r8} {player2_roll_r9}")
    exit() # If someone win we exit out of the game
elif player2_wins == 3:
    print("Player 2 is the new GOD of Dice!")
    print(f"Player1 result! {player1_roll_r1} {player1_roll_r2} {player1_roll_r3} {player1_roll_r4} {player1_roll_r5} {player1_roll_r6} {player1_roll_r7} {player1_roll_r8} {player1_roll_r9}")
    print(f"Player2 result! {player2_roll_r1} {player2_roll_r2} {player2_roll_r3} {player2_roll_r4} {player2_roll_r5} {player2_roll_r6} {player2_roll_r7} {player2_roll_r8} {player2_roll_r9}")
    exit() # If someone win we exit out of the game
else:
    print("This heated Battle of Dices is still going on! Who will win in the end? ")
input("\nPress ENTER to roll the dice...")

player1_roll_r10 = random.randint(1, 100)
player2_roll_r10 = random.randint(1, 100)

print("Player 1 rolled: ", player1_roll_r10)
print("Player 2 rolled: ", player2_roll_r10)

input("\nPress ENTER to continue...")

# So far so good right? But how to check who got the highest roll?

if player1_roll_r10 > player2_roll_r10:
    player1_wins += 1
    print("Player 1 wins this round!")
    print("Because ", player1_roll_r10," is greater than ", player2_roll_r10)
elif player1_roll_r10 < player2_roll_r10:
    player2_wins = player2_wins + 1
    print("Player 2 wins this round!")
    print("Because ", player2_roll_r10," is greater than ", player1_roll_r10)
else:
    print("Amaaazzinng! This round has a tie!")

# We can print the game score:
print("The game score is Player1 ", player1_wins, " vs. ", player2_wins, " Player 2.")

# Now we need to check if either player won.
if player1_wins == 3:
    print("Player 1 is the new GOD of Dice!")
    print(f"Player1 result! {player1_roll_r1} {player1_roll_r2} {player1_roll_r3} {player1_roll_r4} {player1_roll_r5} {player1_roll_r6} {player1_roll_r7} {player1_roll_r8} {player1_roll_r9} {player1_roll_r10}")
    print(f"Player2 result! {player2_roll_r1} {player2_roll_r2} {player2_roll_r3} {player2_roll_r4} {player2_roll_r5} {player2_roll_r6} {player2_roll_r7} {player2_roll_r8} {player2_roll_r9} {player2_roll_r10}")
    exit() # If someone win we exit out of the game
elif player2_wins == 3:
    print("Player 2 is the new GOD of Dice!")
    print(f"Player1 result! {player1_roll_r1} {player1_roll_r2} {player1_roll_r3} {player1_roll_r4} {player1_roll_r5} {player1_roll_r6} {player1_roll_r7} {player1_roll_r8} {player1_roll_r9} {player1_roll_r10}")
    print(f"Player2 result! {player2_roll_r1} {player2_roll_r2} {player2_roll_r3} {player2_roll_r4} {player2_roll_r5} {player2_roll_r6} {player2_roll_r7} {player2_roll_r8} {player2_roll_r9} {player2_roll_r10}")
    exit() # If someone win we exit out of the game
else:
    print("This heated Battle of Dices is still going on! Who will win in the end? ")



