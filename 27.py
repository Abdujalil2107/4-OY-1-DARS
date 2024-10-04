a = int(input("A:"))
b = int(input("B:"))
c = int(input("C:"))
if a>b and b>c or b>a and a>c:
    sum = c
else:
    if a>c and c>b or c>a and a>b:
        sum = b
    else:
        if b>c and c>a or c>b and b>a:
            sum = a
    
print(f"|| Natija = {sum} | A,B,C = {a},{b},{c} ||")