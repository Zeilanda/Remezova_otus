"""
создайте класс `Plane`, наследник `Vehicle`
"""
from homework_02.base import Vehicle
from homework_02.exceptions import CargoOverload


class Plane(Vehicle):
    cargo = 0
    max_cargo = 0

    def __init__(self):
        Plane.cargo = cargo
        

    @classmethod
    def load_cargo(needed_cargo):
        if needed_cargo + cargo <= max_cargo:
            cargo = needed_cargo + cargo
        else:
            raise CargoOverload()

    def remove_all_cargo(self):
        cargo_weight = self.cargo
        self.cargo = 0
        return cargo_weight
