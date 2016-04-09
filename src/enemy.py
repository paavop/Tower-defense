

class Enemy(object):
    


    def __init__(self, name, hp, speed,spot):
        self.name=name
        self.hp=hp
        self.speed=speed
        self.spot=spot
    
    def move(self):
        next=self.spot.get_next()
        self.spot=next
    
    def shot(self,hplost):
        self.hp=self.hp-hplost
        
    def is_alive(self):
        if (self.hp>0):
            return True
        else:
            return False
    def get_speed(self):
        return self.speed
        