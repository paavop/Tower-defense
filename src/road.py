'''
Created on 9.3.2016

@author: Paavo
'''
from spot import Spot

class Road(Spot):
    '''
    classdocs
    '''


    def __init__(self):
        self.next=None
        self.start=False
        self.goal=False
        
    def def_start(self):
        self.start=True
        
    def def_goal(self):
        self.goal=True
        
    def __str__(self):
        return "road"
        
    
        