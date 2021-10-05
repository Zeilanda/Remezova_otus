from abc import ABC
from homework_02.exceptions import LowFuelError, NotEnoughFuel


class Vehicle(ABC):
    def __init__(self, weight, fuel, fuel_consumption):
        self.weight = weight
        self.fuel = fuel
        self.fuel_consumption = fuel_consumption

    def start(self, started):
        if not started:
            if self.fuel > 0:
                "refresh started"
            else:
                raise LowFuelError

    def move(self, distance):
        if distance * self.fuel_consumption >= self.fuel:
            self.fuel = self.fuel - distance * self.fuel_consumption
        else:
            raise NotEnoughFuel
