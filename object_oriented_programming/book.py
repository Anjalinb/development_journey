class Book:
    title:str
    price:int
    pages:int
    author:str

    def __init__(self,title,price,pages,author):
        self.title=title
        self.price=price
        self.pages=pages
        self.author=author

    def get_book(self):
        print(self.title,self.price,self.pages,self.author)

rm_instance=Book("randamoozham",500,200,"mt")



rm_instance.get_book()

