from osztaly import Tanulo

tanulok = []

with open("forras.csv", "r", encoding = "utf-8") as f:
    next(f) 

    for sor in f:
        adat = sor.strip().split(",")
        nev = adat[0]
        szulhely = adat[1]

        Tanulo(nev, szulhely)
        tanulok.append(Tanulo(nev, szulhely))

print(tanulok[45].nev)
