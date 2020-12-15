# Bubble Sort Visualization
# Rohan Deswal

import pygame
from random import randint

pygame.init()

display_width = 800
display_height = 500

gameDisplay = pygame.display.set_mode((display_width,display_height))

pygame.display.set_caption('BUBBLE_SORT')

clock = pygame.time.Clock()

def change_range(OldValue,OldMin,OldMax,NewMin,NewMax):
    return int((((OldValue - OldMin) * (NewMax - NewMin)) / (OldMax - OldMin)) + NewMin)

def game_loop():
    crashed = False

    arr = []
    arr_colors = []

    i = 0
    j = 0
    width = 20   
    len_done = False
    
    for lengths in range(0,int(display_width),width):
        arr.append(randint(0,display_height))
    for colors in range(0,len(arr)):
        c = change_range(arr[colors],0,display_height,0,255)
        arr_colors.append(c)

    while not crashed:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.display.quit()
        gameDisplay.fill((0,151,0))
        for lengths in range(0,len(arr)):
                c = arr_colors[lengths]
                pygame.draw.rect(gameDisplay,(c,c,c),[width * lengths,display_height - arr[lengths],width,arr[lengths]])
        
        if len_done == False:
            if arr[j] > arr[j+1]:
                arr[j],arr[j+1] = arr[j+1],arr[j]

        if len_done and arr_colors[j] > arr_colors[j+1]:
            arr_colors[j],arr_colors[j+1] = arr_colors[j+1],arr_colors[j]
        
        j += 1
        if j == len(arr)- i - 1:
            i += 1
            j = 0 

        if i >= len(arr) - 1:
            if len_done:
                game_loop()
            i = 0
            len_done = True
            j = 0


        

            
        pygame.display.update()
        clock.tick(60)

game_loop()
pygame.quit
quit()

            
