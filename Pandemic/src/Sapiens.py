#!/usr/bin/env python3
import Field
import State
from Location import Velocity, Location
import math
class Sapiens:
    """Represents a sapiens in movement with a Location
    and a Velocity.

    :author: Peter Sander
    """
    def __init__(self, location: Location, velocity: Velocity,
                 colour: str, field: Field, state: State, numberInfected: int):

        """Initialize a sapiens.

        :colour: Sapiens colour.
        :field: Field containing the sapiens.
        """
        self.location = location
        self.velocity = velocity
        self.field = field
        self.state = state
        self.colour = colour
        self.numberInfected = numberInfected

    def move(self) -> None:
        """Sapiens moves to a new Location.

        Random move depending on the sapiens's current Location.
        """
        [nextLocation,velocity] = self.field.nextDirectedsapiens(self.location,self.velocity)
        self.velocity = velocity
        if nextLocation != None:
            self.setLocation(nextLocation)


    def collisions(self, AdjacentLocation: Location) -> None:
        if self.location.row == AdjacentLocation.row and self.location.col == AdjacentLocation.col:
            self.velocity.row = -self.velocity.row
            self.velocity.col = -self.velocity.col



    def setLocation(self, nextLocation: Location) -> None:
        """Place the sapiens at the given Location.
        """
        self.field.clear(self.location)
        self.location = nextLocation
        self.field.place(self)

    def setVelocity(self, nextVelocity: Velocity) -> None:
        """Place the sapiens at the given Location.
        """
        self.field.clear(self.velocity)
        self.velocity = nextVelocity
        self.field.place(self)

    def setState(self, nextState: State) -> None:
        self.field.clear(self.state)
        self.state = nextState
        self.field.place(self)

    def setColor(self, nextColor: str) -> None:
        self.field.clear(self.color)
        self.color = nextColor
        self.field.place(self)

    def __str__(self):
        return f'Paricle({self.location})'
