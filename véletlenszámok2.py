import random

hős_életerő = 1000
ellenfél_életerő = 500

hős_ütéspont = random.randint(0, 300)
ellenfél_ütéspont = random.randint(0, 300)

print(f"Hős életereje: {hős_életerő}\n"
      f"ellenfél életereje: {ellenfél_életerő}\n"
      f"Hős ütéspontja: {hős_ütéspont}\n"
      f"ellenfél ütéspontja: {ellenfél_ütéspont}\n\n")

print(f"Ütés utáni életerő")

if hős_ütéspont > ellenfél_ütéspont:
    ellenfél_életerő -= hős_ütéspont
    print(f"Ellenfél életerő: {ellenfél_életerő}")
elif hős_ütéspont < ellenfél_ütéspont:
    hős_életerő -= ellenfél_ütéspont
    print(f"Hős életerő: {hős_életerő}")
elif 140 < hős_ütéspont <= 160:
    print("Az ellenfél védekezett!")