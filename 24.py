a = float(input("A:"))
b = float(input("B:"))
sum = 0
if a>b:
    sum = a
    a = b
    b = sum
print(f"|| Natija = A:{a}, B:{b} | A,B = {sum},{a} ||")