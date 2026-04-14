class Zene:
    def __init__(self, title, artist, album, year, genre, length_sec, country, popularity, bpm, language):
        self.title = title
        self.artist = artist
        self.album = album
        self.year = year
        self.genre = genre
        self.length_sec = length_sec
        self.country = country
        self.popularity = popularity
        self.bpm = bpm
        self.language = language

    def __str__(self):
        return f"Title: {self.title}\n\tArtist: {self.artist}\n\tAlbum: {self.album}\n\tYear: {self.year}\n\tGenre: {self.genre}\n\tLength: {self.length_sec} sec\n\tCountry: {self.country}\n\tPopularity: {self.popularity}\n\tBPM: {self.bpm}\n\tLanguage: {self.language}"