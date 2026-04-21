class Konyv:
    def __init__(self, cim, szerzo, isbn, megjelenes_eve, oldalszam):
        self.cim = cim
        self.szerzo = szerzo
        self.isbn = isbn
        self.megjelenes_eve = int(megjelenes_eve)
        self.oldalszam = int(oldalszam)
        self.ar = 0
        self.elerhetoseg = True

    def __str__(self):
        return f"{self.cim}\n\tSzerző: {self.szerzo}\n\t ISBN: {self.isbn}\n\t Megjelenés éve: {self.megjelenes_eve}\n\t Oldalszám: {self.oldalszam}\n\t Ár: {self.ar}\n\t Elérhetőség: {self.elerhetoseg}"