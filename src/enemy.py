

class Enemy(object):
    


    def __init__(self, name, hp, speed,spot,index):
        self.name=name
        self.orig_hp=hp
        self.hp=hp
        self.speed=speed
        self.spot=spot
        self.anim_frame=0
        self.timetonext=5/speed
        self.lastmove=0
        self.index=index
        
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
    
    def get_frame(self):
        return self.anim_frame
    
    def add_frame(self,x,time):
        self.anim_frame=self.anim_frame+x
        self.lastmove=time
    
    def framezero(self):
        self.anim_frame=0
        
    def get_timetonext(self):
        return self.timetonext
    
    def get_lastmove(self):
        return self.lastmove
    
    def get_relative_hp(self):
        return self.hp/self.orig_hp
    
    def get_index(self):
        return self.index
    