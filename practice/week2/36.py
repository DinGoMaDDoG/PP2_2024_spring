car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}

x = car.keys()

print(x) #before the change

car["color"] = "white"

print(x) #after the change

y = car.values()

print(y) #before the change

car["year"] = 2020

print(y) #after the change

z = car.items()
print (z)