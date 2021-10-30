#Imports
import pygame
import sys
from pygame.locals import *
import random
import time

#Initialzing
pygame.init()

#Setting up FPS
FPS = 60
FramePerSec = pygame.time.Clock()

#Creating colors
BLUE  = (0, 0, 255)
RED   = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

#Other Variables for use in the program
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 800
SPEED = 5
SCORE = 0

#Create a white screen
DISPLAYSURF = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
DISPLAYSURF.fill(BLUE)
pygame.display.set_caption("Gra")
background = pygame.image.load("tlo.png")

class Tlo(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("kolko.png")
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_threshold(background, (255, 202, 24), (1, 1, 1, 255))
        self.rect.center = (160, 520)

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("Player.png")
        self.rect = self.image.get_rect()
        self.rect.center = (160, 520)

    def move(self):
        pressed_keys = pygame.key.get_pressed()

        if self.rect.top > 0:
            if pressed_keys[K_UP]:
                self.rect.move_ip(0, -5)
        if self.rect.bottom < SCREEN_HEIGHT:
            if pressed_keys[K_DOWN]:
                self.rect.move_ip(0, 5)

        if self.rect.left > 0:
            if pressed_keys[K_LEFT]:
                self.rect.move_ip(-5, 0)
        if self.rect.right < SCREEN_WIDTH:
            if pressed_keys[K_RIGHT]:
                self.rect.move_ip(5, 0)


all_sprites = pygame.sprite.Group()
P1 = Player()
T1 = Tlo()
TG = pygame.sprite.Group()
TG.add(T1)
all_sprites.add(P1)

T1.mask = pygame.mask.from_threshold(background, (255, 0, 0), (13, 13, 13, 255))

#for sprite in objects:
 #       sprite.mask = pygame.mask.from_threshold(sprite.image, pygame.Color('yellow'), (1, 1, 1, 255))



while True:

    # Cycles through all events occuring
    for event in pygame.event.get():

        if event.type == QUIT:
            pygame.quit()
            sys.exit()
   # DISPLAYSURF.blit(background, (0, 0))

    if pygame.sprite.spritecollide(P1, TG, pygame.sprite.collide_mask):
        print(True)
    else:
        print(False)
    DISPLAYSURF.blit(T1.image, T1.rect)
    for entity in all_sprites:
        entity.move()
        DISPLAYSURF.blit(entity.image, entity.rect)

    pygame.display.update()
    FramePerSec.tick(FPS)