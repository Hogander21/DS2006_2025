visitedCities = []
uniqueVisitedCities = []

def AddNewCity(city):
    global uniqueVisitedCities
    if uniqueVisitedCities.count(city) == 0:
        uniqueVisitedCities.append(city)
        print("New unique city added!")
    
    visitedCities.append(city)
    print("City added!")
    
def ViewListOfUniqueVisitedCities():
    global uniqueVisitedCities
    global visitedCities
    view_str = "You have visited:\n"
    for c in range(len(uniqueVisitedCities)):
        view_str += f"{c+1}: {uniqueVisitedCities[c]}: {visitedCities.count(uniqueVisitedCities[c])}\n"
    return view_str
    
def SortListOfVisitedCities():
    global uniqueVisitedCities
    uniqueVisitedCities.sort()
    print(ViewListOfUniqueVisitedCities())

def NumberOfCitiesVisited():
    print(f"You have visited a total of {len(visitedCities)} cities! In {len(uniqueVisitedCities)} unique cities!")

def RemoveACity(city):
    if visitedCities.count(city) == 1:
        uniqueVisitedCities.remove(city)
        print("Unique city removed!")

    if visitedCities.count(city) > 0:
        visitedCities.remove(city)
        print("Visit removed!")
    else:
        print("You haven't visited that city before!")

def RemoveAllCities():
    confirm = input("If you want to remove all cities type: 'YES'").lower()
    if confirm == 'yes':
        visitedCities.clear()
        uniqueVisitedCities.clear()
        print("Cleared all cities!")
    else:
        print("Cancelled command!")

def SaveData():
    file = "visited_Places_Save_Data"
    file = open(file+".txt", "w")

    data_str = "Visited Places Save Data\n" + ViewListOfUniqueVisitedCities()
    file.write(data_str)
    print("Save successful! (file saved as 'visited_Places_Save_Data.txt')")

while True:
    intro_str = ""
    intro_str += "\n                My Travel List!\n"
    intro_str += "Please choose one of the following options:\n\n"
    intro_str += "(1) Add a new city to the list of visited cities.\n"
    intro_str += "(2) View your list of visited cities.\n"
    intro_str += "(3) Sort the list of visited cities.\n"
    intro_str += "(4) Shows the number of visited cities.\n"
    intro_str += "(5) Remove a given city from the list of visited cities.\n"
    intro_str += "(6) Remove all cities from the list of visited cities.\n"
    intro_str += "(7) Save the list of visited cities to a file.\n"
    intro_str += "(8) Quit"

    print(intro_str)
    
    player_choice = 0
    try:
        player_choice = int(input())
    except:
        player_choice = 0

    match player_choice:
        case 1:
            player_input = input("What is the city called? ")
            AddNewCity(player_input.capitalize())
        case 2:
            print(ViewListOfUniqueVisitedCities())
        case 3:
            SortListOfVisitedCities()
        case 4:
            NumberOfCitiesVisited()
        case 5:
            player_input = input("What is the city called? ")
            RemoveACity(player_input.capitalize())
        case 6:
            RemoveAllCities()
        case 7:
            SaveData()
        case 8:
          quit()
        case _:
            print("Invalid menu choice!")

    input("Ready to continue?")
