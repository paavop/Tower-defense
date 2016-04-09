'''
Created on 9.3.2016

@author: Paavo
'''
from spot import Spot

class Tower(Spot):
    '''
    classdocs
    '''


    def __init__(self,price,power,range):
        self.price=price
        self.power=power
        self.range=range
        
    def __str__(self):
        return "tower"
        