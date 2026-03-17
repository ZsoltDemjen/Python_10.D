class Termék:
    def __init__(self, név, cikkszám, kategória, egységár):
        self.név = str(név)
        self.cikkszám = int(cikkszám)
        self.kategória = str(kategória)
        self.egységár = int(egységár)

    def __str__(self):
        return f"Termék neve: {self.név} ({self.cikkszám})\nKategória: {self.kategória}\nEgységára: {self.egységár}"
