#!/usr/bin/python
# -*- coding: utf-8 -*-

__author__ = 'K. Ziegler'

#Import and Initialization

import pygame
from pygame.locals import *

pygame.init()

#Display Configuration
screen = pygame.display.set_mode((640, 480))
pygame.display.set_caption("Paint Brush")

background = pygame.Surface(screen.get_size())
background = background.convert()
background.fill((255,255,0))

#Entities
brush = pygame.image.load('black_brush.gif')
brush = pygame.transform.scale(brush,(64,64))
brush_rect = brush.get_rect()

#Action --> Alter

#Assign Variables
keepGoing = True;
paint = False
clock = pygame.time.Clock()
speed = [2,2]

#Loop

while keepGoing:
    #Timer
    clock.tick(30)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            keepGoing = False
            break
        elif event.type ==MOUSEBUTTONDOWN:
            paint = True
        elif event.type == MOUSEBUTTONUP:
            paint = False
    if paint:
        x,y = pygame.mouse.get_pos()
        screen.blit(brush, (x-32,y-32))
        pygame.display.update()



