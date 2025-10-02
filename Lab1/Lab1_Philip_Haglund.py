# Welcome message
print("Welcome to Python Programming!")

# Basic Arithmetic
# Addition
result_addition = 2 + 6
print("The result of the addition is:", result_addition)

# Multiplication
result_multiplication = 5 * 3
print("The result of the multiplication is: ", result_multiplication)

# Print simple message
print("Hello world!")

# Variable assignments 
A = 10 # Assign value 10 to variable A
B = 4 # Assign value 4 to variable B

print("The result of the addition is ", A+B)
print("The result of the multiplication is ", A*B)
print("The result of the division is ", A/B)



# Using variables to store user information
name = "Phil"
age = 21

# Printing user information
print("Hi! My name is", name, "and I am", age, "years old.")
print(f"In 2 years, I will be {age+2} years old.")

# Conditional statement based on age
if age > 30:
    print(f"Access granted. Welcome {name}.")
else:
    print(f"Access refused. Common {name}, you can come back in {30-age} years.")

# List of usernames
usernames = ["Mark", "Sara", "Ahmad", "Johanna"]

# Looping through the list and writing welcome messages
for user in usernames:
    print(f"Welcome {user}")

# Looping to demonstrate range and multiplication
for i in range(0,10):
    print(f"The double of {i} is {2*i}")

# Printing the user's full name
# Replace 'Your Full Name' with your actual name
print("Hello, Data Scientists!")
print("Philip Haglund!")

# Demonstrating input
psuedoname= input("Please enter pseudoname: ")
print("Hello", psuedoname)

# Demonstrate final variable values.
print("The variable A is", A)
print("The variable B is",B)
print("The variable name is", name)
print("The variable age is", age)
print("The variable psuedoname", psuedoname)
print("The variable usernames is", usernames)