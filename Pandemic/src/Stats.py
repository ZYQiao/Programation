#!/usr/bin/env python 
# -*- coding:utf-8 -*-
"""Virus characteristics.

   These are absolutely arbitrary.
   :author: Peter Sander
"""
from State import State


class Stats:
    def __init__(self):
        self.R_0 = 10.5
        # the probability of passing the virus
        #  upon contact between sapienses
        self.INFECTION_RATE = 0.5
        # the number of steps that a sapiens remains infected before
        #  passing to the next state
        self.RECOVERY_TIME = 21
        # the probability of passing from infected to dead
        # hence the probability of recovering is 1 - MORBIDITY_RATE
        self.MORBIDITY_RATE = 0.5


    def isViable(self, sapienses: list) -> bool:
        """Determine whether the simulation is still viable, ie, should it
        continue to run.

        :param sapienses:
        When no infected sapiens are left, the simulation stops.
        :return: True if there are any infected sapiens left.
        """
        for s in sapienses:
            if s.state == State.INFECTED:
                return True
        return False

    def calculateR(self, sapienses:list) -> float:
        """Calculates the current effective reproduction number.

        :param sapienses:
        :return: R, the effective reproduction number.
        """
        number = {state: 0 for state in State}
        totalInfected = 0
        for sapiens in sapienses:
            number[sapiens.state] += 1
            if sapiens.state == State.INFECTED:
                totalInfected += sapiens.numberInfected
        return totalInfected / number[State.INFECTED] * number[State.SUSCEPTIBLE] / (number[State.SUSCEPTIBLE]
                                                                                     + number[State.RECOVERED]
                                                                                     + number[State.DEAD])\
            if number[State.INFECTED] > 0 else 0

    def state(self, sapienses:list) -> str:
        number = {state: 0 for state in State}
        totalInfected = 0
        for sapiens in sapienses:
            number[sapiens.state] += 1
            if sapiens.state == State.INFECTED:
                totalInfected += sapiens.numberInfected
        i = number[State.INFECTED]
        s = number[State.SUSCEPTIBLE]
        r = number[State.RECOVERED]
        d = number[State.DEAD]
        R = totalInfected / number[State.INFECTED] * number[State.SUSCEPTIBLE] / (number[State.SUSCEPTIBLE]
                                                                              + number[State.RECOVERED]
                                                                              + number[State.DEAD]) if number[State.INFECTED] > 0 else 0
        return "['S="+str(s)+ "','I="+str(i)+"','R="+str(r)+"','D="+str(d)+"']R="+str(R)
