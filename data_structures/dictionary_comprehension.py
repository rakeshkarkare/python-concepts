# values = []
# for x in range(5):
#     values.append(x * 2)

values = [x * 2 for x in range(5)]

values = {x * 2 for x in range(5)}
print(values)

values = {x: x * 2 for x in range(5)}
print(values)


# Storing string into dictionary on index basis
sel = "Selenium"
# print(dict(enumerate(sel)))
dict_values = {x: y for x, y in enumerate(sel)}
print(dict_values)
