from homework_05 import exceptions
from homework_05.base import Vehicle


class Plane(Vehicle):
    """Самолёт — транспортное средство с грузовым отсеком."""

    cargo = 0
    max_cargo = 0

    def __init__(self, weight, fuel, fuel_consumption, max_cargo):
        super().__init__(weight, fuel, fuel_consumption)
        self.max_cargo = max_cargo

    def load_cargo(self, value):
        """
        Загрузить value единиц груза.
        Если cargo + value > max_cargo — CargoOverload.
        """
        if self.cargo + value > self.max_cargo:
            raise exceptions.CargoOverload("Превышена максимальная загрузка")
        self.cargo += value

    def remove_all_cargo(self):
        """Обнулить груз и вернуть то, что было до обнуления."""
        previous = self.cargo
        self.cargo = 0
        return previous