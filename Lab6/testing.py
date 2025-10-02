lastNumber = 2.0
numbers = [5.0,7.0]
result = []
for number in numbers:
	math = number % lastNumber
	result.append(math)
print(result)