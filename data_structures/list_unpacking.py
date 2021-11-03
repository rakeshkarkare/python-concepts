numbers = [1, 2, 3]
first, second, third = numbers

# first = numbers[0]
# second = numbers[1]
# third = numbers[2]

numbers = [1, 2, 3, 4, 4, 4, 4, 9]
first, second, *other = numbers
first, *other, last = numbers
print(first)
print(other)
print(first, last)
