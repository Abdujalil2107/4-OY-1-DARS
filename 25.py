a = int(input("A:"))
b = int(input("B:"))
c=a
d=b
if a!=b:
    a+=b
    b=a
else:
    a=0
    b=a
print(f"|| Natija = A:{a}, B:{b} | A,B = {c},{d} ||")