import pygame
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
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

def histogram(df,feature):
    plt.figure(figsize=(8,4))
    plt.hist(df[feature],bins=20)
    plt.title(f"Histogram of {feature}")
    plt.show()

def boxplot(df,feature):
     plt.figure(figsize=(8,8))
     sns.boxplot(df[feature])
     plt.title(f"Boxplot of {feature}")
     plt.show()

def barchart(df,feature):
     plt.figure(figsize=(8,4))
     sns.countplot(x=df[feature])
     plt.title(f"Countplot of {feature}")
     plt.show()

def piechart(df,feature):
     counts=df[feature].value_counts()
     plt.figure(figsize=(8,4))
     plt.pie(counts,labels=counts.index)
     plt.title(f"Pie Chart of {feature}")
     plt.show()

def scatterplot(df,feature1,feature2):
     plt.figure(figsize=(8,4))
     sns.scatterplot(x=df[feature1],y=df[feature2])
     plt.title(f"Scatterplot of {feature1} and {feature2}")
     plt.show()

def pairplot(df,feature1,feature2):
     plt.figure(figsize=(20,12))
     sns.pairplot(data=df,vars=[feature1,feature2])
     plt.title(f"Pairplot of {feature1} and{feature2}")
     plt.show()


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
