import random

lista = []

elemszám = int(input("hány szám legyen a listában? "))
minimum = int(input("minimum szám: "))
maximum = int(input("maximum szán: "))

for x in range(elemszám):
    lista.append(random.randint(minimum, maximum))

'''for x in range(30):
    lista.append(random.randint(0, 100))'''

print(f"{lista}")

print(f"Lista hossza: {len(lista)}\n"
      f"Legkisebb eleme: {min(lista)}\n"
      f"Legnagyobb eleme: {max(lista)}\n"
      f"Első elem: {lista[0]}\n"
      f"Utolsó elem: {lista[len(lista)-1]}\n"
      f"Első 7 elem: {lista[:7]}\n"
      f"3-től felfelé az elemek: {lista[3:]}\n"
      f"10. és 25. elem között: {lista[10:25]}\n"
      f"Lista elemeinek összeg: {sum(lista)}")

páros_lista = []
páratlan_lista = []

for x in lista:
    if x % 2 == 0:
        páros_lista.append(x)
    else: 
        páratlan_lista.append(x)

print(f"Páros számok: {páros_lista}\n"
      f"-   -   -\n"
      f"Páratlan számok: {páratlan_lista}\n")

hárommal = []
öttel = []
héttel = []
kilenccel = []
tízzel = []

for x in lista:
    if x % 3 == 0:
        hárommal.append(x)
    if x % 5 == 0:
        öttel.append(x)
    if x % 7 == 0:
        héttel.append(x)
    if x % 9 == 0:
        kilenccel.append(x)
    if x % 10 == 0:
        tízzel.append(x)

print(f"Hárommal osztható: {hárommal}\n"
      f"-   -   -\n"
      f"Öttel osztható: {öttel}\n"
      f"-   -   -\n"
      f"Héttel osztható: {héttel}\n"
      f"-   -   -\n"
      f"Kilenccel osztható: {kilenccel}\n"
      f"-   -   -\n"
      f"Tízzel osztható: {tízzel}")

index = 0
while index < elemszám:
    print(f"A {index}. elem: {lista[index]}")
    index += 1