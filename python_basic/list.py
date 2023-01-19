list1 = [123, 242223, 1234552, 4233]
index = list1.index(123)
print(index)

try:
    list1.index(50)
except Exception as e:
    print(e)

list1.extend([9, 10, 11])
print(list1)

list1.insert(2, 999)
print(list1)

list1.sort()
print(list1)

list1.reverse()
print(list1)

print(list1.count(0))
