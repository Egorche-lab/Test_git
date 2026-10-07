class LowFuelError(Exception):
    """Топливо на нуле, двигатель не запустится."""
    pass


class NotEnoughFuel(Exception):
    """Топлива не хватает на поездку."""
    pass


class CargoOverload(Exception):
    """Превышена максимальная загрузка."""
    pass