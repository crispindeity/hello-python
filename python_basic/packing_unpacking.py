a, b = 1, 2
print(a)
print(b)

c = (3, 4)
d, e = c  # c 의 값을 unpacking
print(d)
print(e)

f = d, e  # d, e 의 값을 f에 packing
print(f)


def tuple_func():
    return 1, 2


q, w = tuple_func()
print(q)
print(w)
