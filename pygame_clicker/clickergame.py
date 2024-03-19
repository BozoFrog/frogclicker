import pygame
from pygame.locals import *
import colorama
from sprites import *

pygame.init()

def check(var):
    if score < self.price:
    self.canbuy = "dark red"

else:
    self.canbuy = "dark green"

clock = pygame.time.Clock()

scrw = 1920
scrh = 1080
scrs = (scrw, scrh)

scr_flags = pygame.FULLSCREEN | pygame.NOFRAME

screen = pygame.display.set_mode(scrs, scr_flags)

scr_col = pygame.color.Color("grey")

frogfloat = 100

scorefontsize = 80

scorefont = pygame.font.SysFont("comicsansms", scorefontsize)

score = 0

scoreprint = scorefont.render(f"{score}", True, pygame.color.Color("#E3963E"))

class shopitem:
    def __init__(self, price, lvl):
        self.price = price
        self.lvl = lvl

click = shopitem(50, 1)

autoclick = shopitem(100, 0)

shopfont = pygame.font.SysFont("Times New roman", 40)
shopprint = shopfont.render("|Froggy Shop|", True, "black")

shopbg = pygame.Rect(1400, 160, 500, 800)
shopsign = pygame.Rect(1420, 180, 460, 100)

clicklvlup = pygame.Rect(1420, 330, 460, 100)
clicktext = shopfont.render(f"{click.lvl} : Clicks Level : {click.price}", True, "black")

running = True

while running:
    clock.tick(60)

    screen.fill(scr_col)

    screen.blit(exspr, (1895, 10))

    screen.blit(flscrspr, (1875, 10))

    screen.blit(minspr, (1855, 10))
    
    screen.blit(pointspr, (0, 0))

    if score < 10:
        scorepos = 1390

    elif score < 100:
        scorepos = 1360

    elif score < 1000:
        scorepos = 1330

    elif score < 10000:
        scorepos = 1310

    elif score < 100000:
        scorepos = 1310

    if score < 10000:
        scorefontsize = 80
        scoreypos = 15
        scorefont = pygame.font.SysFont("comicsansms", scorefontsize)

    elif score < 100000:
        scorefontsize = 65
        scoreypos = 20
        scorefont = pygame.font.SysFont("comicsansms", scorefontsize)

    elif score < 1000000:
        scorefontsize = 50
        scoreypos = 30
        scorefont = pygame.font.SysFont("comicsansms", scorefontsize)

    screen.blit(scoreprint, (scorepos, scoreypos))

    pygame.draw.rect(screen, pygame.color.Color("#E3963E"), shopbg)
    pygame.draw.rect(screen, pygame.color.Color("#D8B589"), shopsign)

    pygame.draw.rect(screen, click.canbuy, clicklvlup) 

    screen.blit(shopprint, (1545, 205))
    screen.blit(clicktext, (1500, 360))

    if frogfloat >= 100:
        frogup = False

    elif frogfloat <= 55:
        frogup = True

    if frogup:
        frogfloat += 1

    else:
        frogfloat -= 1

    screen.blit(frogspr, (0, frogfloat))

    frog = pygame.Rect(208, 120 + frogfloat, 855, 720)

    for ev in pygame.event.get():
        if ev.type == KEYDOWN:
            if ev.key == K_ESCAPE:
                running = False

        if ev.type == MOUSEBUTTONDOWN and ev.button == 1:
            if ex.collidepoint(ev.pos):
                running = False

            if flscr.collidepoint(ev.pos):
                pygame.display.toggle_fullscreen()

            if mini.collidepoint(ev.pos):
                pygame.display.iconify()

            if frog.collidepoint(ev.pos):
                score += click.lvl
                scoreprint = scorefont.render(f"{score}", True, pygame.color.Color("#E3963E"))

    pygame.display.update()