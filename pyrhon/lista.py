# Lista létrehozása
gyumolcsok = ["alma", "banán", "cseresznye"]

# Lista elemeinek elérése
print("Első gyümölcs:", gyumolcsok[0])  # Indexelés 0-tól kezdődik

# Új elem hozzáadása
gyumolcsok.append("narancs")
print("Gyümölcsök listája:", gyumolcsok)

# Lista hosszának lekérdezése
print("Hány gyümölcs van a listában?", len(gyumolcsok))

print("-------------------")
# Városok listájának létrehozása
varosok = ["Budapest", "Debrecen", "Szeged", "Pécs", "Győr"]

# Városok listájának kiírása
print("Városok listája:", varosok)

# Új város hozzáadása
varosok.append("Miskolc")

# Városok listájának kiírása az új várossal
print("Városok listája az új várossal:", varosok)

# Lista hosszának lekérdezése
print("Hány város van a listában?", len(varosok))