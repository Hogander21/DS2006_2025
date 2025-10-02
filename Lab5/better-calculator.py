
def Addition(firstNumber, secondNumber):
    """
    Adds the numbers together.
    
    Result:
        float:
            Result of two numbers.
    """
    
    return firstNumber + secondNumber

def Subtraction(firstNumber, secondNumber):
    """
    Subtracts the second number to the first.

    Result:
        float:
            Result of subtraction.
    """

    return firstNumber - secondNumber

def Multiplication(firstNumber, secondNumber):
    """
    Multiplies the numbers together.

    Result:
        float:
            Result of multiplication.
    
    """

    return firstNumber * secondNumber

def Division(firstNumber, secondNumber):
    """
    Divides the first number by the second. Returns 0 on a division by 0.
    
    Return:
        float:
            Result of division.
    """

    if secondNumber == 0: 
        return 0
    
    return firstNumber / secondNumber

def FloorDivision(firstNumber, secondNumber):
    """
    Returns floor division of first number divided by second number.

    Return:
        int:
            Result of floor division.
    """

    return int(firstNumber // secondNumber)

def ModulusDivision(firstNumber, secondNumber):
    """
    Returns the modulus of the first number divided by the second.

    Return:
        int:
            Modulus of the division.
    """

    return firstNumber % secondNumber


def GetNumberInputs(integerInputAmount):
    """
    Gets an amount of inputs from the user and sort them into a list.

    Return:
        list:
            float:
                Number Input.
    """
    inputs = []
    for x in range(integerInputAmount):
        i = float(input(f"{x+1}th Input:")) # Cast to float
        inputs.append(i)
    return inputs

def MathOperation(operation, firstNumber, secondNumber):
    """
    Runs the operation provided using the input.
    
    Return:
        float:
            Returns a float of the result of the operation.
    """

    return operation(firstNumber, secondNumber)


print("*** Welcome to Basic Calculator ***")
print("Choose a mathematical operation:")

# Formating error
userChoice = input(" (1) Addition\n (2) Subtraction\n (3) Multiplication\n (4) Division\n (5) Floor Division\n (6) Modulus\n")

match int(userChoice): # Wrong cast
    case 1:
        inputs = GetNumberInputs(2)
        result = MathOperation(Addition, inputs[0], inputs[1])
        print(f"The Addition of {inputs[0]} + {inputs[1]} = {result}")
    case 2:
        inputs = GetNumberInputs(2)
        result = MathOperation(Subtraction, inputs[0], inputs[1])
        print(f"The Subtraction of {inputs[0]} - {inputs[1]} = {result}")
    case 3:
        inputs = GetNumberInputs(2)
        result = MathOperation(Multiplication, inputs[0], inputs[1])
        print(f"The Multiplication of {inputs[0]} * {inputs[1]} = {result}")
    case 4: 
        inputs = GetNumberInputs(2)
        result = MathOperation(Division, inputs[0], inputs[1])
        print(f"The Division of {inputs[0]} / {inputs[1]} = {result}")
    case 5: 
        inputs = GetNumberInputs(2)
        result = MathOperation(FloorDivision, inputs[0], inputs[1])
        print(f"The Floor Division of {inputs[0]} // {inputs[1]} = {result}")
    case 6:
        inputs = GetNumberInputs(2)
        result = MathOperation(ModulusDivision, inputs[0], inputs[1])
        print(f"The Modulus of {inputs[0]} % {inputs[1]} = {result}")
    case _:
        print ("Invalid menu choice")










# print("*** Welcome to Basic Calculator ***")
# print("Choose a mathematical operation:")

# # Formating error
# userChoice = input(" (1) Add two numbers\n (2) Subtract two numbers\n (3) Multiply two numbers\n (4) Divide two numbers\n")

# firstNumber = float(input("Type the first number:")) # Cast to float
# secondNumber = float(input("Type the second number:")) # Cast to float

# match int(userChoice): # Wrong cast
#     case 1:
#         total = firstNumber + secondNumber
#         print(f"The addition of {firstNumber} + {secondNumber} is {total}") 
#         # Variable spelled incorrectly. 
#     case 2:
#         total = firstNumber - secondNumber
#         print(f"The subtraction of {firstNumber} - {secondNumber} is {total}") 
#         # Variable spelled incorrectly. Incorrect operator in text.
#     case 3:
#         total = firstNumber * secondNumber
#         print(f"The multiplication of {firstNumber} * {secondNumber} is {total}") 
#         # Variable spelled incorrectly. Incorrect operator in text.
#     case 4: 
#         try: 
#             total = firstNumber / secondNumber
#             print(f"The division of {firstNumber} / {secondNumber} is {total}")  
#             # firsNumber not firstNumber and "+" instead of division
#         except:
#             print(f"The division of {firstNumber} / {secondNumber} was unresolved.") 
#             # if the user divides by 0
#     case _:
#         print ("Invalid menu choice")

