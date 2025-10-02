import copy
import dice

# Variables to keep track of:
rounds = 0
gameover = False
# Number of wins needed to win the game:
winning_score = 3

# Dictionary template
player_info = {
    "name": "",
    "email": "",
    "country": "",
    "wins": 0,
    "rolls": []
}

# List 
players = []

# Obtain number of players
number_of_players = int(input("How many players? "))

# For loop to obtain player names:
for i in range(number_of_players):
    
    # Make a deep copy
    player = player_info.copy()
    # player = copy.deepcopy(player_info)

    player["name"] = input(f"What is the name of Player {i+1}? ")
    player["email"] = input(f"What is the email of Player {i+1}? ")
    player["country"] = input(f"What is the country of Player {i+1}? ")

    players.append(player)

while gameover is False:
    print(f"Round {rounds+1}:")
    #input("\nPress ENTER to continue...")

    # Dice roll for each player in the current round:
    current_rolls = []

    # We need to roll the dice for each player:
    for each_player in players:
        roll = dice.RollD6()

        #player_rolls_history[i].append(roll)
        each_player["rolls"].append(roll)

        current_rolls.append(roll)

        print(f"Player {each_player["name"]} rolled: {roll}")
    
    max_roll = max(current_rolls)

    # Find winners of the round:
    winners = []

    # Search for all players who got the highest roll:
    for each_player in players:
        if(each_player["rolls"][-1] == max_roll):
            each_player["wins"] += 1
            print(f"Player {each_player["name"]} won in round {rounds}")

            winners.append(each_player["name"])
    print(f"Winners of this round: {winners}")

    for each_player in players:
        if(each_player["wins"] >= winning_score):
            print(f"\n{each_player["name"]} is the newest Battle of Dices Champion!")
            gameover = True
    if gameover is False:
        print("This heated Battle of Dices is still going on! Who will win in the end?")
    rounds += 1

filename = input("Enter the filenameto save the results: ")
with open(filename, "w") as file: # 'w' = write mode
    # Player information:
    file.write("Player Information:\n")

    # Save each player information using python automatic concatenation
    # of adjecent strings:
    for each_player in players:
        file.write(
            f"Name: {each_player["name"]}\n"
            f"* E-mail: {each_player["email"]}\n"
            f"* Country: {each_player["country"]}\n"
            f"* Wins: {each_player["wins"]}\n\n"
        )
    
    file.write("\nGame rounds:\n")

    # Round history
    for r in range(rounds):
        # Start with empty text
        rolls_str = ""

        # Go through each player and build the string step by step
        for i, each_player in enumerate(players):
            rolls_str += f"{each_player["name"]} rolled {each_player["rolls"][r]}"

            # Add a comma and space unless its the last player
            if i < len(players) -1:
                rolls_str += ", "

        file.write(f"Round {r+1}:\n {rolls_str}\n")

print("\nGame over! Results save successfully.")