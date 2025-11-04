import random

lista = []

for x in range(1000):
    lista.append(random.randint(2000, 5000))

a = int(input("Kérek egy számot: "))

osztható = []

for x in lista:
    if x % a == 0:
        osztható.append(x)

osztható.sort()

print(f"Osztható számok: {osztható}")