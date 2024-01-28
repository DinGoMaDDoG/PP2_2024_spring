thistuple = ("apple", "banana", "cherry")
y = ("orange",)
thistuple += y

print(thistuple)


thistuple2 = ("apple", "banana", "cherry")
y2 = list(thistuple2)
y2.remove("apple")
thistuple2 = tuple(y2)