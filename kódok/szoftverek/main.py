from modul import Szoftver

szoftverek = []

with open("szoftverek.csv", "r", encoding="utf-8") as f:
    next(f)
    for sor in f:
        adat = sor.strip().split(",")
        szoftverek.append(Szoftver(adat[0], adat[1], adat[2], adat[3]))
        
#print(szoftverek[0])

for szoftver in szoftverek:
    print(szoftver)