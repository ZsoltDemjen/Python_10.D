lista = [5, 63, 2, 85, 3]

print(f"Lista elemei: {lista}")
print(f"Lista elemeinek száma: {len(lista)}")
print(f"Lista első eleme: {lista[0]}")
print(f"Lista utolsó eleme: {lista[len(lista)-1]}")
print(f"Lista elemeinek összege: {sum(lista)}")
print(f"Lista legkisebb eleme: {min(lista)}")
print(f"Lista legnagyobb eleme: {max(lista)}")

összeg = 0
for x in lista:
    összeg += x

print(f"A lista elemeinek összege: {összeg}")

különbség = lista[0]
for x in lista:
    különbség += x

print(f"A lista elemeinek különbsége: {különbség}")
