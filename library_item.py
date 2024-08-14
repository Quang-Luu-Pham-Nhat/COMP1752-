class LibraryItem:
    def __init__(self, key, name, director, rating=0, play_count=0):
        self.key = key
        self.name = name
        self.director = director
        self.rating = rating
        self.play_count = play_count

    def info(self):
        return f"{self.name} - {self.director} {self.stars()}"

    def stars(self):
        stars = ""
        for i in range(self.rating):
            stars += "*"
        return stars
