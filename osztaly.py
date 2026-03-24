class Tanulo:
    def __init__(self, nev, szulhely):
        self.nev = nev
        self.szulhely = szulhely

    def __str__(self):
        return f"{self.nev}, született: {self.szulhely}"