"""
создайте класс `Plane`, наследник `Vehicle`
"""
from base import Vehicle
import exceptions as exc


class Plane(Vehicle):

    def __init__(
            self,
            weight: int,
            fuel: float,
            fuel_consumption: float,
            max_cargo: int = 200
        ):
        
        self._cargo = 0
        self._max_cargo = max_cargo
        super().__init__(weight, fuel, fuel_consumption)

    def load_cargo(self, extra_cargo: int) -> None:

        if (new_cargo := self._cargo + extra_cargo) > self._max_cargo:
            raise exc.CargoOverload("New cargoload is too heavy")
        
        self._cargo = new_cargo

    def remove_cargo(self) -> int:

        current_cargo = self._cargo
        self._cargo = 0

        return current_cargo