class EventWise:
    def __init__(self):
        self.programs=[
            {"id":1,"event":"group song","name":"abi","contact":75875885,"batch":"djangorct","faculty":"anju"}

        ]

    def post(self,**kwargs):
        self.programs.append(kwargs)
        print("record has been created...")

    def get(self):
        if len(self.programs)==0:
            print("no records")

        else:
            for p in self.programs:
                print(p)

    def retrieve(self,id=None):
        pgm=[p for p in self.programs if p.get("id")==id][0]
        print(pgm)

    def put(self,id=None,**kwargs):
        pgm=[p for p in self.programs if p.get("id")==id][0]
        pgm.update(kwargs)
        print("record has been updated...")
        print(pgm)

  




event_instance=EventWise()

event_instance.post(id=2,event="dance",name="avin",contact=376587,batch="django",faculty="sukumar")
event_instance.get()
event_instance.retrieve(id=1)
event_instance.put(id=2,name="avin a b",contact=8367447589)
