class Movies:

    def __init__(self):
        self.movies=[
            {"id":1,"title":"spiderman","year":2026,"genre":"action","rating":9.5,"run_time":180,"director":"destin daniel"}
        ]

    def post(self,**kwargs):
        self.movies.append(kwargs)
        print("movie has been added")

    def get(self):
        if len(self.movies)==0:
            print("no records")
        else:
            for m in self.movies:
                print(m)

    def retrieve(self,id=None):
        mov=[m for m in self.movies if m.get("id")==id][0]
        print(mov)

    def put(self,id=None,**kwargs):
        mov=[m for m in self.movies if m.get("id")==id][0]
        mov.update(kwargs)
        print("record has been updated")
        print(mov)

    def delete(self,id=None):
        mov=[m for m in self.movies if m.get("id")==id][0]
        self.movies.remove(mov)
        print("record has been deleted")
        self.get()
                


mov_instance=Movies()
mov_instance.post(id=2,title="lokah",year=2025,genre='fantasy',rating=9.4,run_time=120,director='dominic arun')
mov_instance.get()
mov_instance.retrieve(2)
mov_instance.put(id=2,rating=9.1)
mov_instance.delete(id=2)