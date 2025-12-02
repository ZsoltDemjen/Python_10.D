with open ('szöveg.txt', 'w', encoding='utf-8') as adatfolyam:
    print(f"Ez egy teszt...", file=adatfolyam)
    print(f"A fájl sikeresen létrehozva!")