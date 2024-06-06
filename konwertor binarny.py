cyfry =[ ]
n= int(input("podaj liczbe: "))
liczba=n
while n>0:
     cyfry.append(n%2)
     n=n//2
     cyfry.reverse()

print("Zapis binarny liczby ", liczba, "to: ", end=" ")
     
for cyfra in cyfry:
     print(cyfra, end="")
     