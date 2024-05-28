import random
print('Witaj w świecie wisielca! Podaj nazwę:')
pseudonim = input()
lista= ['sekret','pies','drzewo','polska']
# hasło
haslo = str(lista[random.randint(0,len(lista)-1)])
tablica = list('_' * len(haslo))
 
zycia = 3
 
while zycia > 0:
    print('')
    print(pseudonim, 'pozostało ci', zycia, 'żyć')
    print('')
    print(''.join(tablica))
    print('')
    print('Podaj swoją literę:')
    litera = input()
 
    if litera in haslo:
        for i in range(len(haslo)):
            if haslo[i] == litera:
                tablica[i] = litera
    else:
        zycia -= 1
 
    if '_' not in tablica:
        print('Gratulacje! Odgadłeś hasło:', ''.join(tablica))
        break
else:
    print('Przegrałeś. Prawidłowe hasło to:', haslo)