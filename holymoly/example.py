#!/usr/bin/python
# -*- coding: utf-8 -*-


import pygame
import random
pygame.init()
pygame.display.set_caption('Crash!')
pygame.mixer.music.load('bounce.wav')

#variables
window = pygame.display.set_mode((600, 600))
rectplace = pygame.draw.rect(window, (0, 0, 0),(0, 0, 100, 100))
counter = 200000
randx = random.randrange(100, 500)
randy = random.randrange(100, 500)
score = 0
life = 6
running = True

#Main Loop
while running:
    pos = pygame.mouse.get_pos()
    (pressed1,pressed2,pressed3) = pygame.mouse.get_pressed()
    if rectplace.collidepoint(pos)& pressed1==1:
        score=score+1
        print("Score ",score)
        pygame.mixer.music.play(0)
        counter=200000
        life=life+1
    if counter == 200000:
        rectplace = pygame.draw.rect(window, (0, 0, 0),(randx, randy, 100, 100))
        pygame.display.update()
        randx = random.randrange(100, 500)
        randy = random.randrange(100, 500)
        rectplace = pygame.draw.rect(window, (255, 0, 0),(randx, randy, 100, 100))
        counter=0
        pygame.display.update()
        life=life-1
        print ("lives: ",life)
    counter=counter+1
    if life == 0:
        running = False
    for event in pygame.event.get():
        if event.type == pygame.QUIT:

            running = False