import random
számlista = []

for x in range(2500):
    számlista.append(random.randint(0, 500))

print(f"Elemek: {számlista}")

print(f"Lista hossza: {len(számlista)}\n"
      f"legkisebb eleme : {min(számlista)}\n"
      f"Legnagyobb eleme: {max(számlista)}\n"
      f"Első elem: {számlista[0]}\n"
      f"Utolsó elem: {számlista[len(számlista)-1]}\n"
      f"Lista elemeinek összege: {sum(számlista)}")

páros = []
páratlan = []

for x in számlista:
    if x % 2 == 0:
        páros.append(x)
    else:
        páratlan.append(x)

print(f"Páros számok: {páros}\n"
      f"-   -   -\n"
      f"Páratlan számok: {páratlan}")