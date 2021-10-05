"""
создайте класс `Car`, наследник `Vehicle`
"""
from homework_02.base import Vehicle
from engine import Engine


class Car(Vehicle):
    def __init__(self, engine, weight, started, fuel, fuel_consumption):
        super().__init__(weight, started, fuel, fuel_consumption)
        self.engine = engine

    def set_engine(self, engine):
        engine = Car.engine

