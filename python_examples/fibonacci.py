def fibonacci(num):
    if num <= 1:
        return num
    if num == 2:
        return 1
    else:
        return(fibonacci(num-1) + fibonacci(num-2))


for i in range(10):
    print(fibonacci(i))
