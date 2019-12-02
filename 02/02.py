#!/usr/bin/env python
from pprint import pprint


class OpCodeError(Exception):
    pass


class Intcode(object):
    def __init__(self, file: str) -> None:
        """ Initialize the input """
        self.file = file
        self._process_file()
        self.reset()

    def _process_file(self):
        with open(self.file, 'r') as f:
            t_input = f.read().rstrip().split(',')
            self.input = list(map(lambda x: int(x), t_input))

    def reset(self) -> None:
        self.dataset = list(map(lambda x: int(x), self.input)) # This should be the equivalent of a deep copy

    def update_dataset(self, val1: int, val2: int) -> None:
        self.dataset[1] = val1
        self.dataset[2] = val2

    def instruction(self, ptr: int) -> int:
        """ Run the instruction """
        noun = self.dataset[ptr]
        if noun == 1 or noun == 2:
            params = [self.dataset[ptr + 1], self.dataset[ptr + 2], self.dataset[ptr + 3]]

        if noun == 1:
            self.dataset[params[2]] = self.dataset[params[0]] + self.dataset[params[1]]
            return ptr + 4
        elif noun == 2:
            self.dataset[params[2]] = self.dataset[params[0]] * self.dataset[params[1]]
            return ptr + 4
        elif noun == 99:
            return 0
        else:
            raise OpCodeError(f"Invalid OpCode: index {ptr} value: self.dataset[ptr]")


    def _process(self, val1: int, val2: int) -> int:
        self.update_dataset(val1, val2)
        position = 0

        while position <= len(self.dataset):
            new_pos = self.instruction(position)
            if new_pos != 0:
                position = new_pos
            else:
                break

        return self.dataset[0]

    def run(self, target: int) -> list:
        """Run _process with all values of val1 and val2 until a match for
        target has been found"""

        valid_values = range(0, 99)

        # This will be some sort of brute force attempt
        values = [0, 0]
        while values[0] < 100 and values[1] < 100:
            self.reset()
#            import pdb; pdb.set_trace()
            test = self._process(values[0], values[1])
            if test == target:
                break
            else:
                if values[0] <= 99:
                    if values[1] < 99:
                        values[1] += 1
                    elif values[1] == 99 and values[0] < 99:
                        values[0] += 1
                        values[1] = 0

                else:
                    raise OpCodeError("No value possible")

        return 100 * values[0] + values[1]



ic = Intcode('input.txt')

pprint(ic.run(19690720))
