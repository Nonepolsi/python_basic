"""
Объявите следующие исключения:
- LowFuelError
- NotEnoughFuel
- CargoOverload
"""

class LowFuelError(Exception):
    '''Low fuel level'''

class NotEnoughFuel(Exception):
    '''Not enough fuel'''

class CargoOverload(Exception):
    '''Cargo overload'''