from modul import Szemelyek

szemelyek = []

with open("szemelyek_bov.csv", "r", encoding="utf-8") as f:
    next(f)
    for sor in f:
        adat = sor.strip().split(",")
        szemelyek.append(Szemelyek(adat[0], adat[1], adat[2], adat[3], adat[4], adat[5], adat[6], adat[7], adat[8], adat[9], adat[10], adat[11], adat[12]))

print(szemelyek[0])