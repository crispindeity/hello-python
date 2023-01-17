list = [1, 2, 3, 4, 5]

for i, v in enumerate(list):
    print("{}번째 값: {}".format(i, v))

for n in enumerate(list):
    print("{}번째 값: {}".format(n[0], n[1]))

for n in enumerate(list):
    print("{}번째 값: {}".format(*n))

ages = {
    "Tod": 35,
    "Jane": 23,
    "Paul": 66
}

for key, value in ages.items():
    print("{}의 나이는: {}".format(key, value))

for n in ages.items():
    print("{}의 나이는: {}".format(n[0], n[1]))

for n in ages.items():
    print("{}의 나이는: {}".format(*n))
