from random import randint

class Enemy(object):
    


    def __init__(self, name, hp, speed,spot,index):
        self.name=name
        self.orig_hp=hp
        self.hp=hp
        self.speed=speed
        self.spot=spot
        self.anim_frame=0
        self.anim_y=0
        self.timetonext=5/speed
        self.lastmove=0
        self.index=index
        self.shott=0
        self.shot_time=0
        self.hplost=False
        self.prev_time=0
        self.steps_taken=0
        self.price=(self.orig_hp+5*self.speed)/10
        
    
        return
    def move(self,prev):
        mynext=self.spot.get_next()
        self.spot=mynext
        self.framezero()
        self.prev_time=prev
        self.steps_taken+=1
        #print(self.name+" moved")
    
    def shot(self,hplost,time):
        if self.shott==0:
            self.shot_time=time
        self.shott+=hplost
        
        
        
    def is_alive(self):
        if (self.hp>0):
            return True
        else:
            return False
    def get_speed(self):
        return self.speed
    def gotshot(self,time,totarget):
        if(-(self.shot_time-time/1000)>=totarget and self.shot_time>0 and self.shott>0):
            self.hp-=self.shott
            self.hplost=True
            self.shott=0
            self.shot_time=0
            return True
        return False
    def get_frame(self):
        return self.anim_frame
    def get_framey(self):
        if(self.hp>0):
            self.add_y(randint(0,1)-0.5)
        return self.anim_y
    def add_y(self,x):
        if (self.anim_y+x>10 or self.anim_y+x<-10):
            x=-x
        self.anim_y+=x
        
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
    