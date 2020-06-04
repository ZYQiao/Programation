#!/usr/bin/env python3
from random import randrange

import Field
from State import State
from Location import Velocity, Location
from Stats import Stats


class Sapiens:
    """Represents a sapiens in movement with a Location
    and a Velocity.

    :author: Peter Sander
    """
    def __init__(self, location: Location, velocity: Velocity,
                 colour: str, field: Field, state: State, numberInfected: int, step: int):

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
        self.step = step
        
    

    def infectedMove(self) -> None:
        """A infected sapiens move

        :param sapiens: infected sapiens
        :return:
        """
        self.step += 1
        if self.step == 22:
            if randrange(0, 1000) >= 500:
                self.state = State.DEAD
                self.velocity.row = 0
                self.velocity.col = 0
            else:
                self.state = State.RECOVERED

    def move(self) -> None:
        """Sapiens moves to a new Location.

        Random move depending on the sapiens's current Location.
        """
        if(self.state == State.INFECTED):
            self.infectedMove()
        [nextLocation,velocity] = self.field.nextDirectedsapiens(self.location,self.velocity)
        self.velocity = velocity
        if nextLocation != None:
            self.setLocation(nextLocation)


    # def collisions(self, AdjacentLocation: Location) -> None:
    #     if self.location.row == AdjacentLocation.row and self.location.col == AdjacentLocation.col:
    #         self.velocity.row = -self.velocity.row
    #         self.velocity.col = -self.velocity.col



    def setLocation(self, nextLocation: Location) -> None:
        """Place the sapiens at the given Location.
        """
        self.field.clear(self.location)
        self.location = nextLocation
        self.field.place(self)

    def setVelocity(self, nextVelocity: Velocity) -> None:
        """Place the sapiens at the given Location.
        """
        self.field.clear(self.location)
        self.velocity = nextVelocity
        self.field.place(self)

    def setState(self, nextState: State) -> None:
        self.field.clear(self.location)
        self.state = nextState
        self.field.place(self)

    def setColour(self, nextColour: str) -> None:
        self.field.clear(self.location)
        self.colour = nextColour
        self.field.place(self)

    def __str__(self):
        return f'Paricle({self.location})'
