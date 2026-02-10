with open("import.txt", "r", encoding="utf-8") as forrásfájl:
    tartalom = forrásfájl.read()

speckar = [",", ".", "!", "?", "\n", ";", ":", "[", "]", "(", ")", "{", "}", "-"]
for karakter in speckar:
    if karakter in tartalom:
        tartalom = tartalom.replace(karakter, " ")

tartalom = tartalom.lower()

tartalomlista = tartalom.split()

'''for szó in tartalomlista:
    print(szó)'''

#print(*tartalomlista, sep=' - ')

a_betűs_szavak = []
for szó in tartalomlista:
    if szó[0] == "a" and len(szó) > 2:
        a_betűs_szavak.append(szó)

#print(f"A betűs szavak listája: {a_betűs_szavak}")

with open ("export.txt", "w", encoding="utf-8") as kimenet:
    print(*a_betűs_szavak, sep=";", file=kimenet)
    print("Az exportálás elkészült!")

'''with open("export.txt", "r", encoding="utf-8") as importfájl:
    tartalom = importfájl.read()'''

