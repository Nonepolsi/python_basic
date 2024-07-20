"""
создайте класс `Car`, наследник `Vehicle`
"""
from base import Vehicle
from engine import Engine

class Car(Vehicle):

    def __init__(self, *args):
        
        self.engine = None
        super().__init__(*args)

    def set_engine(self, new_engine: Engine) -> None:

        self.engine = new_engine

car1 = Car()
print(isinstance(car1, Vehicle))