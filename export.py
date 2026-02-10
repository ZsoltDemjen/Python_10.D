import random

számlista = []

for _ in range(2000):
    számlista.append(random.randint(1, 50000))

with open("export_szám.txt", "w", encoding="utf-8") as adatfájl:
    print(*számlista, sep=";", file=adatfájl)
    print("A fájl elkészült!")

