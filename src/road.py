'''
Created on 9.3.2016

@author: Paavo
'''
from spot import Spot

class Road(Spot):
    '''
    classdocs
    '''


    def __init__(self,x,y):
        self.x=x
        self.y=y
        self.next=None
        self.start=False
        self.goal=True
        
    def def_start(self):
        self.start=True
        
    def def_goal(self):
        self.goal=True
    
    def def_next(self,road):
        self.next=road
    def get_next(self):
        return self.next
        
    def __str__(self):
        return "road"
        
    
        