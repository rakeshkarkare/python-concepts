import keyword


keys = ["for", "while", "tanisha", "break", "sky",
        "elif", "assert", "pulkit", "lambda", "else", "sakshar"]

for i in range(len(keys)):
    if keyword.iskeyword(keys[i]):
        print(keys[i] + " is python keyword")
    else:
        print(keys[i] + " is not a python keyword")
