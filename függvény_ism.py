def össz(a: int, b: int) -> int:
    eredmény = a + b
    return eredmény

print(f"A két szám összege: {össz(12, 5)}")


def kulombseg(a: int, b: int) -> int:
    eredmény = a - b
    return eredmény

print(f"A két szám külömbdége: {kulombseg(12, 5)}")


def szorzat(a: int, b: int) -> int:
    eredmény = a * b
    return eredmény

print(f"A két szám szorzata: {szorzat(12, 5)}")


def hanyados(a: int, b: int) -> int:
    eredmény = a / b
    return eredmény

print(f"A két szám hányadosa: {hanyados(12, 5)}")

def ellenőrzés(szám: int):
    if szám % 2 ==0:
        print(f"Szám: {szám} - A szám páros!")
    else:
        print(f"Szám: {szám} - A szám páratlan!")

ellenőrzés(össz(34, 57))