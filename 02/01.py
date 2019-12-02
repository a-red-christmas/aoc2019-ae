#!/usr/bin/env python
from pprint import pprint


class OpCodeError(Exception):
    pass


class Intcode(object):
    def __init__(self, file: str) -> None:
        """ Initialize the input """
        self.file = file
        self._process_file()

    def _process_file(self):
        with open(self.file, 'r') as f:
            t_input = f.read().rstrip().split(',')
            self.input = list(map(lambda x: int(x), t_input))

    def update_dataset(self):
        self.input[1] = 12
        self.input[2] = 2

    def process(self):
        position = 0
        self.update_dataset()

        while position <= len(self.input):
            if self.input[position] == 1 or self.input[position] == 2:
                #import pdb; pdb.set_trace()
                instructions = [
                    self.input[position],
                    self.input[position + 1],
                    self.input[position + 2],
                    self.input[position + 3]
                ]
                if instructions[0] == 1:
                    # This is an add operation
                    self.input[instructions[3]] = \
                        self.input[instructions[1]] + self.input[instructions[2]]
                elif instructions[0] == 2:
                    self.input[instructions[3]] = \
                        self.input[instructions[1]] * self.input[instructions[2]]

                position = position + 4
            elif self.input[position] == 99:
                break
            else:
                raise OpCodeError(f"Unknown opcode: {self.input[position]}")

        return self.input[0]





ic = Intcode('input.txt')

pprint(ic.process())
