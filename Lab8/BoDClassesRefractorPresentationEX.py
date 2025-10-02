import dice

# Simple for the standard BoD
# Assuming we only roll 1 dice per round and can track it easily.
# Assuming we only roll 1d6 for rolls.

# class Player():
#     def __init__(self, name, year):
#         self.name = name
#         self.year = year

#         self.wins = 0
#         self.rolls = [] # EX of getting a roll -> player.rolls[round] 


#     # RollD6 is from previously made dice class from labs.
#     def RollDice(self):
#         roll:int = dice.RollD6()
#         self.rolls.append(roll)
#         return roll
    
#     def AddWin(self):
#         self.wins += 1
#         return self.wins


# Overkill
# Reformats the game to run entirely through a class called game.


class Game():
    def __init__(self, dices:list, winsRequired:int , playerAmount:int, old_playerList):
        self.dices:list = dices
        self.winsRequired:int = winsRequired
        self.winners:list = [] # Saves winners for easy access.
        self.players:list = [] # Gets players & player info.
        self.rounds:list = [] # Saves our round objects.
        self.has_played_tie_breaker:bool = False

        # Import old players
        if old_playerList != None or len(old_playerList) != 0:
            
            for old_player in old_playerList:
                new_player = Player(old_player.name, old_player.year, self)
                self.players.append(new_player)

        # Creates more players if our playerAmount is higher than the player amount in our players list
        if playerAmount - len(self.players) > 0:
            for i in range(playerAmount):
                    self.CreatePlayer(i)

    def CreatePlayer(self, playerIndex:int):
        name:str = str(input(f"Player {playerIndex+1}'s name: ")).capitalize()
        year:int = int(input(f"Player {playerIndex+1}'sage: "))

        player:Player = Player(name, year, self)
        self.players.append(player)
        return player 

    def Play(self):
        # Make sure the game hasnt been played
        if len(self.rounds) != 0:
            print("This game has already been played!")
            return False
        
        while len(self.winners) <= 0:
            # Play round
            round = Round(self)
            round.Play()

            # Check for game winners & Apply round wins
            for player in round.highestRollers:
                if(player.AddWin()) >= self.winsRequired:
                    # Player Won
                    self.winners.append(player)


            self.rounds.append(round)
            if (len(self.winners) > 1):
                self.TieBreaker()

    def TieBreaker(self):
        self.has_played_tie_breaker = True
        players = self.winners

        print("\nTiebreaker Begins!")
        tieBreaker: Game = Game(self.dices, 1, len(players), players)
        tieBreaker.Play()
        
        # Load the game data from our tiebreaker into our game.
        # I mean how else are we going to save it correctly :P
        for player_index in range(len(players)):
            players[player_index].wins += tieBreaker.players[player_index].wins # import wins

            # Import rolls
            for dice_index in range(len(players[player_index].rolls)):
                players[player_index].rolls[dice_index].extend(tieBreaker.players[player_index].rolls[dice_index])
        
        # Load the round data from our tiebreaker into our game.
        for round_index in range(len(tieBreaker.rounds)):
            new_round:Round = Round(self)
            new_round.highestRoll = tieBreaker.rounds[round_index].highestRoll

            for player_index in range(len(tieBreaker.players)):
                if tieBreaker.players[player_index] in tieBreaker.rounds[round_index].highestRollers: # If the current player top rolled
                    new_round.highestRollers.append(players[player_index]) # Add current player from our game
                
                # Load tiebreaker player rolls into this games player rolls.
                new_round.player_rolls[players[player_index]] = tieBreaker.rounds[round_index].player_rolls[tieBreaker.players[player_index]]
            
            self.rounds.append(new_round) # Add the round to rounds

    def Save(self, filename:str):
        def SpacingRounder(str:str, write_spacing:int):
            return " "*(write_spacing - len(str)) + str 

        def InverseSpacingRounder(str:str, write_spacing:int):
            return str + " "*(write_spacing - len(str)) 

        def Divider(int:int, dividerLook:str):
            return (dividerLook*int + "\n") 
        

        # Settings
        write_str:str = f"BoD Results!\nSettings:\n winsRequired: {self.winsRequired}\n playerAmount: {len(self.players)}\n\n"
        
        # Stats
        write_str += f"Stats:\n winners: ({len(self.winners)}){self.winners}\n rounds: ({len(self.rounds)}){self.rounds}\n tiebreaker: {self.has_played_tie_breaker}\n\n"

        #Players
        write_str += f"Players:\n\n"
        for player in self.players:
            #Player Info
            write_str += f" {player.name}:\n  {InverseSpacingRounder("Age:",7)} {SpacingRounder(f"{player.year}",7)}\n  {InverseSpacingRounder("Wins:",7)} {SpacingRounder(f"{player.wins}",7)}\n\n"
            
            # Player rounds clarification row
            write_str += f"  {InverseSpacingRounder("Rounds",7)}"
            for i in range(len(player.rolls[0])):
                write_str += f" {SpacingRounder(str(i+1), 7)}"
            write_str += "\n"

            # Divider
            write_str += Divider(8*(len(player.rolls[0])+2), "-")

            # Per Dice
            for diceIndex in range(len(player.rolls)):
                if diceIndex == 0:
                    # Dice total
                    write_str += f"  {InverseSpacingRounder("Total",7)}"
                else:
                    # Dice name
                    write_str += f"  {InverseSpacingRounder(self.dices[diceIndex-1].__name__.split("Roll")[1],7)}"
                
                # Rolls
                for roundIndex in range(len(player.rolls[diceIndex])):
                    write_str += f" {SpacingRounder(str(player.rolls[diceIndex][roundIndex]), 7)}"
                write_str += "\n" # New row for next dice
            
            # Divider
            write_str += Divider(8*(len(player.rolls[0])+2), "-")

            
            write_str += "\n" # New row for next player
            
        longestPlayerName:int = len("Rounds")
        for player in self.players:
            if len(player.name) > longestPlayerName:
                longestPlayerName = len(player.name)
        
        # Wins visualized
        write_str += f"Wins visualized:\n"
        # Player rounds clarification row
        write_str += f" {InverseSpacingRounder("Rounds",longestPlayerName)}"
        for i in range(len(player.rolls[0])):
            write_str += f" {SpacingRounder(str(i+1), 7)}"
        write_str += "\n"

        # Divider
        write_str += Divider(8*(len(player.rolls[0])+2), "-")

        
        # Visualizing wins player by player
        for player in self.players:
            write_str += f" {InverseSpacingRounder(player.name, longestPlayerName)}" # Player name
            
            player_wins_so_far = 0 
            for round in self.rounds:
                player_wins_print_str = ""
                if player in round.highestRollers:
                    player_wins_so_far += 1
                    player_wins_print_str = str(player_wins_so_far)
                write_str += f" {SpacingRounder(player_wins_print_str, 7)}" # New win count as we get a new win
            write_str += "\n" # New row for new player
            write_str += Divider(8*(len(player.rolls[0])+2), "-") # New divider for new player
        
        # Totals Comparison
        write_str += "\n\nTotals Comparison:\n" 

        # Round visualiser
        write_str += f" {InverseSpacingRounder("Rounds",longestPlayerName)}"
        for i in range(len(player.rolls[0])):
            write_str += f" {SpacingRounder(str(i+1), 7)}"
        write_str += "\n"

        # Divider
        write_str += Divider(8*(len(player.rolls[0])+2), "-")

        for player in self.players:
            write_str += f" {InverseSpacingRounder(player.name, longestPlayerName)}" # Player name
            for round_total in player.rolls[0]:
                write_str += f" {SpacingRounder(str(round_total),7)}"
            write_str += "\n" # new row for new player



        # Write the file XD
        file = open(filename+".txt", "w")
        file.write(write_str)
        print(f"Saved as {filename+".txt"}!")
        return write_str
class Round():
    def __init__(self, game:Game):
        self.game:Game = game
        self.highestRoll:int = 0
        self.highestRollers:list = []

        self.player_rolls:dict = {}

    def Play(self):
        
        # Rolls for all players
        for player in self.game.players:
            rolls = player.RollDices()

            # Updates highest roll
            if rolls[0] > self.highestRoll:
                self.highestRoll = rolls[0] 

            self.player_rolls[player] = rolls

        # Check winners
        for player in self.game.players:
            if self.player_rolls[player][0] == self.highestRoll:
                self.highestRollers.append(player)
                print(f"{player.name} is the newest round winner!")    
class Player():
    def __init__(self, name:str, year:int, game):
        self.name:str = name
        self.year:int = year

        self.wins = 0

        # Structure example: call the dices using player.rolls[dice(index) + 1][round].
        # Structure example: player.rolls[0][round] = round total.
        if game != None:
            self.game:Game = game
            self.rolls:list = []
            for i in range(len(self.game.dices)+1): # +1 to create an extra spot for round totals
                self.rolls.append([])

    # Rolls all the dices and
    def RollDices(self):
        """
        Return:
            List:
                Int: 
                    Returns a list of ints.
                    Entry 0 being the total of all the others.
        """
        rolls = []
        rolls.append(0)

        

        # Gets all the dices but the last one
        for i in range(len(self.game.dices)):
            # Roll
            roll:int = self.game.dices[i]()

            # Save for return
            rolls[0] += roll
            rolls.append(roll)

            # +1 to leave 0 for total
            self.rolls[i+1].append(roll)
        
        # Print
        print_str = f"Player {self.name}"
        for i in range(len(self.game.dices)):
            # .__name__.split("Roll")[1] gets method name, splits it by "Roll" and gets the second part of that so it just EX: RollD6 -> [ "", "D6"]
            print_str += f" rolled {rolls[i+1]} on a {self.game.dices[i].__name__.split("Roll")[1]}"
            if i != len(self.game.dices)-1:
                print_str += " and"
        print_str += f". With a total of {rolls[0]}!"
        print(print_str)

        self.rolls[0].append(rolls[0])
        return rolls

    def AddWin(self):
        self.wins += 1
        return self.wins

# Example information
#dices:list = [dice.RollD6, dice.RollD6, dice.RollD20] # This Example dices list will play 2d6 + 1d20
dices:list = [dice.RollD6, dice.RollD6, dice.RollD20] # This Example dices list will play 2d6 + 1d20

print("Time to play Battle of Dices!")
#winsRequired:int = int(input("Wins required to win? "))
#playerAmount:int = int(input("How many players: "))
winsRequired:int = 1
playerAmount:int = 3
players = [Player("Phil",21,None), Player("Satu", 21, None), Player("Ark", 19, None)]

game:Game = Game(dices, winsRequired, playerAmount, players)
game.Play()
game.Save("output")