#!/usr/bin/env python3

import tkinter
from Simulator import Simulator


def main():
    root = tkinter.Tk()
    root.title('Brownian Motion Simulation')
    simulator = Simulator(root)
    numSapienses = input("Please input numSapienses：")
    simulator.simulate(int(numSapienses),0.1)
    root.mainloop()
    

if __name__ == '__main__':
    main()
