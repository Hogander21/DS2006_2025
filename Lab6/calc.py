def Addition(numbers):
    """
    Adds the numbers together.
    
    Result:
        float:
            Result of adding all the numbers together
    """
    result = 0
    for number in numbers:
        result += number

    return result

def Subtraction(numbers):
    """
    Subtracts all the numbers from the first one.

    Result:
        float:
            Result of subtraction.
    """
    result = numbers[0]
    for number in range(1,len(numbers)):
        result -= numbers[number]

    return result

def Multiplication(numbers):
    """
    Multiplies the numbers together.

    Result:
        float:
            Result of multiplication.
    
    """
    result = 1
    for number in numbers:
        result *= number

    return result

def Division(numbers):
    """
    Divides the numbers by the last number. Returns 0 on a division by 0.
    
    Return:
        List:
            Floats:
                Number divided by second number.
    """

    lastNumber = numbers[len(numbers)-1]
    numbers.pop(len(numbers)-1)
    result = []
    for number in numbers:
        if lastNumber == 0:
            result.append(0)
        else:
            result.append(number/lastNumber) 
    return result

def HalfNumbers(numbers):
    """
    Divides the numbers by 2.
    
    Return:
        List:
            Floats:
                Number divided by second number.
    """
    result = []
    for number in numbers:
        result.append(number/2) 
    return result

def FloorDivision(numbers):
    """
    Returns floor division of numbers divided by the last number.

    Return:
        List:
            Floats:
                Number divided by second number.
    """
    lastNumber = numbers[len(numbers)-1]
    numbers.pop(len(numbers)-1)
    result = []

    for number in numbers:
        if lastNumber == 0:
            result.append(0)
        else:
            result.append(number//lastNumber) 
    return result

def ModulusDivision(numbers):
    """
    Returns the modulus of the numbers divided by the last number.

    Return:
        List:
            Floats:
                Number divided by second number.
    """
    lastNumber = numbers[len(numbers)-1]
    numbers.pop(len(numbers)-1)
    result = []

    for number in numbers:
        if lastNumber == 0:
            result.append(0)
        else:
            result.append((number%lastNumber)) 
    return result


def GetNumberInputs():
    """
    Gets an amount of inputs from the user and sort them into a list.

    Return:
        list:
            float:
                Number Input.
    """
    integerInputAmount = int(input("How many numbers? (min 2) "))
    if integerInputAmount < 2:
        integerInputAmount = 2

    inputs = []
    for x in range(integerInputAmount):
        i = float(input(f"{x+1}th Input:")) # Cast to float
        inputs.append(i)
    return inputs

def MathOperation(operation, numbers):
    """
    Runs the operation provided using the input.
    
    Return:
        float:
            Returns a float of the result of the operation.
    """

    return operation(numbers.copy())

print("*** Welcome to Basic Calculator ***")
print("Choose a mathematical operation:")

# Formating error
userChoice = input(" (1) Addition\n (2) Subtraction\n (3) Multiplication\n (4) Division\n (5) Floor Division\n (6) Modulus\n (7) Half\n")

match int(userChoice): # Wrong cast
    case 1:
        inputs = GetNumberInputs()
        result = MathOperation(Addition, inputs)
        print(f"The Addition of {inputs} = {result}")
    case 2:
        inputs = GetNumberInputs()
        result = MathOperation(Subtraction, inputs)
        print(f"The Subtraction of {inputs} = {result}")
    case 3:
        inputs = GetNumberInputs()
        result = MathOperation(Multiplication, inputs)
        print(f"The Multiplication of {inputs}  = {result}")
    case 4: 
        inputs = GetNumberInputs()
        result = MathOperation(Division, inputs)
        print(f"The Division of {inputs}  = {result}")
    case 5: 
        inputs = GetNumberInputs()
        result = MathOperation(FloorDivision, inputs)
        print(f"The Floor Division of {inputs}  = {result}")
    case 6:
        inputs = GetNumberInputs()
        result = MathOperation(ModulusDivision, inputs)
        print(f"The Modulus of {inputs} = {result}")
    case 7:
        inputs = GetNumberInputs()
        result = MathOperation(HalfNumbers, inputs)
        print(f"The Half of {inputs} / 2 = {result}")
    case _:
        print ("Invalid menu choice")