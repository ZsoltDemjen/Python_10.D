import random

def össz(a: int, b: int) -> float:
    return a + b 

def össz2(a:int, b:int) -> float:
    print(f"A két szám összege: {a + b}")

print(össz(5, 12))
össz2(5,12)

def osztható(szám:int) -> str:
    if szám %3 ==  0:
        return "Igen, a szám osztható 3-mmal" 
    else:
        return "Nem osztható 3-mmal"
    
print(osztható(5))
        
def genlista(tol:int, ig:int, db=100) -> list:
    lista = []
    for _ in range(db):
        lista.append(random.randint(tol, ig))
    return lista

számlista = genlista(1, 500)

for x in számlista:
    print(x)