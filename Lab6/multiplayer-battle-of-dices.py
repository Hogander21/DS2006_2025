import dice


winning_score = 3 # wins needed to win
player_names = [] # Array for storing the names
player_wins = [] # Array for storing the names of the players

 # Obtain the number of players:
number_of_players = int(input("How many players?"))
if number_of_players < 2:
    number_of_players = 2

# For loop to obtain the player names:
for i in range(number_of_players):
    name = input(f"What is the name of Player {i+1}?")
    player_names.append(name)

# Initialize scores and rolls
for i in range(number_of_players):
    player_wins.append(0)

# Initialize player rolls as empty list for each player
player_rolls_history = [] # Nestled list

for i in range(number_of_players):
    # Add an empty list for each player:
    player_rolls_history.append([])

rounds = 0
gameover = False
while gameover is False:
    
    print(f"Round {rounds+1}:")

    # Dice roll for each player in the current round:
    current_rolls = []

    # We need to roll the dice for each player:
    for i in range(number_of_players):
        roll = dice.RollD6()
        current_rolls.append(roll)
        player_rolls_history[i].append(roll)
        print(f"Player {player_names[i]} rolled: {roll}")

    input("\nPress ENTER to continue...")

    max_roll = max(current_rolls) # Gets highest roll this round
    winners = [] # will store who won this round

    for j in range(len(current_rolls)):
        if current_rolls[j] == max_roll:
            winners.append(player_names[j])
            player_wins[j] += 1
    
    print(f"Winners of this round are: {winners}")

    for z in range(number_of_players): # Check if people won. Can be multiple winners.
        if player_wins[z] >= winning_score:
            print(f"\n{player_names[z]} is the newest Battle of Dices Champion!")
            gameover = True

    if gameover is False:
        print("This heated Battle of Dices is still going on! Who will win in the end?")

    rounds +=1

# Save results to a file
filename = input("Enter the filename to save the results: ")
with open(filename, "w") as file: # "w" = write
    for round_number in range(rounds):
        file.write(f"Round {round_number+1}: ")
        rolls_str = "" # initialize string
        for i in range(number_of_players):
            rolls_str += (f"{player_names[i]} rolled {player_rolls_history[i][round_number]}")
            if i < number_of_players - 1: # seperate the players except the last one.
                rolls_str += ", "
        print(f"Saving {rolls_str}")
        file.write(rolls_str + "\n")
