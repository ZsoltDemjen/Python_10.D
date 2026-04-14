from modul import Zene

zenek = []

with open("zene.csv", "r", encoding="utf-8") as f:
    next(f)
    for sor in f:
        adat = sor.strip().split(",")
        zenek.append(Zene(adat[0], adat[1], adat[2], adat[3], adat[4], adat[5], adat[6], adat[7], adat[8], adat[9]))

print(zenek[0])