numbers_list = [1, 2, 3, 4, 5]
numbers_dict = {
    "one": 1,
    "two": 2
}

print(len(numbers_dict))
print(len(numbers_list))

print(2 in numbers_list)
print("one" in numbers_dict.keys())
print(2 in numbers_dict.values())
print(32 in numbers_dict.values())
