a = int(input("A:"))
b = int(input("B:"))
c = int(input("C:"))
if a>b and b>c or b>a and a>c:
    sum = c
    if a>b:
        summ = a
    else:
        summ = b
else:
    if a>c and c>b or c>a and a>b:
        sum = b
        if a>c:
            summ = a
        else:
            summ = c
    else:
        if b>c and c>a or c>b and b>a:
            sum = a
            if b>c:
                summ = b
            else:
                summ = c
print(f"|| Natija = {sum},{summ} | A,B,C = {a},{b},{c} ||")