import dice

# Initializing storage variables for player results
player1_result = 0
player2_result = 0

rounds = 0

# While loop that runs until a player wins
while player1_result < 3 and player2_result < 3:
    rounds += 1
    # Anticipation input
    input("New round! Press enter to roll!")

    # Roll player dice
    player1_roll_d20 = dice.RollD20()
    player1_roll_d100= dice.RollD100()
    
    player2_roll_d20 = dice.RollD20()
    player2_roll_d100= dice.RollD100()

    player1_roll = player1_roll_d20 + player1_roll_d100
    player2_roll = player2_roll_d20 + player2_roll_d100

    # Print results of the roll
    print(f"Player 1 rolled {player1_roll_d20} on a D20, and {player1_roll_d100} on a D100, with a combined value of {player1_roll}")
    print(f"Player 2 rolled {player2_roll_d20} on a D20, and {player2_roll_d100} on a D100, with a combined value of {player2_roll}")

    # Run the results through our win conditions
    if player1_roll > player2_roll:
        # Player 1 win condition
        print ("Player 1 won this round!")
        player1_result += 1 # Add 1 win to player1
    elif player2_roll > player1_roll:
        # Player 2 win condition
        print("Player 2 won this round")
        player2_result += 1 # Add 1 win to player2
    else:
        # Tie
        print("Both players tied!")
    print(f"SCORE! {player1_result}:{player2_result}\n")
if player1_result > player2_result:
    print("Player 1 won!")
else:
    print("Player 2 won!")
print(f"It took them {rounds} rounds.")

