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
        

    
                    
    def distance(self,enemy):
        return math.sqrt(pow((self.x-enemy.spot.x),2)+pow((self.y-enemy.spot.y),2))
    
    def get_index(self):
        return self.index
    
    def shoot(self,enemies,time):
        if (self.target!=None):
            if(enemies[self.target.get_index()]!=None):
                if(self.distance(enemies[self.target.get_index()])<=self.myrange):
                    self.mytarget=enemies[self.target.get_index()]
                    self.mytarget.shot(self.power)
                    self.lastshot=time
                    return
                else:
                    for i in enemies:
                        if (enemies[i]!=None and self.distance(enemies[i])<=self.myrange):
                            self.mytarget=enemies[i]
                            self.mytarget.shot(self.power)
                            self.lastshot=time
            else:
                for i in enemies:
                    if (enemies[i]!=None and self.distance(enemies[i])<=self.myrange):
                        self.mytarget=enemies[i]
                        self.mytarget.shot(self.power)
                        self.lastshot=time
        else:
            for i in enemies:
                if (enemies[i]!=None and self.distance(enemies[i])<=self.myrange):
                    self.mytarget=enemies[i]
                    self.mytarget.shot(self.power)
                    self.lastshot=time

        
                              
        
                