try:
    with open("app.py") as file:
        print("File opened.")
except FileNotFoundError:
    print("File not found.")
