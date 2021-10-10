from abc import ABC
from homework_02.exceptions import LowFuelError, NotEnoughFuel


class Vehicle(ABC):
    def __init__(self, weight, fuel=50, fuel_consumption=100):
        self.weight = weight
        self.fuel = fuel
        self.fuel_consumption = fuel_consumption
        self.started = False

    def start(self):
        if not self.started:
            if self.fuel > 0:
                self.started = True
            else:
                raise LowFuelError()

    def move(self, distance):
        required_fuel = distance * self.fuel_consumption
        if self.fuel >= required_fuel:
            self.fuel -= required_fuel
        else:
            raise NotEnoughFuel()

    def check_enough_fuel(self) -> bool:
        if self.fuel > 0:
            return True
        else:
            return False
