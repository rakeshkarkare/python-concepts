point = {"x": 1, "y": 2}
point = dict(x=1, y=2)

point["x"] = 10
point["z"] = 20

# To check existent of key in dictionary
if "a" in point:
    print(point["a"])

# To check existent of key in dictionary we can use
# get method which will return none by default
print(point.get("a"))

# To check existent of key in dictionary we can use
# get method which will return none by default but
#  we can pass default value to it
print(point.get("a", 0))

del point["x"]
print(point)

# How to loop dict
for key in point:
    print(key, point[key])


for key, value in point.items():
    print(key, value)
