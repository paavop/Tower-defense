import pygame
from spot import Spot
from tower import Tower
from road import Road

class Board(object):
    


    def __init__(self):
        self.size=20
        self.board={}
        
        
        for i in range(20):
            for j in range(20):
                self.board[i,j]=Spot()
                
        self.noroad=True
            
    def add_tower(self,x,y):
        if(self.board[x,y]!=Tower and self.board[x,y]!=Road):
            self.board[x,y]=Tower()
        
    def add_road(self,x,y):
        self.board[x,y]=Road()
        if self.noroad:
            self.board[x,y].def_start()
            self.noroad=False
            
    def get_spot(self,x,y):
        return self.board[x,y]
    
    
        
        