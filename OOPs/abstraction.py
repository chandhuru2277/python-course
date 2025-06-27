from abc import ABC, abstractmethod


# abstract class
class Vehicle(ABC):
    @abstractmethod
    def start_engine(self):
        pass

    @abstractmethod
    def stop_engine(self):
        pass

    @abstractmethod
    def start_process(self):
        self.door_open()
    
    def door_open(self):
        print("Door is opened")


# concreate class
class Car(Vehicle):
    def start_engine(self):
        print("Engine is started")

    def stop_engine(self):
        print("Engine stopped")

    def start_process(self):
        return super().start_process()
    
c1 = Car()
c1.start_engine()
c1.stop_engine()
c1.start_process()
