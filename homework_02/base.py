from abc import ABC
import exceptions as exc


class Vehicle(ABC):
    
    def __init__(
            self, *,
            weight: int = 1000,
            fuel: float = 30, 
            fuel_consumption: float = 5
        ):

        self._weight = weight
        self._started = False
        self._fuel = fuel
        self._fuel_consumption = fuel_consumption

    def start(self):
        
        if self._fuel <= 0:
            raise exc.LowFuelError("Not enough fuel to start vehicle")
        
        if not self._started:
            self._started = True
            print("success")

    def move(self, distance):

        if (new_fuel := self._fuel - self._fuel_consumption * distance) < 0:
            raise exc.NotEnoughFuel("Not enough fuel to cover journey")
        
        self._fuel = new_fuel
        print(self._fuel)