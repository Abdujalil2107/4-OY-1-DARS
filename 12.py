n =int(input("N: "))%1000
# istalgan xonali sonlar uchun ishlaydi !!!
sum = ((n%10)*100)+(((n//100)%10)*10)+((n//10)%10)
print(f"|| Natija = {sum} | N = {n} ||")