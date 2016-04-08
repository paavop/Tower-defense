'''
Created on 9.3.2016

@author: Paavo
'''
from spot import Spot

class Tower(Spot):
    '''
    classdocs
    '''


    def __init__(self):
        self.value=0;
        
    def __str__(self):
        return "tower"
        