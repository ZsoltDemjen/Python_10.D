import random
lista = []

for x in range(100):
    lista.append(random.randint(0, 1000))

print(f"Elemek: {lista}")

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

hárommal.sort(reverse=True)
öttel.sort(reverse=True)
héttel.sort(reverse=True)
kilenccel.sort(reverse=True)
tízzel.sort(reverse=True)

print(f"Hárommal osztható: {hárommal}\n"
      f"-   -   -\n"
      f"Öttel osztható: {öttel}\n"
      f"-   -   -\n"
      f"Héttel osztható: {héttel}\n"
      f"-   -   -\n"
      f"Kilenccel osztható: {kilenccel}\n"
      f"-   -   -\n"
      f"Tízzel osztható: {tízzel}")