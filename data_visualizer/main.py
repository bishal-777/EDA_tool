import pygame
import sys
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from tkinter import Tk, filedialog

pygame.init()
WIDTH,HEIGHT=1200,1080
screen=pygame.display.set_mode((WIDTH,HEIGHT))

WHITE=(255,255,255)
BLACK=(0,0,0)

font=pygame.font.Font(None,30)

def draw_text(text,x,y,color=BLACK):
    text_surface=font.render(text,True,color)
    screen.blit(text_surface,(x,y))

def load_dataset():
    Tk().withdraw()
    file_path=filedialog.askopenfilename(filetypes=[("CSV files","*.csv")])
    if file_path:
        return pd.read_csv(file_path)
    return None

def scatterplot(df,feature1,feature2):
    plt.figure()
    sns.scatterplot(x=df[feature1],y=df[feature2])
    plt.title(f"Scatter Plot of {feature1} vs {feature2}")
    plt.show()

def lineplot(df,feature1,feature2):
    plt.figure()
    sns.lineplot(x=df[feature1],y=df[feature2])
    plt.title(f"Line Plot of {feature1} vs {feature2}")
    plt.show()

def boxplot(df,feature):
    plt.figure()
    sns.boxplot(y=df[feature])
    plt.title(f"Boxplot of {feature}")
    plt.show()

def histogram(df,feature):
    plt.figure()
    sns.histplot(df[feature],bins=20)
    plt.title(f"Histogram of {feature}")
    plt.show()
    pass


def main():
    running=True
    df=None
    feature_selection=False
    scatter_selection=False
    line_selection=False  

    while running:
        screen.fill(WHITE)
        y_offset=50
        draw_text("Press 'L' to load dataset",50,y_offset)
        y_offset+=50

        if df is not None:
            if feature_selection or scatter_selection or line_selection:
                draw_text("Select a column:",50,y_offset)
                y_offset += 30
                for i,col in enumerate(df.columns):
                    key_label = str(i + 1) if i < 9 else chr(pygame.K_a + (i - 9))
                    draw_text(f"{key_label}. {col}", 50, y_offset)
                    y_offset+=30
                y_offset+=20
                draw_text("Press the corresponding key to select a column", 50, y_offset)
            else:
                y_offset+=30
                draw_text("Press 'H' for Histogram",50,y_offset)
                y_offset+=30
                draw_text("Press 'V' for Boxplot",50,y_offset)
                y_offset+=30
                draw_text("Press 'S' for Scatterplot",50,y_offset)
                y_offset+=30
                draw_text("Press 'P' for Line Plot",50,y_offset)
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                running=False
            elif event.type==pygame.KEYDOWN:
                if event.key==pygame.K_l:
                    df=load_dataset()
                elif df is not None:
                    if pygame.K_1<=event.key<=pygame.K_9:
                        index = event.key-pygame.K_1
                        index=event.key-pygame.K_a + 9
                    else:
                        continue
                    
                    if 0 <=index<len(df.columns):
                        if scatter_selection or line_selection:
                            if selected_x is None:
                                selected_x=df.columns[index]
                            else:
                                selected_y=df.columns[index]
                                if scatter_selection:
                                    scatterplot(df,selected_x,selected_y)
                                    scatter_selection=False
                                elif line_selection:
                                    lineplot(df,selected_x,selected_y)
                                    line_selection=False
                                selected_x,selected_y=None,None
                        else:
                            selected_column=df.columns[index]
                            if plot_type=='hist':
                                histogram(df,selected_column)
                            elif plot_type=='box':
                                boxplot(df,selected_column)
                            feature_selection=False
                    elif event.key==pygame.K_h:
                        feature_selection=True
                        plot_type='hist'
                    elif event.key==pygame.K_v:
                        feature_selection=True
                        plot_type='box'
                    elif event.key==pygame.K_s:
                        scatter_selection=True
                        selected_x,selected_y=None,None
                    elif event.key==pygame.K_p:
                        line_selection=True
                        selected_x,selected_y=None,None
            
            
    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()