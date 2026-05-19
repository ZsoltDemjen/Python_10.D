szoveg = str('''A közönséges pörölycápa (Sphyrna zygaena) a porcos halak (Chondrichthyes) osztályának kékcápaalakúak (Carcharhiniformes) rendjébe, ezen belül a pörölycápafélék (Sphyrnidae) családjába tartozó faj, amely egyben e porcoshal-nem típusfaja is.

Az angol nyelvben ezt a cápát sima pörölycápának („smooth hammerhead”) nevezik, mivel más fajoktól ellentétben, a „kalapácsfej” elülső részén nincs semmiféle dudor vagy egyéb kiemelkedés, tehát a felülete sima. Közeli rokonától, a nagy pörölycápától (Sphyrna mokarran) eltérően a közönséges pörölycápa szemeit tartó „kalapácsfej” szélei kissé hátrahajolnak. Más pörölycápáktól eltérően inkább a mérsékelt övi szélességi körökön levő tengervizeket választja élőhelyéül, világszerte megtalálható e szélességi körök környékén. Nyáron a hűvösebb víztömegeket követve a pólusok felé vándorol. Ekkortájt több száz, vagy akár több ezer fős rajokba verődik össze.

A nagy pörölycápa mögött az ötméteres hosszával a második legnagyobb pörölycápafaj. Ragadozó lévén számos élőlény szerepel az étlapján, köztük csontos halak és tengeri gerinctelenek; a nagyobb példányok rájákat és más cápafajokat is zsákmányolnak. Mint minden pörölycápa, ez a faj is elevenszülő, és egy vemhesség alatt 20–40 utódja jöhet a világra. Amint a magyar neve is mutatja, ez a cápafaj közönséges, azaz gyakori, emiatt az elterjedési területén ipari mértékű halászata folyik. Szándékosan és mellékfogásként is belekerülhet a halászhálókba, hiszen akár a többi cápafajt, elsősorban az uszonyaiért halásszák. A jelentős gazdasági érdek abból ered, hogy az ázsiai konyhákban kedvelt fogás a cápauszonyleves.

Mérete és éles fogai miatt veszélyt jelent az ember számára, de csak néhány cápatámadásért felelős. Ennek fő oka, hogy a nembeli társaitól eltérően a hidegebb vizek lakója, ezért kevésbé valószínű, hogy a fürdőzők ezzel a pörölycápafajjal találkozzanak. A Természetvédelmi Világszövetség (IUCN) sebezhető fajként tartja számon.''')


szoveg = szoveg.lower()

lista = szoveg.strip().split("\n")

print(len(lista))


speci_karakterek = [".", "!", "?", "-", "_", ",", "(", ")","„", "”","[", "]"]

for jel in speci_karakterek:
    szoveg = szoveg.replace(jel," ")


szavak = szoveg.strip().split()
print(len(szavak))

szavak2 = []
for szo in szavak:
    if szo != "a" or szo != "az" or szo != "e" or szo != "ez":
        szavak2.append(szo)

print(len(szavak2))