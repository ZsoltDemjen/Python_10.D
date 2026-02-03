with open("forras3.txt", "r", encoding="UTF-8") as fajl:
    szoveg = fajl.read()

elvalasztok = [",", ".", "!", "?", "\n", ";", ":", "[", "]", "(", ")", "{", "}"]

for jel in elvalasztok:
    szoveg = szoveg.replace(jel, " ")

szoveg = szoveg.lower()

szavak = szoveg.split()

for szó in szavak:
    print(szó)

print("Szavak száma:", len(szavak))

tisztitott = []
for szó in szavak:
    if szó != "":
        tisztitott.append(szó)

szavak = tisztitott

a_betűs_szavak = []

for szó in szavak:
    if szó[0] == "a":
        a_betűs_szavak.append(szó)

a_betűs_szavak.sort()
print(a_betűs_szavak)

with open("kimenet.txt", "w", sep=";", encoding="UTF-8") as célfájl:
    print(*a_betűs_szavak, file=célfájl)

    űrhajó_hányszor = []

    for szó in szavak:
        if szó == "űrhajó":
            db += 1

