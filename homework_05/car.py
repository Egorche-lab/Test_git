from homework_05.base import Vehicle
from homework_05.engine import Engine


class Car(Vehicle):
    """Автомобиль — транспортное средство с двигателем."""

    engine: Engine = None

    def set_engine(self, engine: Engine):
        """Установить двигатель на автомобиль."""
        self.engine = engine