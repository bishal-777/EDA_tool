import pygame
import pandas as pd
from tkinter import filedialog

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

def load_dataset():
     file_path=filedialog.askopenfilename(filetypes=[('CSV files','*.csv')])
     if file_path:
          return pd.read_csv(file_path)
     return None

running=True
while running==True:
        screen.fill(background)

        screen.blit(img_headline,(350,20))
        screen.blit(img_subheadline,(20,80))

        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                running=False
            elif event.type==pygame.KEYDOWN:
                 if event.key==pygame.K_l:
                      df=load_dataset()

        pygame.display.update()


pygame.quit()
