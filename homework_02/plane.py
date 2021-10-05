"""
создайте класс `Plane`, наследник `Vehicle`
"""
from homework_02.base import Vehicle


class Plane(Vehicle):
    def __init__(self, cargo, max_cargo):
        self.cargo = cargo
        self.max_cargo = max_cargo

    def load_cargo(self, needed_cargo):
        if needed_cargo + cargo <= max_cargo:
            cargo = needed_cargo + cargo
        else:
            exceptions.CargoOverload

    def remove_all_cargo(self):
        cargo_weight = cargo
        cargo = 0
        return cargo_weight

