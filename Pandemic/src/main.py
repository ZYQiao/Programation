#!/usr/bin/env python3

import tkinter
from Simulator import Simulator


def main():
    root = tkinter.Tk()
    root.title('Brownian Motion Simulation')
    simulator = Simulator(root)
    numSteps = input("Please input numSteps：")
    numParticles = input("Please input numParticles：")
    simulator.simulate(int(numSteps),int(numParticles),0.05)
    root.mainloop()
    

if __name__ == '__main__':
    main()
