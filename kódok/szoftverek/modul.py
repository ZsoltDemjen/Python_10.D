class Szoftver:
    def __init__(self, nev, verzio, meret_mb, kategoria):
        self.nev = nev
        self.verzio = verzio
        self.meret_mb = meret_mb
        self.kategoria = kategoria
        self.ar = 0

    def __str__(self):
        return f"{self.nev}\n\tVerzió: {self.verzio}\n\tMéret: {self.meret_mb}MB\n\tKategória: {self.kategoria}\n\tÁr: {self.ar}"