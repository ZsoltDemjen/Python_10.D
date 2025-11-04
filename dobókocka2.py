import random

játékos_1 = random.randint(1, 6)
játékos_2 = random.randint(1, 6)

print(f"Első játékos dobása: {játékos_1}")
print(f"Második játékos dobása: {játékos_2}")

if játékos_1 > játékos_2:
    print("Első játékos nyert!")
elif játékos_1 < játékos_2:
    print("Második játékos nyert!")
elif játékos_1 == játékos_2:
    print("Döntetlen!")