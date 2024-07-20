from abc import ABC
import exceptions as exc


class Vehicle(ABC):
    
    def __init__(
            self,
            weight: int = 1000,
            fuel: float = 30, 
            fuel_consumption: float = 5
        ):

        self.weight = weight
        self.started = False
        self.fuel = fuel
        self.fuel_consumption = fuel_consumption

    def start(self):
        
        try:
            if self.fuel <= 0:
                raise exc.LowFuelError("Not enough fuel to start vehicle")
            
        except exc.LowFuelError as err:
            print(err)

        
        if not self.started:
            self.started = True
            print("success")

    def move(self, distance):

        try:
            if (new_fuel := self.fuel - self.fuel_consumption * distance) < 0:
                raise exc.NotEnoughFuel("Not enough fuel to cover journey")
            
        except exc.NotEnoughFuel as err:
            print(err)
        
        self.fuel = new_fuel
        print(self.fuel)