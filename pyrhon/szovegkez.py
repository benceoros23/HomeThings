szoveg = "hello világ"
# Szöveg hossza
print("A szöveg hossza:", len(szoveg))

# Szöveg nagybetűsre alakítása
print("Nagybetűs:", szoveg.upper())
szoveg2=szoveg.upper()
print(szoveg2)
print("Kisbetus:",szoveg2.lower())

# Részszöveg ellenőrzése
if "világ" in szoveg:
    print("A 'világ' szó benne van a szövegben!")
else:
    print("Nincs benne az adott szó")