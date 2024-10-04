a =int(input("A: "))
b =int(input("B: "))

print(f"A: {a} B: {b}",end="\t")

c = a
a = b
b = c

print(f"A: {a} B: {b}")