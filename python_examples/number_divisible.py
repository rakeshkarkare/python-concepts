# List all numbers divisible by 3, 9 and 12 using nested "if" with list comprehension
mylist4 = [i for i in range(200) if i % 3 == 0 if i % 9 == 0 if i % 12 == 0]
print(mylist4)
