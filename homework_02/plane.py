"""
создайте класс `Plane`, наследник `Vehicle`
"""
from homework_02.base import Vehicle
from homework_02.exceptions import CargoOverload



def initer_parent(self, a, b, c):
    self.a = a
    self.b = b
    self.c = c

def initer_child(self, a, b, c, d):
    initer_parent(self, a, b, c)
    self.d = d

class Plane(Vehicle):
    cargo = 0
    max_cargo = 0

    def __init__(self, weight, fuel, fuel_consumption, max_cargo):
        super().__init__(weight, fuel, fuel_consumption)
        self.max_cargo = max_cargo

    def load_cargo(self, needed_cargo):
        if needed_cargo + self.cargo <= self.max_cargo:
            self.cargo = needed_cargo + self.cargo
        else:
            raise CargoOverload()

    def remove_all_cargo(self):
        cargo_weight = self.cargo
        self.cargo = 0
        return cargo_weight
