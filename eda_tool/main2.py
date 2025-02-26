import pygame

pygame.init()

WIDTH,HEIGHT=1200,1000
screen=pygame.display.set_mode((WIDTH,HEIGHT))

WHITE=(255,255,255)
BLACK=(0,0,0)
CYAN=(0,255,255)

font1=pygame.font.SysFont('arial',50,bold=True)
font2=pygame.font.SysFont('arial',40)
img_headline=font1.render('Welcome to EDA app!',True,BLACK)
img_subheadline=font2.render('Press L to load dataset',True,BLACK)

background=CYAN

running=True
while running==True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False

    screen.fill(background)

    screen.blit(img_headline,(350,20))
    screen.blit(img_subheadline,(20,80))

    pygame.display.update()


pygame.quit()
