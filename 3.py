a =int(input("A: "))
b =int(input("B: "))
c =int(input("C: "))

print(f"A: {a} B: {b} C:{c}",end="\t")

temp = a
a = c
c = b
b = temp

print(f"A: {a} B: {b} C:{c}")