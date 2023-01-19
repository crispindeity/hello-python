numbers = list(range(10))
del numbers[:5]
print(numbers)
numbers[1:3] = [77, 88]
print(numbers)
numbers[1:3] = [77, 88, 99]
print(numbers)
numbers[1:4] = [8]
print(numbers)
