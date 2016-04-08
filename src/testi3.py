import pygame
from game import Game
from spot import Spot
from road import Road
from tower import Tower



peli=Game()

        

for i in range(7):
    peli.board.add_road(5, i)
for i in range (3):
    peli.board.add_road(5+i,7)
for i in range (6):
    peli.board.add_road(8,7+i)
for i in range (3):
    peli.board.add_road(8-i,13)
for i in range(7):
    peli.board.add_road(5, 13+i)
    
peli.board.add_tower(4, 0)
peli.board.add_tower(11, 7)
peli.board.add_tower(6, 18)

pygame.init()
    
logo = pygame.image.load("logo32x32.png")
torni=pygame.image.load("tower.png")
tie=pygame.image.load("road.png")
tie_start=pygame.image.load("road_start.png")
tie_goal=pygame.image.load("road_goal.png")
maa=pygame.image.load("empty.png")
pygame.display.set_icon(logo)
pygame.display.set_caption("Tower defense")

size=1000
    
    # create a surface on screen that has the size of 240 x 180
screen_width=size
screen_height=size-400
screen = pygame.display.set_mode((screen_width,screen_height))

screen.fill((200,191,231))
    


pygame.display.flip()

print("   00 01 02 03 04 05 06 07 08 09 10 11 12 13 14 15 16 17 18 19 ")
for i in range(12):
    print (str(i).zfill(2),end=" ")
    for j in range(20):
        if isinstance(peli.board.get_spot(i, j),Tower):
            print("T  ", end="")
            screen.blit(torni,(50*j,50*i))
            continue
        if isinstance(peli.board.get_spot(i, j),Road):
            if(peli.board.get_spot(i, j).start):
                print("S  ", end="")
                screen.blit(tie_start,(50*j,50*i))
                continue
            if(peli.board.get_spot(i, j).goal):
                print("G  ", end="")
                screen.blit(tie_goal,(50*j,50*i))
                continue
            
            print("R  ", end="")
            screen.blit(tie,(50*j,50*i))
            continue
        if isinstance(peli.board.get_spot(i, j),Spot):
            print("   ", end="") 
            screen.blit(maa,(50*j,50*i))
    print("")
    
    
pygame.display.flip()

running=True

while running:
    for event in pygame.event.get():
            # only do something if the event is of type QUIT
            if event.type == pygame.QUIT:
                # change the value to False, to exit the main loop
                running = False