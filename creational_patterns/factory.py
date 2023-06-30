"""
The Factory Method pattern is a creational design pattern that provides an interface for creating objects but delegates the responsibility of instantiation to subclasses. It encapsulates the creation of objects within a method, known as the factory method, which subclasses can override to provide specialized implementations.

The main idea behind the Factory Method pattern is to allow the client code to work with an abstract interface or base class, without being aware of the specific concrete class that will be instantiated. This promotes loose coupling between the client code and the concrete classes.

Here's a simplified overview of how the Factory Method pattern works:

Define an abstract base class or interface (e.g. Shape).
Create concrete subclasses that inherit from the base class or implement the interface (e.g. Square). 
Create a Factory class that creates instances of the subclasses, using the factory method (I renamed the method to manufacture below).
The client code (main()) uses the factory method to create objects, without having to know the concrete class being instantiated. It relies on the abstraction provided by the base class or interface.
At runtime, the appropriate concrete subclass is instantiated based on the implementation of the factory method in that subclass.
The client code can then work with the newly created object through the abstract interface or base class, without being tightly coupled to specific concrete classes.
The Factory Method pattern allows for extensibility and flexibility in object creation. It enables the addition of new concrete subclasses without modifying existing client code, as long as they conform to the abstract interface or base class.

By utilizing the Factory Method pattern, you can achieve decoupling and improve the maintainability and testability of your code, as well as support the principle of "programming to an interface, not an implementation."
"""

class Abstract:
    def identify(self):
        print(f"I am a {self.__class__.__name__}")

class Concrete1(Abstract):
    pass

class Concrete2(Abstract):
    pass

class Concrete3(Abstract):
    pass

class Factory:
    @staticmethod
    def manufacture(type: str) -> Abstract:
        if  str.lower(type) == 'concrete1':
            return Concrete1()
        elif str.lower(type) == 'concrete2':
            return Concrete2()
        elif str.lower(type) == 'concrete3':
            return Concrete3()
        else:
            raise ValueError("No such type exists")

def main():
    # Instantiate object of type Abstract
    concrete: Abstract = Factory.manufacture('concrete1')

    # Note that the actual type is Concrete
    concrete.identify()

    # Main only depends on the abstract class. It does not know or care about the concrete classes.

if __name__ == '__main__':
    main()