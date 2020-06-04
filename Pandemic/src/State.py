#!/usr/bin/env python 
# -*- coding:utf-8 -*-

from enum import Enum, unique


@unique
class State(Enum):
    SUSCEPTIBLE, INFECTED, RECOVERED, DEAD = range(4)



if __name__ == '__main__':
    print(State.SUSCEPTIBLE)