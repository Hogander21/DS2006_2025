import dice

write_spacing = 5
win_amount = 3

# This allows us to add or modify the dices we roll for each round easily and access them for print statements with ease.
dices = [dice.RollD6, dice.RollD20, dice.RollD100] # Gets our dices.
dice_amount = len(dices)

# Player Amount
player_amount = int(input("How many will be playing? ")) 
if player_amount < 2: # Force the game to be minimum 2 players
    player_amount = 2

print(f"{player_amount} players confirmed.")

# Get player names
player_names = []
for i in range(player_amount):
    player_names.append(input(f"What is the name of Player {i+1}? "))
    # player_names.append(i+1) # Testing

# Initializing storage variables
player_rolls = [] # Tripple nestled player -> round -> dice -> result
player_wins = []

for player in range(player_amount):
    player_rolls.append([]) # initialize
    player_wins.append(0) # initialize

def RoundInitializePlayerRolls(round):
    global player_rolls
    for player in range(player_amount):
        player_rolls[player].append([])# intialize



round = 0
gameover = False

# While loop that runs until a player wins
while gameover is False:
    
    print(f"Round {round+1} starts now!")

    RoundInitializePlayerRolls(round)
    round_rolls = [] # Stores the total of all players for that round

    # Roll player dice
    for player in range(player_amount):
        round_rolls.append(0) # Initialize
        
        roll_str = f"{player_names[player]} rolled " # result printing
        
        for _dice in range(dice_amount):
            roll = dices[_dice]()
            round_rolls[player] += roll
            player_rolls[player][round].append(roll)

            roll_str += f"{roll} on a {(str)(dices[_dice].__name__.split("Roll")[1])}, " # result printing
        
        # Print results of the roll
        roll_str += f"with a combined value of {round_rolls[player]}."
        print(roll_str)
    
    input("\nPress ENTER to continue...")

    max_roll = max(round_rolls)
    winners = []
    winners_str = "Round winners are"
    for player in range(player_amount):
        if round_rolls[player] >= max_roll:
            player_wins[player] += 1 # add 1 win to player
            
            winners.append(player)
            
            if len(winners) != 0: # put commas between each winner
                winners_str += ", "
            winners_str += f"{player_names[player]}"
    if len(winners) != 0:
        winners_str += "!"
        print(winners_str)

    for player in range(player_amount):
        if (player_wins[player] >= win_amount):
            print(f"{player_names[player]} has won the Battle of the Dices after {round} rounds and risen as a champion!")
            gameover = True
    
    if gameover is False:
        print(f"The Battle of the Dices continues!")
    round += 1
        

# Save Game Data to file!

def SpacingRounder(str):
    return " "*(write_spacing - len(str)) + str 

def InverseSpacingRounder(str):
    return str + " "*(write_spacing - len(str)) 

# Open file.
#file = input("Choose file name!")
file = "output"
file = open(file+".txt", "a")

# Print roll data and write it to file
file.write("\n\nBattle of dices results!\n")

write_str = ""
for player in range(player_amount):
    write_str += f"{player_names[player]}\n"

    # Round row
    write_str += InverseSpacingRounder("Round") + " "
    for _round in range(round):
        write_str += SpacingRounder(f"{_round+1}") + " "
    write_str += "\n"

    # Dice rows
    for _dice in range(dice_amount):
        # Gets the function name, splits it by roll then takes the second part. EX RollD6 -> D6
        name = dices[_dice].__name__.split("Roll")[1]
        write_str += InverseSpacingRounder(name) + " "
        for _round in range(round):
            write_str += SpacingRounder(f"{player_rolls[player][_round][_dice]}") + " "
        write_str += "\n"
    write_str += "\n"

file.write(write_str)