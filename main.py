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
font3=pygame.font.SysFont('arial',30)

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

def countplot(df,feature):
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

def lineplot(df,feature1,feature2):
     plt.figure(figsize=(8,4))
     sns.lineplot(x=df[feature1],y=df[feature2])
     plt.title(f"Lineplot of {feature1} and{feature2}")
     plt.show()


running=True
df=None
select_analysis=None
select_plot=None
select_feature=None
select_feature2=None


while running==True:
        screen.fill(background)

        screen.blit(img_headline,(350,20))

        if df is None:
          screen.blit(img_subheadline,(20,80))

        elif select_analysis is None:
             img_select=font3.render('Press U for Univariate analysis',True,BLACK)             
             screen.blit(img_select,(20,80))
             img_select=font3.render('Press B for Bivariate analysis',True,BLACK)
             screen.blit(img_select,(20,120))

        elif select_analysis=='uni' and select_plot==None:
             img_select=font3.render('Press H for Histogram',True,BLACK)             
             screen.blit(img_select,(20,80))
             img_select=font3.render('Press B for Boxplot',True,BLACK)
             screen.blit(img_select,(20,110))
             img_select=font3.render('Press C for Countplot',True,BLACK)             
             screen.blit(img_select,(20,140))
             img_select=font3.render('Press P for Piechart',True,BLACK)
             screen.blit(img_select,(20,170)) 
             img_select = font3.render('Press M to return to Main Menu', True, BLACK)  # Return to main menu option
             screen.blit(img_select, (20, 200)) 

        elif select_analysis=='bi' and select_plot==None:
             img_select=font3.render('Press S for Scatterplot',True,BLACK)             
             screen.blit(img_select,(20,80))
             img_select=font3.render('Press P for lineplot',True,BLACK)
             screen.blit(img_select,(20,110))
             img_select = font3.render('Press M to return to Main Menu', True, BLACK)  # Return to main menu option
             screen.blit(img_select, (20, 200))

        elif select_feature==None:
             img_feature=font3.render('Select the feature by entering designated key',True,BLACK)
             screen.blit(img_feature,(20,80))

             y=110
             for i,col in enumerate(df.columns):
                  if i<9:
                       key=str(i+1)
                  else:
                       key=chr(pygame.K_a+(i-9))    #works by increasing ascii value for differnt characters         
                  img_col=font3.render(f"{key}.{col}",True,BLACK)
                  screen.blit(img_col,(20,y))
                  y+=40
        
        pygame.display.update()
        
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                running=False

            elif event.type==pygame.KEYDOWN:
                 if event.key==pygame.K_l:
                      df=load_dataset()

                 elif df is not None and select_analysis is None:
                      if event.key==pygame.K_u:
                           select_analysis='uni'
                      if event.key==pygame.K_b:
                           select_analysis='bi'
            
                 elif select_analysis=='uni' and select_plot==None:
                      if event.key==pygame.K_h:
                           select_plot='hist'
                      elif event.key==pygame.K_b:
                           select_plot='box'
                      elif event.key==pygame.K_c:
                           select_plot='count'
                      elif event.key==pygame.K_p:
                           select_plot='pie'
                      elif event.key == pygame.K_m:
                           select_analysis = None

                 elif select_analysis=='bi' and select_plot==None:
                      if event.key==pygame.K_s:
                           select_plot='scatter'
                      elif event.key==pygame.K_p:
                           select_plot='line'
                      elif event.key == pygame.K_m:
                           select_analysis = None
                           
                 elif select_plot is not None and select_feature is None:
                     index=None
                     if pygame.K_1<=event.key<=pygame.K_9:
                         index=event.key-pygame.K_1
                     elif pygame.K_a<=event.key<=pygame.K_z:
                         index=event.key-pygame.K_a+9
                     if index is not None and 0<=index<len(df.columns):
                         select_feature=df.columns[index]
                         if select_analysis=='uni':
                             if select_plot=='hist':
                                 histogram(df,select_feature)
                             elif select_plot=='box':
                                 boxplot(df,select_feature)
                             elif select_plot=='count':
                                 countplot(df,select_feature)
                             elif select_plot=='pie':
                                 piechart(df,select_feature)
                             select_feature,select_plot=None,None
                         elif select_analysis=='bi':
                             select_feature2=None
                 elif select_feature is not None and select_feature2 is None:
                     index=None
                     if pygame.K_1<=event.key<=pygame.K_9:
                         index=event.key-pygame.K_1
                     elif pygame.K_a<=event.key<=pygame.K_z:
                         index=event.key-pygame.K_a+9
                     if index is not None and 0<=index<len(df.columns):
                         select_feature2=df.columns[index]
                         if select_plot=='scatter':
                             scatterplot(df,select_feature,select_feature2)
                         elif select_plot=='line':
                             lineplot(df,select_feature,select_feature2)
                         select_feature,select_feature2,select_plot=None,None,None

pygame.quit()
