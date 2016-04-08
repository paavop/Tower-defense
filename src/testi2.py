from Game import Game
from spot import Spot
from road import Road
from tower import Tower
import types
peli=Game()

        
for i in range(20):
    for j in range(20):
        if isinstance(peli.board.get_spot(i, j),Spot):
            print("S ", end="")
        if isinstance(peli.board.get_spot(i, j),Tower):
            print("T ", end="")
        if isinstance(peli.board.get_spot(i, j),Road):
            print("R ", end="")
    print("")
print("")  
        
peli.board.add_road(0, 0)

for i in range(20):
    for j in range(20):
        if isinstance(peli.board.get_spot(i, j),Tower):
            print("T ", end="")
            continue
        if isinstance(peli.board.get_spot(i, j),Road):
            print("R ", end="")
            continue
        if isinstance(peli.board.get_spot(i, j),Spot):
            print("S ", end="")
        
    print("")