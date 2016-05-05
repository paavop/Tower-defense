import pygame
from spot import Spot
from tower import Tower
from road import Road

class Board(object):
    


    def __init__(self):
        self.size=20
        self.length=12
        self.board={}
        self.towers=0
        self.towerlimit=10
        
        for i in range(12):
            for j in range(20):
                self.board[i,j]=Spot()
                
        self.lastroad=None
    def get_towercount(self):
        return(str(self.towers)+"/"+str(self.towerlimit))
    def get_tower_ratio(self):
        return(self.towers/self.towerlimit)
    
    def add_tower(self,x,y,price,power,myrange,index,speed,money,pic,name):
        if not (isinstance(self.board[x,y],Road)):
            if not (isinstance(self.board[x,y],Tower)):
                
                self.board[x,y]=Tower(price,power,myrange,x,y,index,speed,pic,name)
                self.towers+=1
                return(str(name)+" built")
               
            else:
                return("Can't build on another tower")
        else:
            return("Can't build on road")
            
    def remove_tower(self,x,y):
        if  (isinstance(self.board[x,y],Tower)):
            self.board[x,y]=Spot()
            self.towers-=1
            return("Tower removed")
        else:
            return("You can only remove towers")
        
    def add_road(self,x,y):
        self.board[x,y]=Road(x,y)
        #print("Road added to  "+str(x)+" "+str(y))
        if self.lastroad==None:
            self.board[x,y].def_start()
        if self.lastroad:
            self.lastroad.def_next(self.board[x,y])
            self.lastroad.goal=False
        self.lastroad=self.board[x,y]
        
            
    def get_spot(self,x,y):
        return self.board[x,y]
    
    
        
        