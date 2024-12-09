import pygame 
import os 

pygame.font.init()

WIDTH = 900
HEIGHT = 500 

display_surface = pygame.display.set_mode((900,500))

WHITE = (255,255,255)
BLACK= (0,0,0)
RED = (255,0,0)
YELLOW = (255,255,0)

BORDER = pygame.Rect(WIDTH//2 -5,0 ,10,HEIGHT)
HEALTH_FONT = pygame.font.SysFont('calibri',40)
WINNER_FONT = pygame.font.SysFont('calibri',100)

SPACE = pygame.transform.scale(pygame.image.load(os.path.join('Assets','bgspace.png')),(WIDTH,HEIGHT))

FPS = 60
VEL = 5

BULLET_VEL = 7
MAX_BULLET = 3

SPACESHIP_WIDTH,SPACESHIP_HEIGHT = 55,40

YELLOW_HIT = pygame.USEREVENT + 1
RED_HIT =pygame.USEREVENT + 2

YELLOW_SPACESHIP_IMAGE =pygame.image.load(os.path.join('Assets','yellow.png'))

YELLOW_SPACESHIP = pygame.transform.rotate(pygame.transform.scale(YELLOW_SPACESHIP_IMAGE,(SPACESHIP_WIDTH,SPACESHIP_HEIGHT)),90)