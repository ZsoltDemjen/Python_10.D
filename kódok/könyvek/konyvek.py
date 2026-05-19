from osztaly import Konyv

konyvek = []

with open("konyvek.csv", "r", encoding="utf-8") as f:
    next(f)

    for sor in f:
        adat = sor.strip().split(",")

        konyvek.append(Konyv(adat[0], adat[1], adat[2], adat[3], adat[4]))

print(konyvek[0])

cimlista = []

for elem in konyvek:
    cimlista.append(elem.cim)

print(*cimlista, sep=", ")

atlag_oldal = []

for oldal in konyvek:
    atlag_oldal.append(oldal.oldalszam)

db = len(atlag_oldal)
osszoldal = sum(atlag_oldal)
print(f"Átlag oldalszám: {osszoldal / db}")