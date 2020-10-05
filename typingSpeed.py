#!/bin/python3

import pygame
from pygame.locals import *
import sys
import time
import random
import importlib


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
        self.results = 'Time: 0 Accuracy: 0% Wpm: 0'
        self.wmp = 0
        self.end = False
        self.HEAD_C = (255, 213, 102)
        self.TEXT_C = (240, 240, 240)
        self.RESULT_C = (255, 70, 70)

        pygame.init()
        self.open_img = pygame.image.load('type-speed-open.jpg')
        self.open_img = pygame.transform.scale(self.open_img, (self.width, self.height))

        self.bg = pygame.image.load('bg.jpg')
        self.bg = pygame.transform.scale(self.bg, (self.height, self.width))

        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption('Typing Speeeeed)')

    def draw_text(self, screen, msg, y, fsize, color):
        font = pygame.font.Font(None, fsize)
        text = font.render(msg, 1, color)
        text_rect = text.get_rect(center=(self.width / 2, y))
        screen.blit(text, text_rect)
        pygame.display.update()

    def get_sentence(self):
        f = open('').read()
        sentences = f.split('\n')
        sentence = random.choice(sentences)
        return sentence

    def show_results(self, screen):
        if(not self.end):
            #Time Calculate
            self.total_time = time.time() - self.time_start

            #Accuracy
            count = 0
            for i,c in enumerate(self.word):
                try:
                    if self.input_text[i] == c:
                        count += 1
                except:
                    pass
            self.accuracy = count/len(self.word)/100

            #words per minute
            self.wpm = len(self.input_text)*60/(5*self.total_time)
            self.end = True
            print(self.total_time)

            self.results = 'Time:' + str(round(self.total_time)) + ' secs Accuracy:' + str(round(self.accuracy)) + '%' + ' Wpm:' + str(round(self.wpm))

            # draw icon img
            self.time_image = pygame.image.load('icon.png')
            self.time_image = pygame.transform.scale(self.time_image, (150, 150))
            # screen.blit(self.time_image, (150, 150))
            screen.blit(self.time_image, (self.width/2-75, self.width-140))
            self.draw_text(screen, "Reset", self.height - 70, 26, (100, 100, 100))

            print(self.results)
            pygame.display.update()

    def run(self):
        # self.reset_game()

        self.running = True
        while(self.running):
            clock = pygame.time.Clock()
            self.screen.fill((0, 0, 0), (50, 250, 650, 50))
            pygame.draw.rect(self.screen,self.HEAD_C, (50,250,650,50), 2)
            # update the text
            self.draw_text(self.screen, self.input_text,
                           274, 26, (250, 250, 250))
            pygame.display.update()


App()
