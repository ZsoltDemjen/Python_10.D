class Szemelyek:
    def __init__(self, nev, szulhely, szuldatum, email, telefonszam, iranyitoszam, varos, utca, hazszam, nem, allampolgarsag ,szemelyi_azonosito ,anyja_neve):
        self.nev = nev
        self.szulhely = szulhely
        self.szuldatum = szuldatum
        self.email = email
        self.telefonszam = telefonszam
        self.iranyitoszam = iranyitoszam
        self.varos = varos
        self.utca = utca
        self.hazszam = hazszam
        self.nem = nem
        self.allampolgarsag = allampolgarsag
        self.szemelyi_azonosito = szemelyi_azonosito
        self.anyja_neve = anyja_neve

    def __str__(self):
        return f"{self.nev}\n\t{self.szulhely}\n\t{self.szuldatum}\n\t{self.email}\n\t{self.telefonszam}\n\t{self.iranyitoszam}\n\t{self.varos}\n\t{self.utca}\n\t{self.hazszam}\n\t{self.nem}\n\t{self.allampolgarsag}\n\t{self.szemelyi_azonosito}\n\t{self.anyja_neve}"