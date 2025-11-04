szám_1 = int(input("kérem az első számot: "))
szám_2 = int(input("kérem a második számot: "))
szám_3 = int(input("kérem a harmadik számot: "))
szám_4 = int(input("kérem a negyedik számot: "))

szorzat = szám_1 * szám_2 * szám_3 * szám_4
hányados = szám_1 / szám_2 / szám_3 / szám_4
maradék = szám_1 % szám_2 % szám_3 % szám_4
egyenlet = szám_1 * szám_2 / (szám_3 + szám_4)+(szám_1*szám_3)-(szám_2 /szám_1)

print(f"Szorzat: {szorzat}\n"
      f"Hányados: {hányados:.2f}\n"
      f"Maradék: {maradék}\n"
      f"Egyenlet eredménye: {egyenlet}")