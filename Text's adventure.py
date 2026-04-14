import pygame
import random

screenW = 1000
screenH = 400

black = (0,0,0)
white = (255,255,255)
red = (255,0,0)
blue = (0,0,255)

FPS = 60

pygame.init()

screen = pygame.display.set_mode([screenW,screenH],pygame.RESIZABLE)

clock = pygame.time.Clock()

font = pygame.font.SysFont(None, 40)

messegemain = "Text"
messege = "The adventure of "
messege2 = str(random.randint(0,100))

textbox = font.render(messege, True, blue)
textRect = textbox.get_rect()
textboxmain = font.render(messegemain, True, blue)
textRectmain = textboxmain.get_rect()

textRect.center = (500,200)
textRectmain.center = (650,200)

running = True 
while running:
    screen.fill((white))
    screenW = screen.get_width()
    screenH = screen.get_height()

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        textRectmain.x-=5
    if keys[pygame.K_RIGHT]:
        textRectmain.x+=5
    if keys[pygame.K_UP]:
        textRectmain.y-=5
    if keys[pygame.K_DOWN]:
        textRectmain.y+=5

    pygame.display.set_caption(f"Width = {screenW}, Hight = {screenH}")

    screen.blit(textbox, textRect)
    screen.blit(textboxmain, textRectmain)

    pygame.display.flip()

    clock.tick(FPS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False    
pygame.quit()