import random
számlista = []

for x in range(1000):
    számlista.append(random.randint(1, 5000))

with open('számok.txt', 'w') as célfájl:
    print(f"Lista elemei: {számlista}", file=célfájl)
    print(f"A fájl elkészült!")