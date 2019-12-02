#!/usr/bin/env python
import math

class RocketFuel(object):

    def __init__(self, file: str) -> None:
        self.filename = file
        self.total = 0

    def calculate_fuel(self, mass: int) -> int:
        """ Calculate fuel requirement based on mass """
        fuel = math.floor(mass/3)-2
        return fuel

    def run(self):
        with open(self.filename, 'r') as f:
            for line in f:
                mass = int(line)
                self.total += self.calculate_fuel(mass)

        return self.total


rf = RocketFuel('input.txt')

print(rf.run())
