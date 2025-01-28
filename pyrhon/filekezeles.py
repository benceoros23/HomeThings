# Fájl írása
with open("pelda.txt", "w") as file:
    file.write("Ez egy példa szöveg.")

# Fájl olvasása
with open("pelda.txt", "r") as file:
    tartalom = file.read()
    print("Fájl tartalma:", tartalom)

    # Napló fájl létrehozása és írása
    with open("naplo.txt", "w") as naplo_file:
        szoveg = input("Kérem, írjon be egy szöveget a naplóhoz: ")
        naplo_file.write(szoveg)

    # Napló fájl olvasása
    with open("naplo.txt", "r") as naplo_file:
        naplo_tartalom = naplo_file.read()
        print("Napló fájl tartalma:", naplo_tartalom)