szam = int(input("Kérek egy számot: "))

if szam % 2 == 0:
    print("A szám páros!")
else:
    print("A szám páratlan!")

'''
if szam % 3 == 0:
    print("A szám osztható 3-mal!")
elif szam % 5 == 0:
    print("A szám osztható 5-tel!")
elif szam % 7 == 0:
    print("A szám osztható 7-tel!")
elif szam % 9 == 0:
    print("A szám osztható 9-cel!")
else:
    print("A szám egyikkel sem osztható!")
!!!HELYTELEN!!!!    
'''

if szam % 5 == 0 and szam % 10 == 0:
    print("A szám osztható 5-tel és 10-zel!")
elif szam % 5 == 0:
    print("A szám csak 5-tel osztható!")
elif szam % 10 == 0:
    print("A szám csak 10-zel osztható!")
else:
    print("A szám nem osztható egyikkel se!")

if szam % 9 != 0:
    print("A szám nem osztható 9-cel!")