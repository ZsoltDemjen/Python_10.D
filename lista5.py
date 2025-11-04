import random
számlista = []
hónapok = ["Január", "Február", "Március"]

for x in range(200):
    számlista.append(random.randint(0, 500))

print(f"Elemek: {számlista}")

print(f"Első elem: {számlista[0]}")
print(f"Utolsó elem: {számlista[-1]}")
print(f"23. elem: {számlista[23]}")
print(f"Első 5 elem: {számlista[:5]}")
print(f"5. elemtől felfelé: {számlista[5:]}")
print(f"5. és 12. elem között: {számlista[5:12]}")

számlista.append(3) #elemeket ad a lista végéhez
számlista.pop() #eltávolít elemeket a lista végéről
#számlista.remove() #a listából kiszedi azt a számot, ami a zárójelben van, egyszer fut csak le, ha több van a számból azelsőt szedi csak ki
számlista.insert(1, 67) #az indexre beszúr egy elemet, a többi indexet 1-el növeli
#számlista.clear() #törli a lisra tartalmát
#számlista.count() #egy elem hányszor fordul elő
számlista.sort() #lista növekvőbe rendezése
számlista.sort(reverse=True) # lista cökkenőbe rendezése

#listában található függvények
sum(számlista) # elemek összege
#max(számlista) #a legnagyobb elem
#min(számlista) #a legkisebb elem
len(számlista) #elemek száma

#speciális kiíratás
print(" - " .join(hónapok))

#elem szerepel-e?
elem = 82
if elem in számlista:
    print(f"Az elem szerepel!")
else:
    print("Az elem nem szerepel!")

    #lista bejárásai
    for x in számlista:
        print(x)

index = 0
while index < 100:
    print(f"A {index}. elem: {számlista[index]}")
    index += 1