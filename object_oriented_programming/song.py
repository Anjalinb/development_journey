class Song:
    id:int
    movie:str
    title:str
    track_no:int
    singer:str
    duration:float

    def __init__(self,id,movie,title,track_no,singer,duration):
        self.id=id
        self.movie=movie
        self.title=title
        self.track_no=track_no
        self.singer=singer
        self.duration=duration

    def get_song(self):
        print(self.id,self.movie,self.title,self.track_no,self.singer,self.duration)

s1_instance=Song(1,"godha","innalekalil",3,"shaan rahman",3.09)

s1_instance.get_song()


