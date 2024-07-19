"""
создайте класс `Car`, наследник `Vehicle`
"""
from base import Vehicle
from engine import Engine

class Car(Vehicle):

    def __init__(self):
        
        self.engine = None

    def set_engine(self, new_engine: Engine) -> None:

        self.engine = new_engine