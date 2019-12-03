#!/usr/bin/env python
from typing import List
import re
from pprint import pprint


class CoordinateException(Exception):
    pass


class Wiregrid(object):
    """ This is the base class for AoC day 3. """

    def __init__(self, filename: str) -> None:
        self.filename = filename
        self.cable1 = set()
        self.cable2 = set()
        self.read_file()
        self._process()

    def move(self, cable: list, instructions: list) -> None:
        """ Pass the cable object as cable, and the list of instructions verbatim """
        # R/L is +/- on first coordinate, U/D is +/- on second coordinate
        current_position = (0,0)
        steps = 0
        for instruction in instructions:

            re_instruction = re.match(r'(U|D|L|R)([0-9]+)', instruction)
            if re_instruction is not None:
                direction = re_instruction.group(1)
                # We ought to check if it's an actual number here, but we trust the dataset
                distance = int(re_instruction.group(2))
            else:
                raise CoordinateException(f'Invalid instruction {instruction}')

            if direction == 'R':
                # Add distance to index 0
                for _ in range(distance):
                    steps += 1
                    axis = current_position[0] + 1
                    new_pos = (axis, current_position[1], steps)
                    cable.add(new_pos)
                    current_position = new_pos

            elif direction == 'L':
                # Subtract distance from index 0
                for _ in range(distance):
                    steps += 1
                    axis = current_position[0] - 1
                    new_pos = (axis, current_position[1], steps)
                    cable.add(new_pos)
                    current_position = new_pos

            elif direction == 'U':
                # Add one to index 1
                for _ in range(distance):
                    steps += 1
                    axis = current_position[1] + 1
                    new_pos = (current_position[0], axis, steps)
                    cable.add(new_pos)
                    current_position = new_pos

            elif direction == 'D':
                # Subtract one from index 1
                for _ in range(distance):
                    steps += 1
                    axis = current_position[1] - 1
                    new_pos = (current_position[0], axis, steps)
                    cable.add(new_pos)
                    current_position = new_pos

    def read_file(self) -> None:
        """ Read file and convert coordinates to a list of instructions """

        self.i_cable1 = []
        self.i_cable2 = []

        instructions = [self.i_cable2, self.i_cable1]

        with open(self.filename, 'r') as f:
            for line in f:
                cable = instructions.pop()
                for inst in line.split(','):
                    cable.append(inst.rstrip())

    def _process(self) -> None:
        self.move(self.cable1, self.i_cable1)
        self.move(self.cable2, self.i_cable2)

    def get_distance(self, x: int, y:int) -> int:
        return abs(x) + abs(y)

    def get_steps(self, point: tuple) -> int:
        paths1 = set(filter(lambda x: x[0] == point[0] and x[1] == point[1], self.cable1))
        paths2 = set(filter(lambda x: x[0] == point[0] and x[1] == point[1], self.cable2))
        step1 = set(map(lambda x: x[2], paths1))
        step2 = set(map(lambda x: x[2], paths2))


        return (min(step1) + min(step2))



    def find_intersections(self) -> list:
        """We need to compare the two lists of positions to find identical
        entries"""
        cab1 = set(map(lambda x: (x[0], x[1]), self.cable1))
        cab2 = set(map(lambda x: (x[0], x[1]), self.cable2))
        common = cab1 & cab2

        steps = list(map(lambda x: self.get_steps((x[0], x[1])), common))

        return min(steps)


if __name__ == '__main__':
    wg = Wiregrid('input.txt')
    pprint(wg.find_intersections())
