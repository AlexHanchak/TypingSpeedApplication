#!/bin/python3

import pygame
from pygame.locals import *
import sys
import time
import random


class App:
    def __init__(self):
        self.width = 800
        self.height = 500
        self.reset = True
        self.active = False

