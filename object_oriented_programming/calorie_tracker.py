"""
create|add = post
details = retrieve
update = put
remove = delete
list = get

"""
class DietLens:

    def __init__(self):
        self.food_logs=[
            {"id":1,"name":"dosa","calorie":180,"owner":"Hari"}
            ]

    def post(self,**kwargs):
        required_fields={"id","name","calorie","owner"}
        missing_fields=required_fields.difference(kwargs.keys())
        if missing_fields:
            raise ValueError(missing_fields,"are missing")
        self.food_logs.append(kwargs)
        print("Record has been added")

    def get(self):
        if len(self.food_logs)==0:
            print("no records found...")
        else:
            for log in self.food_logs:
                print(log)

    def retrieve(self,id=None):
        if not id:
            raise ValueError("id missing") #dou
        else:
            return [log for log in self.food_logs if log.get("id")==id]

    def put(self,id=None,**kwargs):
        log=[log for log in self.food_logs if log.get("id")==id][0] #dou
        log.update(kwargs)
        print("record has been updated")

        print(log)

    def delete(self,id=None):

        log=[log for log in self.food_logs if log.get("id")==id][0]
        self.food_logs.remove(log)
        print("food removed...")
        self.get()    



diet_instance=DietLens()
diet_instance.post(id=2,name="burger",calorie=200,owner="anjali")
diet_instance.post(id=3,name="pizza",calorie=300,owner="sajna")
diet_instance.get()
print(diet_instance.retrieve(id=20))
diet_instance.put(id=1,name="ghee roast",owner="vipin")
diet_instance.delete(id=1)