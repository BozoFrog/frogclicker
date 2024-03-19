import pygame
from pygame.locals import *
from sprites import *

pygame.init()

score = 0

def check(var):
    if score < var.price or var.maxlvl == True:
        var.canbuy = "dark red"

    else:
        var.canbuy = "dark green"
    return var.canbuy

def lvlup(var):
    if var.lvl < 10 and var.canbuy == "dark green":
        var.lvl += 1
        score -= var.price
        var.price = var.pricelist[var.lvl]
        var.maxlvl = False
    if var.lvl == 10:
        var.maxlvl = True
    return var, var.lvl, var.price, var.pricelsit, var.maxlvl, score

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

scoreprint = scorefont.render(f"{score}", True, pygame.color.Color("#E3963E"))

class shopitem:
    def __init__(self, price, lvl):
        self.price = price
        self.lvl = lvl
        self.maxlvl = False
        self.pricelist = []

click = shopitem(50, 0)
autoclick = shopitem(100, 0)

click.pricelist = [50, 60, 75, 100, 150, 200, 300, 500, 1000, 3000, 5000]

autoclick.pricelist = [100, 200, 300, 500, 750, 1000, 2000, 3000, 4000, 5000, 10000]

shopfont = pygame.font.SysFont("Times New roman", 40)
shopprint = shopfont.render("|Froggy Shop|", True, "black")

shopbg = pygame.Rect(1400, 160, 500, 800)
shopsign = pygame.Rect(1420, 180, 460, 100)

clicklvlup = pygame.Rect(1420, 330, 460, 100)
def clicktextfunc():
    clicktext = shopfont.rendgithuber(f"{click.lvl} : Clicks Level : {click.price}", True, "black")
    return clicktext

autoclicklvlup = pygame.Rect(1420, 480, 460, 100)
def autoclicktextfunc():
    autoclicktext = shopfont.render(f"{autoclick.lvl} : Autoclick Level : {autoclick.price}", True, "black")
    return autoclicktext


clicktext = shopfont.render(f"{click.lvl} : Clicks Level : {click.price}", True, "black")
autoclicktext = shopfont.render(f"{autoclick.lvl} : Autoclick Level : {autoclick.price}", True, "black")

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

    check(click)
    
    pygame.draw.rect(screen, click.canbuy, clicklvlup) 

    check(autoclick)

    pygame.draw.rect(screen, autoclick.canbuy, autoclicklvlup)

    clicktextfunc()
    autoclicktextfunc()
    
    screen.blit(shopprint, (1545, 205))
    screen.blit(clicktext, (1500, 360))
    screen.blit(autoclicktext, (1500, 515))

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

    pygame.time.set_timer(score += autoclick.lvl, 1000)

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
                score += click.lvl + 10
                scoreprint = scorefont.render(f"{score}", True, pygame.color.Color("#E3963E"))

            if clicklvlup.collidepoint(ev.pos):
                if click.lvl < 10 and click.canbuy == "dark green":
                    click.lvl += 1
                    score -= click.price
                    click.price = click.pricelist[click.lvl]
                    click.maxlvl = False
                if click.lvl == 10:
                    click.maxlvl = True
                clicktext = (shopfont.render(f"{click.lvl} : Clicks Level : {click.price}", True, "black"))

            if autoclicklvlup.collidepoint(ev.pos):
                if autoclick.lvl < 10 and autoclick.canbuy == "dark green":
                    autoclick.lvl += 1
                    score -= autoclick.price
                    autoclick.price = autoclick.pricelist[autoclick.lvl]
                    autoclick.maxlvl = False
                if autoclick.lvl == 10:
                    autoclick.maxlvl = True
                autoclicktext = (shopfont.render(f"{autoclick.lvl} : Autoclick Level : {autoclick.price}", True, "black"))

    pygame.display.update()
