#!/usr/bin/python
# -*- coding: utf-8 -*-

__author__ = 'K. Ziegler'

import pygame
from pygame.locals import *

pygame.init()

screen = pygame.display.set_mode((640, 480))
pygame.display.set_caption("Hello, world! ")

background = pygame.Surface(screen.get_size())
background = background.convert()
background.fill((255,255,0))
#img = image.load("vikings.jpg").convert()

clock = pygame.time.Clock()
keepGoing = True

while keepGoing:
    clock.tick(30)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            keepGoing = False
    screen.blit(background, (0,0))
    pygame.display.flip()

