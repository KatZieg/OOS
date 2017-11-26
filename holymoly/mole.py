#!/usr/bin/python
# -*- coding: utf-8 -*-

__author__ = 'K. Ziegler'

import pygame, sys
from pygame.locals import *
from pygame import  *
from pygame.sprite import *
import random

pygame.init()
fpsclock = pygame.time.Clock()

windowSurfaceObj = pygame.display.set_mode((640,480))
pygame.display.set_caption('Hit the mole')

class Mole(Sprite):
    def __init__(self):
        Sprite.__init__(self)
        self.image = image.load('mole.jpg')
        self.rect = self.image.get_rect()

my_mole = Mole()
all_sprites = Group(my_mole)
all_sprites.draw(windowSurfaceObj)
display.update()

hammer = pygame.image.load('hammer.jpg')
background = pygame.image.load('background_clear.jpg')

redColor = pygame.Color(255,0,0)
greenColor = pygame.Color(0,255,0)
blueColor = pygame.Color(0,0,255)
whiteColor = pygame.Color(255,255,255)

mousex, mousey = 0,0

fontObj = pygame.font.Font('freesansbold.ttf', 32)
msg = 'Hello World'

soundObj = pygame.mixer.Sound('bounce.wav')

randx = random.randrange(100, 400)
randy = random.randrange(100, 400)

while True:
    windowSurfaceObj.fill(whiteColor)
    windowSurfaceObj.blit(my_mole,(0, 0))
    windowSurfaceObj.blit(background, (0, 0))
    msgSurfaceObj = fontObj.render(msg, False, blueColor)
    msgRectObj = msgSurfaceObj.get_rect()
    msgRectObj.topleft = (10,20)
    windowSurfaceObj.blit(msgSurfaceObj, msgRectObj)

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == MOUSEBUTTONDOWN:
            mousex, mousey = event.pos
            if my_mole.rect.collidepoint(mouse.get_pos()):
                soundObj.play()

        elif event.type == MOUSEBUTTONUP:
            mousex, mousey = event.pos
            if event.button in (1,2,3):
                msg = 'left, middle, or right mouse click'
            elif event.button in (4,5):
                msg = 'mouse scrolled up or down'

        elif event.type == KEYDOWN:
            if event.key in (K_LEFT, K_RIGHT, K_UP, K_DOWN):
                msg = 'Arrow key passed'
            if event.key == K_a:
                msg = 'A key pressed'
            if event.key == K_ESCAPE:
                pygame.event.post(pygame.event.Event(QUIT))

    pygame.display.update()
    fpsclock.tick(30)




