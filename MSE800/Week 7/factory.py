from abc import ABC, abstractmethod
 
class Factory(ABC):
   
    @abstractmethod
    def create_product(self, kind=None):
        pass
 
class VehicleFactory(Factory):
    def __init__(self):
        pass
 
    def create_product(self, kind=None):
        if kind == "dog":
            animal = Car()
        elif kind == "cat":
            animal = Van()
 
        return animal
 
class CarFactory(Factory):
   
    def create_product(self, kind=None):
        pass
 
class VanFactory(Factory):
   
    def create_product(self, kind=None):
        pass
 
 
 
 
class Vehicle(ABC):
 
    @abstractmethod
    def run(self):
        pass
 
class Car(Vehicle):
 
    def run(self):
        print(f"I'm a Dog, I can run!!")

class Van(Vehicle):
    def __init__(self):
        pass
 
    def run(self):
        print(f"I'm a Cat, I can run!!")
 
 
 
 
 
# client
cat_factory = CarFactory()
dog = Car()
dog = cat_factory.create_product()
from abc import ABC, abstractmethod
 
class Factory(ABC):
   
    @abstractmethod
    def create_product(self, kind=None):
        pass
 
class VehicleFactory(Factory):
    def __init__(self):
        pass
 
    def create_product(self, kind=None):
        if kind == "dog":
            animal = Car()
        elif kind == "cat":
            animal = Van()
 
        return animal
 
class CarFactory(Factory):
   
    def create_product(self, kind=None):
        return Car()
 
class VanFactory(Factory):
   
    def create_product(self, kind=None):
        return Van()
 
class Vehicle(ABC):
 
    @abstractmethod
    def run(self):
        pass
 
class Car(Vehicle):
 
    def run(self):
        print(f"I'm a Dog, I can run!!")
 
 
class Van(Vehicle):
    def __init__(self):
        pass
 
    def run(self):
        print(f"I'm a Cat, I can run!!")
 
 
 
 
 
# client

print("Using Animal Factory - Super class")
animal_factory = VehicleFactory()

dog_animal = animal_factory.create_product("dog")
dog_animal.run()

cat_animal = animal_factory.create_product("cat")
cat_animal.run()


print("\nUsing Dog Factory - Sub class")
dog_factory = CarFactory()
dog = Car()
dog = dog_factory.create_product() 
dog.run()

print("\nUsing Cat Factory - Sub class")
cat_factory = VanFactory()
cat = Van()
cat = cat_factory.create_product() 
cat.run()

