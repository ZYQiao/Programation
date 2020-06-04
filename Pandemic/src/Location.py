#!/usr/bin/env python3
from random import randrange


class Location:
    """Represents a Location in a square grid.

    :author: Peter Sander
    """
    def __init__(self, row=None, col=None, min=0, max=50):
        """Initialize the Location.

        If the row and column args are absent,
        then random default values are generated, with
        min <= row, col < max.
        """
        self.row = row if row is not None else randrange(min, max)
        self.col = col if col is not None else randrange(min, max)

    def __str__(self):
        """
        :return: A string representation of the Location.
        """
        return f'({self.row}, {self.col})'



class Velocity(Location):
    """Represents a direction.

    -1 <= row, col <= 1
    :author: Peter Sander
    """
    def __init__(self, row=None, col=None):
        """Initialize the velocity.

        If the row and column args are absent,
        then random default values are generated.
        """
        super().__init__(row, col, -1, 2)


if __name__ == '__main__':
    print(f'default random: {[Location().__str__() for i in range(10)]}')
    print(f'non-random: {[Location(-1, 0).__str__() for i in range(10)]}')
