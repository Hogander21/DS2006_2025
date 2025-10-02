import random

playerScore = 0
enemyScore = 0

def Win():
    global playerScore
    playerScore += 1
    print("Announcer\n  Player won!\n\nEnemy\n  It won't happen again!\n")

def Lose():
    global enemyScore
    enemyScore += 1
    print("Announcer\n  Enemy won!\n\nEnemy\n  Might as well surrender kid.\n")

def Tie():
    print("Announcer\n  A tie! Oh the excitement goes to the ceiling!\n")

def Quit():
    print("Announcer\n  Player Quits!\n\nEnemy\n  It's good that you know your place punk!")

def Score():
    """
    Check the score
    
    """
    if playerScore == 0 and enemyScore == 0:
        print(f"Accouncer\n  You don't trust me? Here in my game both players start equal. Always.")
    elif playerScore == enemyScore:
        print(f"Accouncer\n  The score is tied at {playerScore} points each!")
    elif playerScore > enemyScore:
        print(f"Announcer\n  The score is {playerScore} to {enemyScore} in the Players favour!")
    else:
        print(f"Announcer\n The score is {enemyScore} to {playerScore} in the Enemys favour!")
    input("  Ready to play?\n\nPlayer\n  Yes. (Press enter to continue..)") # Anticipation

def MoveToText(intMove):
    """
    Simply converts an integer move into a text move.
    """
    match int(intMove):
        case 0:
            return "To Check the Score"
        case -1: 
            return "I Quit"
        case 1:
            return "Rock"
        case 2:
            return "Paper"
        case 3:
            return "Scissor"
        case 4: 
            return "to pull out Carlos my teacher"
        case _:
            return "An Invalid move."

def TextToMove(textMove):
    """
    Simply converts text move into a integer move.
    """
    match str(textMove):
        case "To Check the Score":
            return 0
        case "I Quit": 
            return -1
        case "Rock":
            return 1
        case "Paper":
            return 2
        case "Scissor":
            return 3
        case "to pull out Carlos my teacher":
            return 4
        case _:
            return 99
    


def MoveVersusMove(moveOne, moveTwo):
    """"
    Handles the game logic. 
    
    """
    match int(moveOne):
        case -1: # Quit
            Quit()
        case 0: # Check Score
            Score()
        case 1: # Rock
            match int(moveTwo):
                case 2: 
                    # Lose
                    Lose()
                case 3:
                    # Win
                    Win()
                case _:
                    # Ties
                    Tie()
                    

        case 2: # Paper
            match int(moveTwo):
                case 3:
                    # Lose
                    Lose()
                case 1:
                    # Win
                    Win()
                case _:
                    # Ties
                    Tie()

        case 3: # Scissor
            match int(moveTwo):
                case 1: 
                    # Loss
                    Lose()
                case 2:
                    # Win
                    Win()
                case _:
                    # Tie
                    Tie()

        case 4: # Carlos
            Win()
            print("Carlos\n  Oh it will happen!\n  As long as my student keeps coming to my lectures!\n")

        case _:
            Lose()
            print("Announcer\n  I'm not supposed to help but have you considered using a legal move?\n")
         




print("Jankenpo by Philip Haglund\n\nAnnouncer\n  Welcome to my game Player!\n  Now be ready to battle!\n")

# General game loop
while playerScore < 3 and enemyScore < 3:
    playerInput = input("Announcer\n  Choose your move Player.\n  (-1) Quit!\n  (0) Check the score!\n  (1) Rock\n  (2) Paper\n  (3) Scissor\n  (4) Carlos\n")
    enemyInput = random.randrange(1,4)

    print("Announcer\n  Choices have been collected reveal your moves!\n")
    print(f"Player\n  I chose {MoveToText(playerInput).lower()}.\n")
    print(f"Enemy\n  I chose {MoveToText(enemyInput).lower()}.\n")

    MoveVersusMove(playerInput, enemyInput)

if playerScore >= 3:
    print("Announcer\n  Player wins!\n\nEnemy\n  No, how?\n  I demand a recount!\nAnnouncer\n  What insolence!")
    input("  What's your victory speech Player?\n\nPlayer\n  ")
else:
    print("Announcer\n  Enemy wins!\n\nEnemy\n  You didn't even stand a chance!")