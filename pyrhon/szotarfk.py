# Nevek és életkorok mentése fájlba
nevek = {}

while True:
    nev = input("Adj meg egy nevet (vagy írj 'stop'-ot a befejezéshez): ")
    if nev.lower() == "stop":
        break
    eletkor = input(f"Add meg {nev} életkorát: ")
    nevek[nev] = eletkor

# Fájlba írás
with open("nevek.txt", "w") as file:
    for nev, eletkor in nevek.items():
        file.write(f"{nev}:{eletkor}\n")

print("Adatok sikeresen elmentve a 'nevek.txt' fájlba.")
with open("nevek.txt", "r") as file:
    tartalom = file.read()
    print("Fájl tartalma:")
    print(tartalom)

# Fájl feldolgozása és életkorok ellenőrzése
try:
    # Fájl megnyitása olvasásra
    with open("nevek.txt", "r") as file:
        sorok = file.readlines()
    
    # 18 évnél idősebbek számlálása
    tizennyolc_felett = 0

    for sor in sorok:
        # Név és életkor szétválasztása
        nev, eletkor = sor.strip().split(":")
        eletkor = int(eletkor)  # Életkor számmá alakítása

        # Feltétel ellenőrzése
        if eletkor > 18:
            tizennyolc_felett += 1

    # Eredmény kiírása
    print(f"{tizennyolc_felett} személy van, akinek az életkora 18 felett van.")

except FileNotFoundError:
    print("A 'nevek.txt' fájl nem található!")
except ValueError:
    print("Hiba történt az adatok feldolgozása közben!")

