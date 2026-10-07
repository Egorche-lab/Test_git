from homework_05.car import Car
from homework_05.engine import Engine
from homework_05.plane import Plane
from homework_05 import exceptions


# --- Машина ---
car = Car(weight=1500, fuel=60, fuel_consumption=0.08)
car.set_engine(Engine(volume=2.0, pistons=4))
car.start()
car.move(100)
print(f"Осталось топлива: {car.fuel}")

try:
    car.move(10000)
except exceptions.NotEnoughFuel as e:
    print(f"Ошибка: {e}")


# --- Самолёт ---
plane = Plane(weight=50000, fuel=10000, fuel_consumption=5, max_cargo=20000)
plane.load_cargo(5000)
plane.load_cargo(10000)
print(f"Загружено: {plane.cargo}")

try:
    plane.load_cargo(10000)
except exceptions.CargoOverload as e:
    print(f"Ошибка: {e}")

removed = plane.remove_all_cargo()
print(f"Разгрузили: {removed}, теперь cargo = {plane.cargo}")


# --- Нет топлива ---
empty_car = Car(weight=1000, fuel=0, fuel_consumption=0.1)
try:
    empty_car.start()
except exceptions.LowFuelError as e:
    print(f"Ошибка: {e}")