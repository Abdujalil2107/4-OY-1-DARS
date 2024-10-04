a = int(input("A:"))
b = int(input("B:"))
sum = 0
if a>b:
    sum = 1
else:
    sum = 2
if sum==1:
    print(f"|| Natija = A:{a}, B:{b} | A,B = {a},{b} ||")
else:
    print(f"|| Natija = B:{b}, A:{a} | A,B = {a},{b} ||")