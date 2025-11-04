import random
lista = []

for x in range(1000):
    lista.append(random.randint(0, 5000))

lista.sort(reverse=True)
# print(lista)




index = 0
while index < len(lista):
    print(f"Az elem: {lista[index]}")
    if lista[index] % 2 ==0:
        print(f"A szám páros!")
    else:
        print(f"A szám páratlan!")
    index += 2
    print("/  /  /")
    
keresett_szám = int(input("Keresett szám: "))

index = 0
while index < len(lista):
    if lista[index] == keresett_szám:
        print(f"A {keresett_szám} a(z) {index}. helyen szerepel!")
    index += 2

'''
while index < len(lista):
    print(f"Az elem: {lista[index]}")
    if lista[index] % 2 ==0:
        print(f"A szám páros!")
    else:
        print(f"A szám páratlan!")
    index += 2
    print("/  /  /")
    '''