import random

szám = random.randint(-1000, 1000)
print(f"A sorsolt szám: {szám}")

if szám % 2 == 0:
    print("A szám páros!")