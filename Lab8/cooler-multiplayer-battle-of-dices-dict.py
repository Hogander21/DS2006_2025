import dice
import copy

write_spacing = 5
win_amount = 3

round = 0
gameover = False

# This allows us to add or modify the dices we roll for each round easily and access them for print statements with ease.
dices = [dice.RollD6, dice.RollD20, dice.RollD100, dice.RollD6] # Gets our dices.

# Player Amount
player_amount = int(input("How many will be playing? ")) 
if player_amount < 2: # Force the game to be minimum 2 players
    player_amount = 2

print(f"{player_amount} players confirmed.")

# Template
player_info:dict = {
    "name": "",
    "wins": 0,
    "year": 0,
    "rolls": [] # Structure: player_info -> rolls -> dice type -> round result
}

# Get player data
players:list = []
for i in range(player_amount):
    player:dict = copy.deepcopy(player_info)

    player["name"] = input(f"What is Player {i+1}'s name?").capitalize()
    player["age"] = int(input(f"What is Player {i+1}'s age?"))

    for d in range(len(dices)):
        player["rolls"].append([])
    players.append(player)


# While loop that runs until a player wins
while gameover is False:
    
    print(f"Round {round+1} starts now!")
    round_rolls = [] # Stores the total of all players for that round
    for player in range(len(players)):
        round_rolls.append(0) # Initialize
        

    # Roll player dice
    for player in range(len(players)):

        roll_str = f"{players[player]["name"]} rolled " # result printing
        
        for _dice in range(len(dices)):
            roll = dices[_dice]()
            round_rolls[player] += roll
            players[player]["rolls"][_dice].append(roll)

            roll_str += f"{roll} on a {(str)(dices[_dice].__name__.split("Roll")[1])}, " # result printing
        
        # Print results of the roll
        roll_str += f"with a combined value of {round_rolls[player]}."
        print(roll_str)
    
    input("\nPress ENTER to continue...")

    max_roll = max(round_rolls)
    winners = []
    winners_str = "Round winners are"
    for player in range(len(players)):
        if round_rolls[player] >= max_roll:
            players[player]["wins"] += 1 # add 1 win to player
            
            winners.append(player)
            
            if len(winners) != 0: # put commas between each winner
                winners_str += ", "
            winners_str += f"{players[player]["name"]}"
    if len(winners) != 0:
        winners_str += "!"
        print(winners_str)

    for player in range(len(players)):
        if (players[player]["wins"] >= win_amount):
            print(f"{players[player]["name"]} has won the Battle of the Dices after {round} rounds and risen as a champion!")
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
file.write("\n\nBattle of dices results!\n\n")

write_str = ""
for player in range(len(players)):
    
    
    write_str += f"{players[player]["name"]}\n Age: {players[player]["age"]}\n Wins: {players[player]["wins"]}\n\n"


    # Round row
    write_str += InverseSpacingRounder("Round") + " "
    for _round in range(round):
        write_str += SpacingRounder(f"{_round+1}") + " "
    write_str += "\n"

    # Dice rows
    for _dice in range(len(dices)):
        # Gets the function name, splits it by roll then takes the second part. EX RollD6 -> D6
        name = dices[_dice].__name__.split("Roll")[1]
        write_str += InverseSpacingRounder(name) + " "
        for _round in range(round):
            write_str += SpacingRounder(f"{players[player]["rolls"][_dice][_round]}") + " "
        write_str += "\n"

    write_str += InverseSpacingRounder("Total") + " "
    for _round in range(round):
        total = 0
        for _dice in range(len(dices)):
            total += players[player]["rolls"][_dice][_round]
        
        write_str += SpacingRounder(f"{total}") + " "
    write_str += "\n\n"

file.write(write_str)