import pygame
import random
from pygame.locals import *

screenW = 1000
screenH = 400

black = (0,0,0)
white = (255,255,255)
red = (255,0,0)
blue = (0,0,255)

FPS = 60


pygame.init()
level0 = [
    "........................",
    "........................",
    "........................",
    "........................",
    "........................",
    "XXXXXXXXXXXXXXXXXX..XXXX"
    ]
level1 = [
    "........................",
    "........................",
    "...............XX.......",
    "..........XXX...........",
    ".....XXX................",
    "XXXXXXXXXXXXXXXXXX..XXXX"
    ]

levels = [level0, level1]
currentlevel = 0


screen = pygame.display.set_mode((screenW, screenH), pygame.RESIZABLE)
clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 40)

tilesize = 50
groundy = 300

groundimage = pygame.image.load("text.png")
groundimage = pygame.transform.scale(groundimage, (tilesize, tilesize))

messegemain = "Text"
messege = "The adventure of "

textbox = font.render(messege, True, blue)
textRect = textbox.get_rect()

textboxmain = font.render(messegemain, True, blue)
textRectmain = textboxmain.get_rect()

textRect.center = (500,200) 
textRectmain.center = (650,200)

playerx = textRectmain.x 
playery = textRectmain.y

vel_y = 0
gravity = 0.5
jump_power = -10

on_ground = False

startgravity = False

camerax = 0
scrollmargin = 250
def player_collision():
    global playery, vel_y, on_ground

    on_ground = False

    playerrect = pygame.Rect(
        playerx,
        playery,
        textRectmain.width,
        textRectmain.height
    )

    for rowIndex, row in enumerate(levels[currentlevel]):
        for columnIndex, tile in enumerate(row):

            if tile == "X":
                tilerect = pygame.Rect(
                    columnIndex * tilesize,
                    rowIndex * tilesize,
                    tilesize,
                    tilesize
                )

                if playerrect.colliderect(tilerect):

                    if vel_y > 0:
                        playery = tilerect.top - textRectmain.height
                        vel_y = 0
                        onground = True
def draw_level():
    for row_index, row in enumerate(levels[currentlevel]):
        for col_index, tile in enumerate(row):
            if tile == "X":
                x = col_index * tilesize - camerax
                y = row_index * tilesize
                screen.blit(groundimage, (x, y))
def Gravity():
    global playery, vel_y

    vel_y += gravity
    playery += vel_y
running = True
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            startgravity = True

    screen.fill(white)

    screenW = screen.get_width()
    screenH = screen.get_height()

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:
        playerx -= 5
    if keys[pygame.K_RIGHT]:
        playerx += 5
    if keys[pygame.K_UP] and on_ground:
        vel_y = jump_power
        onground = False
    keys = pygame.key.get_pressed()

    if playerx < 0:
        playerx = 0
    

    player_collision()
    Gravity()

    screen_player_x = playerx - camerax

    if screen_player_x > screenW - scrollmargin:
        camerax = playerx - (screenW - scrollmargin)

    if screen_player_x < scrollmargin:
        camerax = playerx - scrollmargin

    if camerax < 0:
        camerax = 0

    starttile = int(camerax // tilesize)
    endtile = int((camerax + screenW) // tilesize) + 2

    
    draw_level()

    textRectmain.x = playerx 
    textRectmain.y = playery

    screen.blit(textbox, textRect)
    screen.blit(textboxmain, textRectmain)

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
