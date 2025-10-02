print("*** Welcome to Basic Calculator ***")
print("Choose a mathematical operation: ")

# Formating error
userChoice = input(" (1) Add two numbers\n (2) Subtract two numbers\n (3) Multiply two numbers \n (4) Divide two numbers\n")

firstNumber = float(input("Type the first number:")) # Cast to float
secondNumber = float(input("Type the second number:")) # Cast float

match int(userChoice): # Wrong cast
    case 1:
        total = firstNumber + secondNumber
        print(f"The addition of {firstNumber} + {secondNumber} is {total}") # Variable spelled incorrectly. 
    case 2:
        total = firstNumber - secondNumber
        print(f"The subtraction of {firstNumber} - {secondNumber} is {total}") # Variable spelled incorrectly. Incorrect operator in text.
    case 3:
        total = firstNumber * secondNumber
        print(f"The multiplication of {firstNumber} * {secondNumber} is {total}") # Variable spelled incorrectly. Incorrect operator in text.
    case 4: 
        total = firstNumber / secondNumber
        print(f"The division of {firstNumber} / {secondNumber} is {total}")  # firsNumber not firstNumber and "+" instead of division
    case _:
        print ("Invalid menu choice")

