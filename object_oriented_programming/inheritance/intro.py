class Parent():
    def house(self):
        print("parent class house method")

class Child(Parent): #inheritance
    def social_media_acc(self):
        print("child class social media acc method")


c1_instance=Child()
c1_instance.social_media_acc()
c1_instance.house()
