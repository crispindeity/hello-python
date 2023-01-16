seasons = ["봄", "여름", "가을", "겨울"]

for season in seasons:
    print(season)

ages = {
    "Tod": 23,
    "Jane": 21,
    "Paul": 44
}

for age_key in ages.keys():
    print(age_key)

for age_value in ages.values():
    print(age_value)

for age in ages.keys():
    print("{}의 나이는 {}입니다." .format(age, ages[age]))

for name, age in ages.items():
    print("{}의 나이는 {}입니다." .format(name, age))
