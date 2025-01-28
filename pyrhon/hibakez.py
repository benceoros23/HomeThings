try:
    szam = int(input("Adj meg egy számot: "))
    print("A szám kétszerese:", szam * 2)
except ValueError:
    print("Hiba: nem számot adtál meg!")

try:
    szam2 = int(input("Adj meg egy számot: "))
    print("A szám:", szam)
except ValueError:
    print("Hiba: nem számot adtál meg!")