from abc import ABC,abstractmethod
class Car(ABC):
    @abstractmethod
    def start(self):pass
    @abstractmethod
    def accelerate(self):pass
    @abstractmethod
    def stop(self):pass

class Baleno(Car):
    def start(self):
        print("baleno start method")

    def accelerate(self):
        print("baleno accelerate method")

    def stop(self):
        print("baleno stop method")

baleno_instance=Baleno()
baleno_instance.start()