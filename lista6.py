import random
számlista = []

for x in range(1000):
    számlista.append(random.randint(0, 1000))

számlista.sort()

print(számlista)

keresett_elem = int(input("Melyik elemet keressem? "))

if keresett_elem in számlista:
    print("Az elem legalább egyszer szerepel!")
    hányszor = 0
    for x in számlista:
        if keresett_elem == x:
            hányszor += 1
    print(f"Találat(ok): {hányszor}")
else:
    print("Az elem nem található!")

if keresett_elem in számlista:
    szám = 1
    while szám <= hányszor:
        számlista.remove(keresett_elem)
        hányszor -= 1

print(számlista)