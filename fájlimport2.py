with open("forras2.txt", "r", encoding="UTF-8") as fajl:
    szoveg = fajl.read()

elvalasztok = [",", ".", "!", "?", "\n", ";", ":", "[", "]", "(", ")", "{", "}"]

for jel in elvalasztok:
    szoveg = szoveg.replace(jel, " ")

szoveg = szoveg.lower()

szavak = szoveg.split()

for szó in szavak:
    print(szó)

print("Szavak száma:", len(szavak))

tisztított = []
for szó in szavak:
    if szó != "":
        tisztított.append(szó)

szavak = tisztított

gergő_hányszor = []

for szó in szavak:
    if szó == "gergő":
        db += 1

g_betűs_szavak = []

for szó in szavak:
    if szó[0] == "a":
        g_betűs_szavak.append(szó)

g_betűs_szavak.sort()
print(g_betűs_szavak)

with open("kimenet.txt", "w", sep=";", encoding="UTF-8") as célfájl:
    print(*g_betűs_szavak, file=célfájl)