import random

def generál(tol:int, ig:int, db=int(100)) -> list:
    lista = []
    for x in range(db):
        lista.append(random.randint(tol, ig))
        return lista

számlista = generál(1, 6000, 5000)

with open('számok.txt', 'w') as célfájl:
    print(f"Lista elemei: {számlista}", file=célfájl)
    print(f"A fájl elkészült!")