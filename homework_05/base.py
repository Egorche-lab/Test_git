from homework_05 import exceptions


class Vehicle:
    """Базовый класс для любого транспортного средства."""

    weight = 0
    started = False
    fuel = 0
    fuel_consumption = 0

    def __init__(self, weight, fuel, fuel_consumption):
        self.weight = weight
        self.fuel = fuel
        self.fuel_consumption = fuel_consumption

    def start(self):
        """
        Запустить двигатель.
        Если топлива нет — выбросить LowFuelError.
        Если уже запущен — ничего не делать.
        """
        if self.started:
            return
        if self.fuel <= 0:
            raise exceptions.LowFuelError("Нет топлива для запуска")
        self.started = True

    def move(self, distance):
        """
        Проехать distance км.
        Если топлива не хватает (вплоть до полного расхода) — NotEnoughFuel.
        Иначе — уменьшить fuel.
        """
        required = distance * self.fuel_consumption
        if required > self.fuel:
            raise exceptions.NotEnoughFuel("Недостаточно топлива")
        self.fuel -= required