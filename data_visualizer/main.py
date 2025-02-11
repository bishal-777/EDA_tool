import pygame
import sys
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

pygame.init()
WIDTH,HEIGHT=1200,1080
screen=pygame.display.set_mode((WIDTH,HEIGHT))

WHITE=(255,255,255)
BLACK=(0,0,0)

font=pygame.font.Font(None,30)

def draw_text(text,x,y,color=BLACK):
    text_surface=font.render(text,True,color)
    screen.blit(text_surface,(x,y))

"""
def draw_histogram(df,feature):
    plt.figure()
    sns.histplot(df[feature],bins=20)
    plt.title(f"Histogram of {feature}")
    plt.show()
    pass
"""


def main():
    running=True

    while running:
        screen.fill(WHITE)
        y_offset=50
        draw_text("Press 'L' to load dataset",50,y_offset)

        pygame.display.flip()
        
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                sys.exit()

        


        #function call
        #draw_histogram(df,feature)



if __name__ == "__main__":
    main()