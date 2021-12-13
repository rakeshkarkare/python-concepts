def add1(*args):
    return sum(args)


print(add1(1, 2, 4))
print(add1(1, 2, 4, 5))
print(add1(1, 2, 6))

list1 = [2, 6, 7, 7]
tuple1 = (2, 6, 7, 7, 6)
print(add1(*list1))
print(add1(*tuple1))
