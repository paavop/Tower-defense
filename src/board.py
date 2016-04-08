import pygame
from spot import Spot
from tower import Tower
from road import Road

class Board(object):
    


    def __init__(self):
        self.size=20
        self.length=12
        self.board={}
        
        
        for i in range(12):
            for j in range(20):
                self.board[i,j]=Spot()
                
        self.lastroad=None
            
    def add_tower(self,x,y):
        if not (isinstance(self.board[x,y],Road)):
            if not (isinstance(self.board[x,y],Tower)):
                self.board[x,y]=Tower()
            else:
                print("Can't build on another tower")
        else:
            print("Can't build on road")
        
    def add_road(self,x,y):
        self.board[x,y]=Road()
        if self.lastroad==None:
            self.board[x,y].def_start()
        if self.lastroad:
            self.lastroad.def_next(self.board[x,y])
            self.lastroad.goal=False
        self.lastroad=self.board[x,y]
        
            
    def get_spot(self,x,y):
        return self.board[x,y]
    
    
        
        