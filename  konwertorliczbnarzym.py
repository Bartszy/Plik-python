n=int(input("Podaj liczbe nie wieksza niz 3999: "))
def romansystem(n):
    if n < 0:
        return "liczb ujemnych nie uwzgledniamy !"
 
    num = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
    sym = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
    
    romanliczba = ""
    obecnaliczba = n
    pos = 0
    
    while obecnaliczba > 0:
        if obecnaliczba - num[pos] >= 0:
            romanliczba += sym[pos]
            obecnaliczba -= num[pos]
        else:
            pos += 1
            
    return romanliczba
 
rn = romansystem(n)
print(rn)
print("wszystko skonczone")