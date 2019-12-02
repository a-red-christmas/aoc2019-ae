#!/usr/bin/env python
import math
from typing import List


class RocketFuel(object):

    def __init__(self, file: str) -> None:
        self.filename = file
        self.total = []

    def calculate_fuel(self, mass: int) -> int:
        """ Calculate fuel requirement based on mass """
        fuel = math.floor(mass/3)-2
        return fuel

    def add_fuel(self, fuel: int) -> int:
        """ Fuel for fuel """
        self.total.append(fuel)
        t_fuel = self.calculate_fuel(fuel)
        while t_fuel > 0:
            self.total.append(t_fuel)
            t_fuel = self.calculate_fuel(t_fuel)
            #import pdb; pdb.set_trace()

    def run(self) -> int:
        with open(self.filename, 'r') as f:
            for line in f:
                mass = int(line)
                self.add_fuel(self.calculate_fuel(mass))

        total = sum(self.total)
        return total


rf = RocketFuel('input.txt')

print(rf.run())
