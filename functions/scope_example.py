message = "a"


def greet(name):
    global message
    message = "b"


greet(message)
print(message)
