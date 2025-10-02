# Keep track of inventory
inventory = {
    "apple": 50,
    "banana": 30,
    "orange": 20,
    "pineapple": 15,
    "carrot": 120
}

def AddItems(item):
    global inventory
    player_amount_choice = 1
    try: 
        player_amount_choice = int(input("How many do you want to add?"))
    except:
        return "Invalid amount"
    
    if item in inventory:
        inventory[item] += player_amount_choice
    else:
        inventory[item] = player_amount_choice

    return f"Added {player_amount_choice} to {item.capitalize()}, there is now {inventory[item]} in the inventory."

def RemoveItems(item):
    global inventory
    player_amount_choice = 1
    try: 
        player_amount_choice = int(input("How many do you want to remove?"))
    except:
        return "Invalid amount"

    if item in inventory:
        if inventory[item] - player_amount_choice > 0:
            inventory[item] -= player_amount_choice
        else:
            inventory[item] = 0
            return f"No {item.capitalize()} left."
    else:
        return f"No {item.capitalize()} found."

    return f"Removed {player_amount_choice} from {item.capitalize()}, there is now {inventory[item]} in the inventory."

def CheckItems(item):
    global inventory
    if item in inventory and inventory[item] > 0:
        return f"There is {inventory[item]} {item.capitalize()}"
    else:
        return f"There is no {item.capitalize()}"
    

while True:
    print("Inventory Menu\n(1) Add Items\n(2) Remove Items\n(3) Check Items\n(4) Quit")
    player_menu_choice = 0
    
    # Get menu choice
    try:
        player_menu_choice = int(input())
    except:
        print("Invalid choice.")
        continue
    
    # Get item choice
    try:
        player_item_choice = str(input("Which item do you want to check?\n")).lower()
    except:
        print("Invalid choice.")
        continue

    match player_menu_choice:
        case 1: # Add Items
            print(AddItems(player_item_choice))
        case 2: # Remove items
            print(RemoveItems(player_item_choice))
        case 3: # Check items
            print(CheckItems(player_item_choice))
        case 4:
            quit()
        case _:
            print("Invalid choice.")


    