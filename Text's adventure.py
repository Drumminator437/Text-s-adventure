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
level2 = [
    "..................................",
    ".....XXXXX...XXXXX...XXXX.........",
    "XX........................XX......",
    "..XX......................XX......",
    "......XX.......XX.........XX......",
    "..........XX.......XX.....XX......",
    ".......................XXXXX......",
    "..................XXX.....XX......",
    "............XXX...........XX......",
    "XXXX...XXX................XXXXXXXX"
    ]
level3 = [
    "........................",
    "........................",
    "...............XX.......",
    "..........XXX...........",
    ".....XXX................",
    "XXXXXXXXXXXXXXXXXX..XXXX"
    ]
level4 = [
    "........................",
    "........................",
    "...............XX.......",
    "..........XXX...........",
    ".....XXX................",
    "XXXXXXXXXXXXXXXXXX..XXXX"
    ]
level5 = [
    "........................",
    "........................",
    "...............XX.......",
    "..........XXX...........",
    ".....XXX................",
    "XXXXXXXXXXXXXXXXXX..XXXX"
    ]
levels = [level0, level1, level2,level3,level4,level5]
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
jumppower = -10

onground = False

startgravity = False

camerax = 0
cameray = 0
scrollmargin = 250
def cameracode():
    global camerax, cameray
    screenplayerx = playerx - camerax

    if screenplayerx > screenW - scrollmargin:
        camerax = playerx - (screenW - scrollmargin)

    if screenplayerx < scrollmargin:
        camerax = playerx - scrollmargin

    if camerax < 0:
        camerax = 0
    screen_player_y = playery - cameray

    verticalmargin = 150

    if screen_player_y > screenH - verticalmargin:
        cameray = playery - (screenH - verticalmargin)

    if screen_player_y < verticalmargin:
        cameray = playery - verticalmargin

    if cameray < 0:
        cameray = 0

    max_camera = level_width() - screenW
    if camerax > max_camera:
        camerax = max_camera
def level_width():
    return len(levels[currentlevel][0]) * tilesize
def death_code():
    global running

    levelheight = len(levels[currentlevel]) * tilesize

    if playery > levelheight:
        running = False
def player_collision():
    global playery, vel_y, onground, playerx

    onground = False

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

                    if vel_y >= 0:
                        playery = tilerect.top - textRectmain.height
                        vel_y = 0
                        onground = True
def draw_level():
    startcollum = int(camerax // tilesize)
    endcollum = startcollum + (screenW // tilesize) + 2

    for rowindex, row in enumerate(levels[currentlevel]):
        for collumindex in range(startcollum, min(endcollum, len(row))):
            if row[collumindex] == "X":
                x = collumindex * tilesize - camerax
                y = rowindex * tilesize - cameray
                screen.blit(groundimage, (x, y))
def next_level():
    global currentlevel, playerx, playery, camerax, vel_y

    if playerx > level_width() - 60:
        currentlevel += 1

        if currentlevel >= len(levels):
            currentlevel = 0

        playerx = 100
        playery = 100
        vel_y = 0
        camerax = 0
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
    if keys[pygame.K_UP] and onground:
        vel_y = jumppower
        onground = False
    keys = pygame.key.get_pressed()

    if playerx < 0:
        playerx = 0
    

    Gravity()
    player_collision()
    next_level()
    cameracode()

    starttile = int(camerax // tilesize)
    endtile = int((camerax + screenW) // tilesize) + 2

    
    draw_level()

    textRectmain.x = playerx - camerax
    textRectmain.y = playery - cameray

    if currentlevel == 0:
        screen.blit(textbox, textRect)
    screen.blit(textboxmain, textRectmain)

    pygame.display.flip()
    clock.tick(FPS)

    death_code()

pygame.quit()
