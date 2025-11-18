import random
 
def sorsolás() -> int:
    lista = []
    for _ in range(5):
        lista.append(random.randint(1, 99))
    lista.sort()
    return lista

ötöslottó_számok = sorsolás()

print(f"ötöslottó számok: {ötöslottó_számok}")

for x in range(52):
    ötöslottó_számok = sorsolás()
    print(f"{x + 1}. heti nyerőszámai: {ötöslottó_számok}")