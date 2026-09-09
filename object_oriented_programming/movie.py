class Movie:
    title:str
    language:str
    year:int
    director:str
    genre:str
    def __init__(self,title,language,year,director,genre):
        self.title=title
        self.language=language
        self.year=year
        self.director=director
        self.genre=genre

    def get_movie(self):
        print(self.title,self.language,self.year,self.director,self.genre)

sp_instance=Movie("Spiderman BND","English",2026,"Destin Daniel","Action")


sp_instance.get_movie()