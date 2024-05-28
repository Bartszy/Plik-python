from random import randrange

def ruch(numer):
    match numer:
        case 1: return "Kamień"
        case 2: return "Papier"
        case 3: return "Nożyce"

punktyGracz, punktyKomputer = 0,0
wygrana = False

print("Gra w kamień, papier, nożyce")

while not wygrana:

    print("1. Kamień\n2. Papier\n3. Nożyce")
    powtorz=True
    while powtorz:

        dane = input("Twój wybór to: ")

        if dane.isdigit():
            wyborGracz = int(dane)
            if wyborGracz>=1 and wyborGracz<=3:
                wyborKomputer = randrange(1,3)
                print(f"Przeciwnik wybrał {ruch(wyborKomputer)} a gracz wybrał {ruch(wyborGracz)}")
                powtorz=False
                oblicz = wyborGracz-wyborKomputer
                if oblicz==-2 or oblicz>0:
                    punktyGracz += 1
                    print("GRACZ WYGRYWA RUNDĘ")
                    print(f"{punktyGracz} - {punktyKomputer}")
                elif wyborKomputer==wyborGracz:
                    print("REMIS")
                    print(f"{punktyGracz} - {punktyKomputer}")
                else:
                    punktyKomputer += 1
                    print("KOMPUTER WYGRYWA RUNDĘ")
                    print(f"{punktyGracz} - {punktyKomputer}")
                
                if punktyGracz==3 or punktyKomputer==3:
                    wygrana = True
                    print(f"GRA ZAKOŃCZONA WYNIKIEM {punktyGracz} - {punktyKomputer}")
            else:
                print("Liczba musi być z przedziału od 1 do 3!")
                powtorz = True
        else:
            print("Wprowadź wartość, która jest liczbą!")
            powtorz = True  



      























