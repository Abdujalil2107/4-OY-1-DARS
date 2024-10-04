a = int(input("A:"))
b = int(input("B:"))
c = int(input("C:"))
if a>b and b>c or c>b and b>a:
    sum = b
else:
    if a>c and c>b or b>c and c>a:
        sum = c
    else:
        if b>a and a>c or c>a and a>b:
            sum = a
    
print(f"|| Natija = {sum} | A,B,C = {a},{b},{c} ||")