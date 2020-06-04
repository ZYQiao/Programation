#!/usr/bin/env python 
# -*- coding:utf-8 -*-
from random import randrange

from Sapiens import Sapiens
from State import State


class Collisions:

    def __init__(self):
        self.numberInfected = 0

                    
    def collisions(self,sapiens_1: Sapiens, sapiens_2: Sapiens) -> None:
        sapiens_1.velocity.row = -sapiens_1.velocity.row
        sapiens_1.velocity.col = -sapiens_1.velocity.col
        sapiens_2.velocity.row = -sapiens_2.velocity.row
        sapiens_2.velocity.col = -sapiens_2.velocity.col
        if sapiens_1.state == State.INFECTED and sapiens_2.state == State.SUSCEPTIBLE:
            sapiens_1.numberInfected += 1
            if randrange(0, 1000) >= 500:
                sapiens_2.state = State.INFECTED
            return None
        if sapiens_2.state == State.INFECTED and sapiens_1.state == State.SUSCEPTIBLE:
            sapiens_2.numberInfected += 1
            if randrange(0, 1000) >= 500:
                sapiens_1.state = State.INFECTED
            return None

        
            