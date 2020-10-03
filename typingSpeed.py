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
        self.input_text = ''
        self.word = ''
        self.time_start = 0
        self.total_time = 0
        self.accuracy = '0%'
        self.results = 'Time: 0 Accuraty: 0% Wpm: 0'
        self.wmp = 0
        self.end = False
        self.HEAD_C = (255, 213, 102)
        self.TEXT_C = (240, 240, 240)
        self.RESULT_C = (255, 70, 70)

        pygame.init()
        self.open_img = pygame.image.load()
        self.open_img = pygame.transform.scale(self.open_img, (self.width, self.height))

        self.bg = pygame.image.load()
        self.bg = pygame.transform.scale(self.bg, (self.height, self.width))

        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption()
