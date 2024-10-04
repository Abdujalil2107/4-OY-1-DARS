a = int(input("A:"))
b = int(input("B:"))
c = int(input("C:"))
musbat = 0
manfi = 0
if a>0:
    musbat+=1
else:
    manfi+=1
if b>0:
    musbat+=1
else:
    manfi+=1
if c>0:
    musbat+=1
else:
    manfi+=1
print(f"|| Natija = Musbat:{musbat}, Manfi:{manfi} | A,B,C = {a},{b},{c} ||")