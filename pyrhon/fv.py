# Függvény, ami összead két számot
def osszead(a, b):
    return a + b

def kerulet_terulet(szelesseg, magassag):
    kerulet = 2 * (szelesseg + magassag)
    terulet = szelesseg * magassag
    return kerulet, terulet
# Függvény használata
eredmeny = osszead(3, 5)
print("Az eredmény:", eredmeny)
print("--------------------")
szelesseg = 4
magassag = 7
kerulet, terulet = kerulet_terulet(szelesseg, magassag)
print(f"A téglalap kerülete: {kerulet}")
print(f"A téglalap területe: {terulet}")