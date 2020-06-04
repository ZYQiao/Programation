from random import shuffle
import Sapiens
from Location import Location, Velocity
from Randomizer import Randomizer


class Field():
    """Represent a square grid of field locations.

    Each location is able to store a single sapiens.
    :author: David J. Barnes and Michael Kolling
    :author: Peter Sander
    """
    _rand = Randomizer.getRandom().random

    def __init__(self, size):
        self.size = size
        self.clear()

    def clear(self, location: Location = None) -> None:
        """Empty the field or clear the given location.

        :location: The location to clear, or None to empty the field.
        """
        if location is None:
            self._field = [[None] * self.size for i in range(self.size)]
        else:
            self._field[location.row][location.col] = None

    def place(self, sapiens: Sapiens) -> None:
        """Place a sapiens at the given location.

        If there is already a sapiens at the location it will be overwritten.
        """
        location = sapiens.location
        self._field[location.row][location.col] = sapiens

    def getObjectAt(self, location: Location) -> Sapiens:
        """Return the sapiens at the given location, if any.

        :location: The location.
        :return: The sapiens at the given location, or None if there is none.
        """
        return self._field[location.row][location.col]

    def freeAdjacentlocation(self, sapiens: Sapiens, radius: int) -> Location:
        """Try to find a free location that is adjacent to the given sapiens's
        location.

        The returned location will be within the bounds of the field.
        :return: A valid location within the grid area, otherwise None.
        """
        adjacent = self._adjacentlocations(sapiens, radius)
        free = [next for next in adjacent if not self.getObjectAt(next)]
        return free[0] if len(free) > 0 else None

    def nextDirectedsapiens(self, location: Location, velocity: Velocity) -> [Location,Velocity]:

        if location.row + velocity.row < self.size and location.row + velocity.row > 0:
            location.row += velocity.row
        else:
            velocity.row = -velocity.row
            location.row += velocity.row
            
        if location.col + velocity.col < self.size and location.col + velocity.col > 0:
            location.col += velocity.col
        else:
            velocity.col = -velocity.col
            location.col += velocity.col
        return [location,velocity]
    
    def _adjacentlocations(self, sapiens: Sapiens, radius) -> list:
        """Return a shuffled list of posiions adjacent to the given one.

        The list will not include the sapiens location itself.
        All locations lie within the grid.
        :radius: Radius of adjacent locations.
        :return: A list of locations adjacent to the sapiens.
        """
        location = sapiens.location
        locations = []
        if location is not None:
            row = location.row
            col = location.col
            for roffset in range(-radius, radius + 1):
                nextRow = row + roffset
                if 0 <= nextRow < self.size:
                    for coffset in range(-radius, radius + 1):
                        nextCol = col + coffset
                        # excludes sapiens location
                        if 0 <= nextCol < self.size \
                                and (roffset != 0 or coffset != 0):
                            locations.append(location(nextRow, nextCol))
            # randomize location order.
            shuffle(locations, Field._rand)
        return locations
