import random

lista = []

for x in range(200):
    lista.append(random.randint(1, 100))

lista.sort()
index = 0
while index < len(lista):
    print(f"{index+1}. elem: {lista[index]}")
    index += 1

keresett_szám = int(input("Keresett szám:"))
if keresett_szám in lista:
    print(f"A keresett szám szerepel a listában!")
    for x in lista:
        if x == keresett_szám:
            print("Találat!")
else:
    print(f"A keresett szám NEM szerepel a listában!")