import random

számlista = []

for x in range (5000):
    számlista.append(random.randint(1, 6))

#print(számlista)

hányszor_1 = 0
for x in számlista:
    if x == 1:
        hányszor_1 += 1

print(f"Az egyest ennyiszer dobták: {hányszor_1}")