import random
start= int(input("Start:" ))

koniec = int (input("Koniec: "))

ile  = int(input("Podaj z ilu liczb mamy losowac: "))

if (ile <= 0):
    print("Musisz podac liczbe wieksza od zera ! ")
    quit()
if(koniec - start + 1<ile):
    print("Wybrales zbyt duza liczbe przerasta dostepny zakres !")
    quit()

liczby= random.sample(range(start,koniec+1),ile)

print(liczby)