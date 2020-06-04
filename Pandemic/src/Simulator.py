#!/usr/bin/env python3
import tkinter
from random import randrange, randint
import time
from Field import Field
from Sapiens import Sapiens
from Location import Location, Velocity
from Randomizer import Randomizer
from SimulatorView import SimulatorView

from State import State



class Simulator():
    """Runs the brownian-motion simulation.

    :author: Peter Sander
    """
    def __init__(self, root: object, size=50):
        """Create a simulation with the given field size.

        :root: tkinter.Tk graphics object
        """
        self.size = size
        self._sapiens = []  # all sapiens in the simulation
        self._field = Field(size)
        self.step = 0
        self._view = SimulatorView(root, size)
        self._colours = {State.SUSCEPTIBLE: 'slate blue',
                        State.INFECTED: 'red',
                        State.RECOVERED: 'spring green',
                        State.DEAD: 'black'}
        self.reset()

    def runLongSimulation(self) -> None:
        """Run the simulation from its current state for a reasonably
        long period, e.g. 500 steps.
        """
        self.simulate(500,50)

    def simulate(self, numSteps, numSapiens, delay=1) -> None:
        """Run the simulation from its current state for
        the given number of steps.

        :delay: Time (in secs) between each iteration.
        """
        self.step = 0
        self.populate(numSapiens)
        while self.step < numSteps:
            self.simulateOneStep()
            # self.step += 1
            time.sleep(delay)

    def simulateOneStep(self) -> None:
        """Run the simulation from its current state for a single step.
        """
        self.step += 1
        #  all _sapiens in motion
        for p in self._sapiens:
            for p_tmp in self._sapiens:
                if p_tmp.location != p.location:
                    p.collisions(p_tmp.location)
        for sapien in self._sapiens:
            sapien.move()
        self._view.showStatus(self.step, self._sapiens)

    def reset(self):
        """Reset the simulation to a starting location.
        """
        self.step = 0
        self._sapiens = []
        self.populate(0)
        self._view.showStatus(self.step, self._sapiens)

    def populate(self, numSapiens=50):
        """Populates the _field with randomly-locationed _sapiens.
        """
        self._field.clear()
        for s in range(numSapiens):
            location = Location(None,None,0,self.size)# generate 0 <= random location < size
            velocity = Velocity(randrange(-1,1),randrange(-1,1))# generate random -1 <= random velocity < 1
            colour = self._colours[State.SUSCEPTIBLE]
            state = State.SUSCEPTIBLE
            self._sapiens.append(Sapiens(location, velocity, colour, self._field, state, ))# append particle with location and velocity


if __name__ == '__main__':
    root = tkinter.Tk()
    root.title('Brownian Motion Simulation')
    simulator = Simulator(root)
    root.mainloop()

