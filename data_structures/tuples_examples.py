point = (1, 2)
point = 1, 2

# To define tuple we can add trailing comma
# so that python understands it is tuple

point = 1,
print(type(point))

# Empty tuple
point = ()
print(type(point))

point = (1, 2) + (3, 4)
print(point)

# Print multiple tuple
point = (1, 2) * 3
print(point)

# Conversion of list to tuple
point = tuple([1, 2])
print(point)

point = tuple("Hello World")
print(point)

point = (1, 2, 3)
print(point[0:2])
x, y, z = point
if 10 in point:
    print("exists")
