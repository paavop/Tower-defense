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
peli.board.add_tower(5, 0)
peli.board.add_tower(4, 0)

print("   00 01 02 03 04 05 06 07 08 09 10 11 12 13 14 15 16 17 18 19 ")
for i in range(12):
    print (str(i).zfill(2),end=" ")
    for j in range(20):
        if isinstance(peli.board.get_spot(i, j),Tower):
            print("T  ", end="")
            continue
        if isinstance(peli.board.get_spot(i, j),Road):
            if(peli.board.get_spot(i, j).start):
                print("S  ", end="")
                continue
            if(peli.board.get_spot(i, j).goal):
                print("G  ", end="")
                continue
            
            print("R  ", end="")
            continue
        if isinstance(peli.board.get_spot(i, j),Spot):
            print("   ", end="") 
    print("")
    
    
    
