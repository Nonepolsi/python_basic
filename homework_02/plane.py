"""
создайте класс `Plane`, наследник `Vehicle`
"""
from ..homework_02.base import Vehicle
from ..homework_02.exceptions import CargoOverload


class Plane(Vehicle):

    def __init__(
            self,
            weight: int,
            fuel: float,
            fuel_consumption: float,
            max_cargo: int = 200
        ):
        
        self.cargo = 0
        self.max_cargo = max_cargo
        super().__init__(weight, fuel, fuel_consumption)

    def load_cargo(self, extra_cargo: int) -> None:

        if (new_cargo := self.cargo + extra_cargo) > self.max_cargo:
            raise CargoOverload("New cargoload is too heavy")
        
        self.cargo = new_cargo

    def remove_all_cargo(self) -> int:

        current_cargo = self.cargo
        self.cargo = 0

        return current_cargo