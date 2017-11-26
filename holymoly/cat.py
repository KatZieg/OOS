#!/usr/bin/python
# -*- coding: utf-8 -*-

__author__ = 'K. Ziegler'

import pygame, sys
from pygame.locals import *

pygame.init()
fpsclock = pygame.time.Clock()

windowSurfaceObj = pygame.display.set_mode((640,480))
pygame.display.set_caption('Pygame Cheetsheat')

catSurfaceObj = pygame.image.load('cat.jpg')
redColor = pygame.Color(255,0,0)
greenColor = pygame.Color(0,255,0)
blueColor = pygame.Color(0,0,255)
whiteColor = pygame.Color(255,255,255)
mousex, mousey = 0,0

fontObj = pygame.font.Font('freesansbold.ttf', 32)
msg = 'Hello World'

soundObj = pygame.mixer.Sound('bounce.wav')

while True:
    windowSurfaceObj.fill(whiteColor)

    pygame.draw.polygon(windowSurfaceObj, greenColor, ((146,0),(291,106),(236, 277),(56,277),(0,106)))
    pygame.draw.circle(windowSurfaceObj, blueColor, (300,50), 20,0)
    pygame.draw.ellipse(windowSurfaceObj, redColor, (300,250, 40, 80), 1)
    pygame.draw.rect(windowSurfaceObj, redColor, (10,10, 50, 100))
    pygame.draw.line(windowSurfaceObj, blueColor, (60,160), (120,60),4)

    pixArr = pygame.PixelArray(windowSurfaceObj)
    for x in range(100, 200, 4):
        for y in range(100, 200, 4):
            pixArr[x][y] = redColor
    del pixArr

    windowSurfaceObj.blit(catSurfaceObj, (mousex, mousey))

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
        elif event.type ==MOUSEBUTTONUP:
            mousex, mousey = event.pos
            soundObj.play()
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




