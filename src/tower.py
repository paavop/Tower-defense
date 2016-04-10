'''
Created on 9.3.2016

@author: Paavo
'''
from spot import Spot
import math
class Tower(Spot):
    '''
    classdocs
    '''


    def __init__(self,price,power,myrange,x,y,index,speed):
        self.price=price
        self.power=power
        self.myrange=myrange
        self.target=None
        self.x=x
        self.y=y
        self.index=index
        self.lastshot=-2
        self.speed=speed
        
    def __str__(self):
        return "tower"
        
    def shot_x(self,time):
        x=0
        xd=0
        if(time/1000-self.lastshot<0.5 and self.target!=None):
            if (self.target.spot.x>self.target.spot.next.x):
                xd=self.target.get_frame()/50
            if (self.target.spot.x<self.target.spot.next.x):
                xd=-self.target.get_frame()/50
            x=-50*(self.x-self.target.spot.x+xd)*((time/1000-self.lastshot)/0.5)            
        return int(x)
    
    def shot_y(self,time):
        y=0
        yd=0
        if(time/1000-self.lastshot<0.5 and self.target!=None):
            if (self.target.spot.y>self.target.spot.next.y):
                yd=self.target.get_frame()/50
            if (self.target.spot.y<self.target.spot.next.y):
                yd=-self.target.get_frame()/50
            y=-50*(self.y-self.target.spot.y+yd)*((time/1000-self.lastshot)/0.5)            
        return int(y)
    
                    
    def distance(self,enemy):
        return math.sqrt(pow((self.x-enemy.spot.x),2)+pow((self.y-enemy.spot.y),2))
    
    def get_index(self):
        return self.index
    
    def shoot(self,enemies,time):
        if (self.target!=None):
            if(enemies[self.target.get_index()]!=None):
                if(self.distance(enemies[self.target.get_index()])<=self.myrange):
                    self.target=enemies[self.target.get_index()]
                    self.target.shot(self.power)
                    self.lastshot=time
                    return
                else:
                    for i in enemies:
                        if (enemies[i]!=None and self.distance(enemies[i])<=self.myrange):
                            self.target=enemies[i]
                            self.target.shot(self.power)
                            self.lastshot=time
            else:
                for i in enemies:
                    if (enemies[i]!=None and self.distance(enemies[i])<=self.myrange):
                        self.target=enemies[i]
                        self.target.shot(self.power)
                        self.lastshot=time
        else:
            for i in enemies:
                if (enemies[i]!=None and self.distance(enemies[i])<=self.myrange):
                    self.target=enemies[i]
                    self.target.shot(self.power)
                    self.lastshot=time

        
                              
        
                