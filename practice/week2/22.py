#convert tuple into list to change

a=("A", "B", "C", "D")
y=list(a)
y.append("G")
a=tuple(y)
print(a) 