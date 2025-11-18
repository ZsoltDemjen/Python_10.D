import random
import math
import csv

def összeg(a: int, b: int) -> int:
    return a + b

def összeg2(a: int, b: int) -> int:
    össz = a + b
    return össz

def összeg3(a: int, b: int, c = int(100)) -> int:
    print(f"Összeg: {a + b + c}")

def összeg4(a: int, b: int, c = int(100), d = int(200)) -> int:
    print(f"Összeg {a+b+c+d}")

'''
print(f"Összeg első megoldás: {összeg(584, 927)}")
print(f"Összeg második megoldás: {összeg2(584, 927)}")
összeg3(34, 76, 200)'''

a = int(input("Kérem az (a) számot: "))
b = int(input("Kérem a (b) számot: "))
c = int(input("Kérem az (c) számot: "))
d = int(input("Kérem a (d) számot: "))
összeg4(a, b)