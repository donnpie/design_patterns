"""
The Abstract Factory pattern is a creational design pattern that provides an interface for creating families of related or dependent objects without specifying their concrete classes. It is also known as the Kit pattern.

The Abstract Factory pattern is useful when you need to create sets of objects that work together or belong to a common theme. It promotes the concept of object composition, where multiple objects are designed to work together to achieve a common goal.
This pattern is particularly useful when you have multiple families of related objects or when you want to provide a choice of object variations to the client code. It encapsulates the decision-making process of object creation within the factory classes.

Here's a simplified overview of how the Abstract Factory pattern works:

Define an abstract factory interface that declares a set of creation methods for creating related objects. Each method in the abstract factory corresponds to a specific product type or family of products.
Create concrete factory classes that implement the abstract factory interface. Each concrete factory is responsible for creating a specific set of related objects.
Define an abstract product interface that declares the operations that all products must implement.
Create multiple sets of concrete product classes that implement the abstract product interface. Each concrete product class corresponds to a specific product type or family of products.
The client code works with the abstract factory and product interfaces. It uses the factory methods to create products, without being aware of the specific concrete classes that are instantiated.
At runtime, the appropriate concrete factory is instantiated, based on the specific implementation chosen.
The concrete factory creates a family of products, which are all guaranteed to be compatible and work together.
The client code can then use the created products, relying on their abstract interfaces, without being tightly coupled to specific concrete classes.
The Abstract Factory pattern enables the creation of families of objects while ensuring their compatibility and adherence to common interfaces. It allows for easy switching between different sets of related objects, promoting flexibility and maintainability.
"""

from abc import ABC, abstractmethod

class Abstract:
    def identify(self):
        print(f"I am a {self.__class__.__name__}")

class Concrete1(Abstract):
    pass

class Concrete2(Abstract):
    pass

class Concrete3(Abstract):
    pass

class Factory(ABC):
    @abstractmethod
    def manufacture(self) -> Abstract:
        pass
        
class Factory1(Factory):
    #Override
    def manufacture(self) -> Abstract:
        return Concrete1()
        
class Factory2(Factory):
    #Override
    def manufacture(self) -> Abstract:
        return Concrete2()
        
class Factory3(Factory):
    #Override
    def manufacture(self) -> Abstract:
        return Concrete3()

class FactoryProducer:
    @staticmethod
    def produce(type: str) -> Factory:
        if  str.lower(type) == 'factory1':
            return Factory1()
        elif str.lower(type) == 'factory2':
            return Factory2()
        elif str.lower(type) == 'factory3':
            return Factory3()
        else:
            raise ValueError("No such type exists")


def main():
    # Create a factory
    fact1: Factory = FactoryProducer.produce('factory1')

    # Instantiate object of type Abstract
    concrete1: Abstract = fact1.manufacture()

    # Note that the actual type is Concrete
    concrete1.identify()

    # Main only depends on the abstract class, the factory producer class and the factory class. It does not know or care about the concrete classes.

if __name__ == '__main__':
    main()