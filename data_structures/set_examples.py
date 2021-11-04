numbers = [1, 1, 2, 3, 4]
first = set(numbers)
second = {1, 5}

# Union of set using vertical bar
print(first | second)

# Intersection of sets
print(first & second)

# Difference between seys
print(first - second)

# Sematric diffference
print(first ^ second)

if 1 in first:
    print("yes")
