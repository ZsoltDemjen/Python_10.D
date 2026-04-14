with open("forras.txt", "r", encoding="utf-8") as fajl:
    szoveg = fajl.read()

sk = ["(", ")", "[", "]", ".", ",", ":", "„", "”"]
for jel in sk:
    szoveg = szoveg.replace(jel, " ")

szoveg = szoveg.lower()

szoveglista = szoveg.split()

'''print(szoveg)
for elem in szoveglista:
    print(elem)'''

#"a" betűs szavak

a_betus_szavak = []
for szo in szoveglista:
    if szo[0] == "a" and not szo in a_betus_szavak:
        a_betus_szavak.append(szo)

'''print(*a_betus_szavak, sep=" / ")'''

#b,c,d betűs szavak

bcd_betus_szavak = []

for szo in szoveglista:
    if szo[0] == "b" or szo[0] == "c" or szo[0] == "d" and not szo in bcd_betus_szavak:
        bcd_betus_szavak.append(szo)

'''print(" // ** // ")
print(*bcd_betus_szavak, sep=" / ")
print(" // ** // ")
print(f"'A' betűs szavak: {len(a_betus_szavak)}")
print(" // ** // ")
print(f"'B' 'C' 'D' betűs szavak: {len(bcd_betus_szavak)}")'''

# 5 karakternél rövidebb szavak

otnel_rovidebb_szavak = []
for szo in szoveglista:
    if len(szo) < 5 and not szo in otnel_rovidebb_szavak:
        otnel_rovidebb_szavak.append(szo)

'''print(" // ** // ")
print(*otnel_rovidebb_szavak, sep=" / ")
print(" // ** // ")
print(f"Öt karakternél rövidebb szavak: {len(otnel_rovidebb_szavak)}")'''

#számold meg, hogy a szövegben hány mondat van

with open("forras.txt", "r", encoding="utf-8") as f:
    szoveg2 = f.read()

sk2 = ["(", ")", "[", "]", ",", ":", "„", "”"]
for jel2 in sk2:
    szoveg2 = szoveg2.replace(jel2, " ")

szoveg2 = szoveg2.lower()

szoveglista2 = szoveg2.split(".")

for elem2 in szoveglista2:
    print(elem2)