# Odd Even Example using List Comprehension
order = [print("{} is even number".format(i)) if i % 2 == 0 else print(
    "{} is odd number".format(i)) for i in range(10)]
