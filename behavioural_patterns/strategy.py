"""
The Strategy pattern is a behavioral design pattern that enables dynamic selection of algorithms or strategies at runtime. It allows you to encapsulate different algorithms within separate classes, making them interchangeable based on specific requirements.

The main idea behind the Strategy pattern is to define a family of algorithms, encapsulate each one as a separate class, and make them interchangeable. This allows the client code to vary the algorithm being used without modifying the client's code structure.

Here's a simplified overview of how the Strategy pattern works:

- Define a common interface or base class that represents the strategy. This interface declares a method or set of methods that represent the algorithm to be performed.
- Implement multiple concrete strategy classes, each providing its own implementation of the strategy methods defined in the interface.
- In the client code, create an instance of the strategy class that needs to be used.
- The client code can then call the strategy method through the interface, without being aware of the specific strategy class being used.
- At runtime, the appropriate strategy class is instantiated based on the desired behavior or input conditions.
- The client code can switch or modify the strategy dynamically by changing the strategy object, allowing for flexibility in algorithm selection.
- The Strategy pattern promotes encapsulation, separation of concerns, and code reusability. It provides a clear separation between the algorithm implementation and the client code, making the codebase more maintainable and extensible. It also allows for easy addition of new strategies without modifying the existing code.

This pattern is especially useful when you have multiple algorithms or behaviors that need to be dynamically selected or switched based on specific conditions, requirements, or user preferences.
"""
from abc import abstractmethod

class AbstractStrategy:
    def identify(self):
        print(f"I am a {self.__class__.__name__}")

    @abstractmethod
    def execute_strategy(self):
        """Must be implemented in derived classes"""
        pass

class ConcreteStrategy1(AbstractStrategy):
    def execute_strategy(self):
        print("Executing strategy 1")

class ConcreteStrategy2(AbstractStrategy):
    def execute_strategy(self):
        print("Executing strategy 2")

class ConcreteStrategy3(AbstractStrategy):
    def execute_strategy(self):
        print("Executing strategy 3")

class StrategySelector:
    @staticmethod
    def select(type: str) -> AbstractStrategy:
        if  str.lower(type) == 'strategy1':
            return ConcreteStrategy1()
        elif str.lower(type) == 'strategy2':
            return ConcreteStrategy2()
        elif str.lower(type) == 'strategy3':
            return ConcreteStrategy3()
        else:
            raise ValueError("No such type exists")

def main():
    # Instantiate object of type Abstract
    strat: AbstractStrategy = StrategySelector.select('strategy1')

    # Note that the actual type is Concrete
    strat.identify()
    strat.execute_strategy()

    # Main only depends on the AbstractStrategy class and the StrategySelector class. It does not know or care about the concrete classes.

if __name__ == '__main__':
    main()