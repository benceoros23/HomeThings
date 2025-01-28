# Egyszerű feltétel
szam = int(input("Adj meg egy számot: "))
if szam > 0:
    print("Pozitív szám")
elif szam < 0:
    print("Negatív szám")
else:
    print("A szám nulla")
print()
age = int(input("Adja meg az életkorát: "))
if age>=18:
    print("Remélem már nem anyádékkal laksz")
else:
    print("Fogadjunk még anyád törli a segged")
print()
szamm = int(input("Adj meg egy számot: "))
if szamm%2==0:
    print("páros")
else:
    print("páratlan")
