n =int(input("N: "))%1000
# istalgan xonali sonlar uchun ishlaydi !!!
sum = ((n//100)%10)+((n//10)%10)+(n%10)
print(f"|| Yig'indi = {sum} | N = {n} ||")