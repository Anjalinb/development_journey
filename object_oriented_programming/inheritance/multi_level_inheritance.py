class GrandParent:
    def properties(self):
        print("2 acre land...")

class Parent(GrandParent):
    def home(self):
        print("1500 sqft house")

class Child(Parent):
    def social_media_acc(self):
        print("social_media_account")

child_instance=Child()
child_instance.social_media_acc()
child_instance.home()
child_instance.properties()