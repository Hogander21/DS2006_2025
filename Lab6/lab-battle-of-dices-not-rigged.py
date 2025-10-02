import dice

# Initializing storage variables for player results
player1_result = 0
player2_result = 0

# Data storage
player1_rolls = []
player2_rolls = []

rounds = 0

# While loop that runs until a player wins
while player1_result < 3 and player2_result < 3:
    rounds += 1
    # Anticipation input
    input("\nPress ENTER to roll the dice for Player 1...")

    # Roll player dice
    player1_roll_d20 = dice.RollD20()
    player1_roll_d100= dice.RollD100()
    
    player1_roll = player1_roll_d20 + player1_roll_d100
    
    # Storing rolls
    player1_rolls.append(player1_roll_d20)
    player1_rolls.append(player1_roll_d100)

    # Anticipation input
    input("\nPress ENTER to roll the dice for Player 2...")

    # Roll player dice
    player2_roll_d20 = dice.RollD20()
    player2_roll_d100= dice.RollD100()

    player2_roll = player2_roll_d20 + player2_roll_d100

    # Storing rolls
    player2_rolls.append(player2_roll_d20)
    player2_rolls.append(player2_roll_d100)

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

# Victory print
if player1_result > player2_result:
    print("Player 1 won!")
else:
    print("Player 2 won!")
print(f"It took them {rounds} rounds.\n")

def printPlayerData(title, player_rolls, roundsPlayed):
    """
    Prints a summary of player data.
    
    Returns:
        str: formatted string with game values
    """
    #String to store our future print a lot of things are extra fluff formatting
    player_stats_str = "\n\n" + title + "\n" + ("-"*10) + "\nD20:  "
    
    # Formats the D20 values properly into the stats str
    for x in range(roundsPlayed):
        value = str(player_rolls[x*2])
        value = ("0"*(3-len(value))) + value

        player_stats_str +=  value + " | "

    player_stats_str += "\nD100: "

    # Formats the D100 values properly into the stats str
    for x in range(roundsPlayed):
        value = str(player_rolls[x*2+1])
        value = ("0"*(3-len(value))) + value

        player_stats_str += value + " | "

    # Prints and returns it (because it can be useful)
    print(player_stats_str)
    return player_stats_str


# Save Game Data to file!

# Open file.
file = input("Choose file name!")
file = open(file+".txt", "a")

# Print roll data and write it to file
file.write("\n\nBattle of dices results!")
file.write(printPlayerData("Player1", player1_rolls, rounds))
file.write(printPlayerData("Player2", player2_rolls, rounds))

