import pygame, sys
import random
from pygame.locals import QUIT

pygame.init()
screen = pygame.display.set_mode((600, 600))
pygame.display.set_caption('Hello World!')
background = pygame.transform.scale(pygame.image.load('green_background.png'),(600,600))
flower = pygame.transform.scale(pygame.image.load('flower.png'),(50,50))
bee = pygame.transform.scale(pygame.image.load('bee.png'),(50,50))
flowerbox = pygame.Rect(random.randint(0,600),random.randint(0,600),50,50)
beebox = pygame.Rect(300,300,50,50)

moveflower = pygame.USEREVENT
score  = 0

clock = 0
font = pygame.font.SysFont('sans',30)


def movement():
    keypress = pygame.key.get_pressed()
    if keypress[pygame.K_w]:
        beebox.y = beebox.y-2
    if keypress[pygame.K_s]:
        beebox.y = beebox.y+2
    if keypress[pygame.K_a]:
        beebox.x = beebox.x-2
    if keypress[pygame.K_d]:
        beebox.x = beebox.x+2
#Creating event 
        
def loadscreen():
    screen.blit(background,(0,0))
    screen.blit(bee,(beebox.x,beebox.y))

    screen.blit(bee,(beebox.x,beebox.y))
    screen.blit(flower,(flowerbox.x,flowerbox.y))
    scorebox = font.render('Score = '+str(score),True,'white')
    screen.blit(scorebox,(0,0))



while True:
    loadscreen()

    movement()
    while clock <=10:
        pygame.time.wait(1000)
        clock  = clock+1
    if clock == 10:
        print('GAMEOVER')
    for event in pygame.event.get():
        if event.type == QUIT:
           pygame.quit()
           sys.exit()
        if beebox.colliderect(flowerbox):
            flowerbox.x = random.randint(0,400)
            flowerbox.y = random.randint(0,400)
            score  = score+1
   
           
    pygame.display.update()