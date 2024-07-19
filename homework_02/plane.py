"""
создайте класс `Plane`, наследник `Vehicle`
"""
from base import Vehicle
from typing import TypedDict, Unpack
import exceptions as exc


class VehicleArgs(TypedDict):

    weight: int
    fuel: float
    fuel_consumption: float


class Plane(Vehicle):

    def __init__(
            self, *,
            max_cargo: int = 200,
            **kwargs: Unpack[VehicleArgs]
        ):
        
        self._cargo = 0
        self._max_cargo = max_cargo
        super().__init__(**kwargs)

    def load_cargo(self, extra_cargo: int) -> None:

        if (new_cargo := self._cargo + extra_cargo) > self._max_cargo:
            raise exc.CargoOverload("New cargoload is too heavy")
        
        self._cargo = new_cargo

    def remove_cargo(self) -> int:

        current_cargo = self._cargo
        self._cargo = 0

        return current_cargo