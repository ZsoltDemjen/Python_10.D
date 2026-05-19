import random

def general(tol:int, ig:int, db:int) -> list:
    lista = []
    for _ in range(db):
        lista.append(random.randint(tol, ig))
    return lista

def osszead(a:int, b:int) -> int:
    return a + b

def kivon(a:int, b:int) -> int:
    return a - b

def szoroz(a:int, b:int) -> int:
    return a * b

def oszt(a:int, b:int) -> int:
    return a / b

tesztlista = general(300, 500, 1000)
print(*tesztlista[:10], sep=" // ")

print(osszead(20, 30))
print(kivon(20, 30))
print(szoroz(20, 30))
print(oszt(20, 30))