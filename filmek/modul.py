class Film:
    def __init__(self, id, title, year, genre, director, country, language, duration_min ,rating ,boxoffice_musd):
        self.id = id
        self.title = title
        self.year = year
        self.genre = genre
        self.director = director
        self.country = country
        self.language = language
        self.duration_min = duration_min
        self.rating = rating
        self.boxoffice_musd = boxoffice_musd

    def __str__(self):
        return f"id: {self.id}\n\tTitle: {self.title}\n\tYear: {self.year}\n\tGenre: {self.genre}\n\tDirector: {self.director}\n\tCountry: {self.country}\n\tLanguage: {self.language}\n\tDuration: {self.duration_min} minutes\n\tRating: {self.rating}\n\tBoxoffice: {self.boxoffice_musd}"
