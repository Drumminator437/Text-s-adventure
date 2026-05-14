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

pygame.display.set_caption("Text's Adventure")

level0 = [
    "........................",
    "........................",
    "........................",
    "........................",
    "........................",
    "XXXXXXXXXXXXXXXXXXXXXXXX"
]

level1 = [
    "....................................",
    "....................................",
    "..........................XX........",
    ".....................XX.............",
    "...............XXX..................",
    "XXXXXXXXXXXXXXXXXXXXXXXXXXXXX..XXXXX"
]

level2 = [
    "..................................",
    "...X.....X...XXXX....XXXX.........",
    "...XX.....................XX......",
    "......X...................XX......",
    "......XX...X...XX...XX....XX......",
    ".........................XXX......",
    ".......................XXXXX......",
    "..................XXX.....XX......",
    "............XXX...........XX......",
    "XXXX...XXX................XXXXXXXX"
]

level3 = [
    "....................................................................",
    "....................................................................",
    "....................................................................",
    "....................................................................",
    "X....XX...XX...XX.................................................XX",
    "XX..................X..............X.....X...X.X.X..X.............XX",
    "XXX......................XX...XXX......................X..X..X....XX",
    "XXXX..X..X...X............X.......................XX..............XX",
    "XXX.............X...XX....X...........XXX........................XXX",
    "XXX......................XX.........X.............................XX",
    "XX.........XX...........XXX.....XXXX..............................XX",
    "XX....XXX......XX......XXXX.....XX................................XX",
    "XXX.................XXXXXXXXX...XX....XXX...XX....................XX",
    "XXXX.....................XX.....XXX.............XXX...X...........XX",
    "XXX...X..X...............XX.....XX..XXX..........X........XXXXXXXXXX",
    "XXX.........XXX...XX....XXX....XXX.......XX......X..........XXXXXXXX",
    "....XXX.....XXX........XXXX...................XXXX...XX..X..XXXXXXXX",
    "......................XXXXX.................X...XX..........XX....XX",
    ".....................XXXXXX......X..X..X..XXX...XX..................",
    "XXXX...XXX...X.X..X..XXXXXXXXXXX................XXXX...X..XXXX...XXX"
]

level4 = [
    "....................................................................",
    "....................................................................",
    "....................................................................",
    ".............................XXXX...XX..........XX..................",
    "..............XX.....X....XX.XX.....XX....XXXX........XX............",
    "..........XX.....XX..........XX.....XXX........X..X......XX.........",
    "X....XXX.............XX....X.XX.....XX..XX............XX.....XX..XXX",
    "XX............XX.............XX.....XX.....XX.....................XX",
    "XXX...............X...XX.....XX.....XX.X.......XX.XX......XX......XX",
    "XXXX...XXX..............XX...XX.....XX.................XX........XXX",
    "XXX........X..XX.............XX.....XX......XX......X...........XXX",
    "XX.................XX........XX.....XX...XX.....XX...............XXX",
    "XX....XXXX..XX..XX.....XXX...XX.....XXX................XX.......XXXX",
    "XXX.........................XXX.....XXXX........XX........X..XX..XXX",
    "XXXX...........XX..........XXXX.....XX...XX...........X...........XX",
    ".......XXXXX........XX..XX...XX.....XX.......XX..XX.......XX..X..XXX",
    "................XX...........XX..........XX...........XX........XXXX",
    "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
]

level5 = [
    "XXXXX...................................................XXXX",
    "XXXX.....................................................XXX",
    "XXXX....................................................XXXX",
    "XXXXX..................................................XXXXX",
    "XXXX....................................................XXXX",
    "XXXX....................................................XXXX",
    "XXXXX....................................................XXX",
    "XXXXX...................................................XXXX",
    "XXXX.....................................................XXX",
    "XXXXX...................................................XXXX",
    "XXXX.....................................................XXX",
    "XXXX......XX....................................XX......XXXX",
    "XXXXXXX..............................................XXXXXXX",
    "XXXXXXXXX..........................................XXXXXXXXX",
    "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
]

levels = [level0, level1, level2, level3, level4, level5]
currentlevel = 0

screen = pygame.display.set_mode((screenW, screenH), pygame.RESIZABLE)
clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 40)

tilesize = 50
groundy = 300

groundimage = pygame.image.load("text.png")
groundimage = pygame.transform.scale(groundimage, (tilesize, tilesize))

bossrect = pygame.Rect((500,10,100,100))
bosshp = 100
bossimage = pygame.image.load("Boss.png")
bossimage = pygame.transform.scale(bossimage, (bossrect.width, bossrect.height))

lives = 3

mainmenuetext = "Press any key to start"
messegemain = "Text"
messege = "The adventure of "
deathtext = "YOU GOT ERASED"
deathtext2 = "GAME OVER"
gamestate = "play"

deathtextbox = font.render(deathtext, True, red)
deathtextbox2 = font.render(deathtext2, True, red)

deathtextrect = deathtextbox.get_rect()
deathtextrect2 = deathtextbox2.get_rect()

deathtextrect.center = (screenW // 2, screenH // 2 - 20)
deathtextrect2.center = (screenW // 2, screenH // 2 + 20)

livestext = font.render(f"Lives: {lives}", True, black)
livestextRect = livestext.get_rect()

textbox= font.render(messege, True, black)
textRect = textbox.get_rect()

livestextRect.center = (100,20)

mainmenutext = font.render(messege, True, black)
mainmenutextRect = mainmenutext.get_rect()

textboxmain = font.render(messegemain, True, black)
textRectmain = textboxmain.get_rect()

textRect.center = (500,200)
textRectmain.center = (650,200)

playerx = textRectmain.x
playery = textRectmain.y

bossjumpcooldown = 0
bossjumppower = -15
bossspeed = 2
bossvely = 0
bossgravity = 0.4
bossdamagecooldown = 0
bossphase = 1

playerhp = 100
playerdamage_cooldown = 0
knockbackx = 0
knockbacky = 0
player_iframes = 0
boss_iframes = 0

vel_y = 0
gravity = 0.5
jumppower = -10
counter = 0

onground = False
startgravity = False

camerax = 0
cameray = 0
scrollmargin = 250

pygame.mixer.init()
currentsong = ""


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


def save_code():
    if currentlevel > 0:
        levelspawn()


def level_width():
    return len(levels[currentlevel][0]) * tilesize


def death_code():
    global running, counter, lives, gamestate

    levelheight = len(levels[currentlevel]) * tilesize
    
    if currentlevel == 4:
        lives == 6
    if currentlevel >= 5:
        lives = playerhp
    if playery > levelheight:
        lives -= 1
        if lives <= 0:
            gamestate = "death"
        else:
            save_code()
    return lives, gamestate

def collision_y():
    global playery, vel_y, onground

    onground = False

    playerrect = pygame.Rect(playerx, playery, textRectmain.width, textRectmain.height)

    for rowIndex, row in enumerate(levels[currentlevel]):
        for columnIndex, tile in enumerate(row):

            if tile != "X":
                continue

            tilerect = pygame.Rect(
                columnIndex * tilesize,
                rowIndex * tilesize,
                tilesize,
                tilesize
            )

            if playerrect.colliderect(tilerect):

                if (playerrect.right > tilerect.left + 5 and
                    playerrect.left < tilerect.right - 5):

                    if vel_y > 0:
                        playery = tilerect.top - textRectmain.height
                        vel_y = 0
                        onground = True

                    elif vel_y < 0:
                        playery = tilerect.bottom
                        vel_y = 0

                    playerrect.y = playery


def collision_x():
    global playerx

    playerrect = pygame.Rect(playerx, playery, textRectmain.width, textRectmain.height)

    for rowIndex, row in enumerate(levels[currentlevel]):
        for columnIndex, tile in enumerate(row):

            if tile != "X":
                continue

            tilerect = pygame.Rect(
                columnIndex * tilesize,
                rowIndex * tilesize,
                tilesize,
                tilesize
            )

            if playerrect.colliderect(tilerect):
                if playerrect.centerx < tilerect.centerx:
                    playerx = tilerect.left - textRectmain.width
                else:
                    playerx = tilerect.right

                playerrect.x = playerx


def draw_level():
    startcollum = int(camerax // tilesize)
    endcollum = startcollum + (screenW // tilesize) + 2

    for rowindex, row in enumerate(levels[currentlevel]):
        for collumindex in range(startcollum, min(endcollum, len(row))):

            if row[collumindex] == "X":
                x = collumindex * tilesize - camerax
                y = rowindex * tilesize - cameray
                screen.blit(groundimage, (x, y))


def levelspawn():
    global playerx, playery, vel_y, camerax, cameray, boss_spawned

    boss_spawned = False

    for rowIndex in range(len(levels[currentlevel]) - 1, -1, -1):
        for columnIndex, tile in enumerate(levels[currentlevel][rowIndex]):

            if tile == "X":
                playerx = columnIndex * tilesize
                playery = rowIndex * tilesize - textRectmain.height
                vel_y = 0
                camerax = 0
                cameray = 0
                return


def next_level():
    global currentlevel, playerx, playery, camerax, vel_y, counter

    if playerx > level_width() - 60:
        currentlevel += 1
        counter = 0

        if currentlevel >= len(levels):
            currentlevel = 0

        levelspawn()
        vel_y = 0
        camerax = 0


def bossspawn():
    if currentlevel == 5:
        screen.blit(
            bossimage,
            (bossrect.x - camerax, bossrect.y - cameray)
        )
        boss()

def boss_collision():
    global bossvely

    for rowIndex, row in enumerate(levels[currentlevel]):
        for columnIndex, tile in enumerate(row):

            if tile != "X":
                continue

            tilerect = pygame.Rect(
                columnIndex * tilesize,
                rowIndex * tilesize,
                tilesize,
                tilesize
            )

            if bossrect.colliderect(tilerect):

                if bossvely > 0:
                    bossrect.bottom = tilerect.top
                    bossvely = 0

                elif bossvely < 0:
                    bossrect.top = tilerect.bottom
                    bossvely = 0
def boss():
    global bosshp, bossvely, bossjumpcooldown
    global playerhp, vel_y, playerx, playery
    global bossphase, player_iframes, boss_iframes

    if bosshp <= 50:
        bossphase = 2

    playerrect = pygame.Rect(playerx, playery, textRectmain.width, textRectmain.height)

    if player_iframes > 0:
        player_iframes -= 1

    if boss_iframes > 0:
        boss_iframes -= 1

    if bossphase == 1:
        speed = bossspeed
        jump_time = int(FPS * 2.5)
        boss_jump_power = bossjumppower
    else:
        speed = bossspeed * 1.5
        jump_time = int(FPS * 1.5)
        boss_jump_power = bossjumppower - 2

    bossjumpcooldown += 1
    if bossjumpcooldown >= jump_time:
        bossvely = boss_jump_power
        bossjumpcooldown = 0

    bossvely += bossgravity
    bossrect.y += bossvely

    if playerx > bossrect.x:
        bossrect.x += speed
    else:
        bossrect.x -= speed

    boss_collision()

    if playerrect.colliderect(bossrect):

        stomp = (
            vel_y > 0 and
            playery + textRectmain.height <= bossrect.top + 18
        )

        if stomp and boss_iframes == 0:
            bosshp -= 25
            bossvely = 6
            boss_iframes = FPS

            vel_y = jumppower

            print("Player HP:", playerhp, "Boss HP:", bosshp)

        elif not stomp and player_iframes == 0:
            playerhp -= 10 if bossphase == 1 else 14
            player_iframes = FPS 

            vel_y = -6

            print("Player HP:", playerhp, "Boss HP:", bosshp)
    
def changegamestate():
    global gamestate
    if playerhp <= 0:
        gamestate = "death"  
    if bosshp <=0:
        gamestate = "win"
def death():
    pygame.mixer.music.load("erase.mp3")
    pygame.mixer.music.set_volume(0.5)
    pygame.mixer.music.play(1)
    screen.fill(black)
    screen.blit(deathtextbox, deathtextrect)
    screen.blit(deathtextbox2, deathtextrect2)
def Gravity():
    global playery, vel_y

    vel_y += gravity
    playery += vel_y


def jumpcode(keys):
    global vel_y, onground

    if keys[pygame.K_UP] and onground:
        vel_y = jumppower
        onground = False
def mainmenu():
    global textRectmain, mainmenutextRect

    if currentlevel == 0:
        mainmenutextRect.center = (500,20)
        mainmenutext = font.render("Press any key to start", True, black)
        
        textRect.center = (500, 200)

        textRectmain.center = (650, 200)

        screen.blit(textbox, textRect)
        screen.blit(textboxmain, textRectmain)

        screen.blit(mainmenutext, mainmenutextRect)
    

    else:
        textRectmain.x = playerx - camerax
        textRectmain.y = playery - cameray

        screen.blit(textboxmain, textRectmain)
def musiccode():
    global currentsong

    if currentlevel == 0 and currentsong != "title":
        pygame.mixer.music.load("title theme.mp3")
        pygame.mixer.music.set_volume(0.5)
        pygame.mixer.music.play(-1)
        currentsong = "title"

    elif currentlevel >= 1 and currentlevel < 5 and currentsong != "main":
        pygame.mixer.music.load("main theme.mp3")
        pygame.mixer.music.set_volume(0.5)
        pygame.mixer.music.play(-1)
        currentsong = "main"
    elif currentlevel == 5 and currentsong != "boss":
        pygame.mixer.music.load("Boss theme.mp3")
        pygame.mixer.music.set_volume(0.5)
        pygame.mixer.music.play(-1)
        currentsong = "boss"
def win():
    screen.fill(black)

    wintext = font.render("YOU BEAT THE EVIL ERASER!", True, white)
    restarttext = font.render("Press 1 to restart or ESC to quit", True, white)
    creditstext = font.render("Made by Jacob Keating", True, white)

    winrect = wintext.get_rect(center=(screenW//2, screenH//2 - 20))
    restartrect = restarttext.get_rect(center=(screenW//2, screenH//2 + 20))
    creditsrect = creditstext.get_rect(center=(screenW//2 + 340, screenH//2 + 175))

    screen.blit(wintext, winrect)
    screen.blit(restarttext, restartrect)
    screen.blit(creditstext, creditsrect)


levelspawn()
running = True

while running:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN and currentlevel == 0:
            startgravity = True
            currentlevel += 1

    screen.fill(white)

    screenW = screen.get_width()
    screenH = screen.get_height()

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:
        playerx -= 5

    if keys[pygame.K_RIGHT]:
        playerx += 5

    if playerx < 0:
        playerx = 0

    jumpcode(keys)
    if gamestate == "play":
        Gravity()
        collision_y()
        collision_x()
    next_level()
    cameracode()
    draw_level()
    bossspawn()
    mainmenu()
    musiccode()
    if currentlevel >=1:
        livestext = font.render(f"Lives: {lives}", True, black)
        screen.blit(livestext,livestextRect)

    pygame.display.flip()
    clock.tick(FPS)
    changegamestate()

    if gamestate == "death":
        death()
        pygame.display.flip()
        pygame.time.wait(5000)
        running = False
    else:
        pygame.display.flip()
    
    if gamestate == "win":
        waiting = True

        while waiting:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    waiting = False

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_1:
                        currentlevel = 1
                        gamestate = "play"

                        bosshp = 100
                        playerhp = 100
                        lives = 3

                        levelspawn()

                        waiting = False
                        break
                        

                    if event.key == pygame.K_ESCAPE:
                        running = False
                        waiting = False

            win()
            pygame.display.flip()
            clock.tick(FPS)
        
                
    death_code()

pygame.quit()
