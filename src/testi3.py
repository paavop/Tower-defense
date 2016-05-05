import pygame
from game import Game
from spot import Spot
from road import Road
from tower import Tower
from enemy import Enemy
from random import randint
import sys


teksti1=""
teksti2=""
teksti3="" 
color=(200,191,231)
start=None
enemies={}
towers={}
enemycount=0
towercount=0
time=0
score=0
money=100
prev_time=0
peli=Game()
pygame.init()
done=False
lost=False
buttonx=120
buttony=37
firstx=350
firsty=600
space=(100-2*buttony-8)/3
build=False
build1=False
build2=False
build3=False
build4=False

names={}
ranges={}
speeds={}
powers={}
prices={}
tornit={}
enemytypes={}
enemypic={}
wavedata={}
wave=1
lastwave1=0
spawnfreq={}
lastspawn={}
def spawn():
    global lastspawn,wave,lastwave1
    if(pygame.time.get_ticks()/1000>wave*60):
        wave+=1
    if(wave in wavedata ):
        
        for key in wavedata[wave]:
            lastwave1=wave
            nexti=(float(lastspawn[key])+float(spawnfreq[key]))
            if (pygame.time.get_ticks()/1000>nexti and pygame.time.get_ticks()/1000<wave*60-10):
                lastspawn[key]=pygame.time.get_ticks()/1000
                spawn_enemy(key)
                
    else:
        for key in wavedata[lastwave1]:
            nexti=(float(lastspawn[key])+float(spawnfreq[key]/(wave-lastwave1)))
            if (pygame.time.get_ticks()/1000>nexti and pygame.time.get_ticks()/1000<wave*60-10):
                lastspawn[key]=pygame.time.get_ticks()/1000
                spawn_enemy(key)
            
def det_spawn_freq():
    global lastspawn
    if(wave in wavedata):
        for key in wavedata[wave]:
            if (not int(wavedata[wave][key])>0):
                spawnfreq[key]=1000
            else:
                spawnfreq[key]=49/int(wavedata[wave][key])
            lastspawn[key]=0
    print(spawnfreq)
def init_waves(file):
    try:
        global wavedata
        file=open(file)
        ind=None
        
        for line in file:
            

            text=line.split()
            if (len(text)>0):
                if(text[0]=='wave'):
                    ind=int(text[1])
                    wavedata[ind]={}
                    
            if(ind!=None and len(text)>0):
                if(isInteger(text[0])):
                   
                    wavedata[ind][int(text[0])]=text[1]
                
        for j in range(4):
            i=j+1
            if (not (i in wavedata[1])):
                raise ValueError('asd')
            
        file.close()
    except (ValueError,IndexError):
        print("wave data is not readable, loading defaults")
        init_enemies("wavedata_default.txt")

def init_enemies(file):
    try:
        global enemytypes,enemypic
        file=open(file)
        ind=None
        
        
        for line in file:
            text=line.split()
            if (len(text)>0):
                if(isInteger(text[0])):
                    ind=int(text[0])
                    enemytypes[ind]={}
                    
            if(ind!=None and len(text)>0):
                if(text[0]=="Name:"):
                    enemytypes[ind][0]=text[1]
                if(text[0]=="Hp:" and isInteger(text[1])):
                    enemytypes[ind][1]=int(text[1])
                if(text[0]=="Speed:" and isInteger(text[1])):
                    enemytypes[ind][2]=int(text[1])
                if(text[0]=="Image:" ):
                    enemypic[ind]=pygame.image.load(str(text[1]))
                
        for j in range(4):
            i=j+1
            if (not (i in enemytypes)):
                raise ValueError('asd')
            for k in range(3):
                
                if (not (k in enemytypes[i])):
                    raise ValueError('asd')
        file.close()
    except (ValueError,IndexError):
        print("Enemy data is not readable, loading defaults")
        init_enemies("enemydata_default.txt")
def init_towers(file):
    try:
        global names, ranges, speeds, powers, prices, tornit
        file=open(file)
        ind=None
        for line in file:
            text=line.split()
            
            if (len(text)>0):
                if(isInteger(text[0])):
                    ind=int(text[0])
            if(ind!=None and len(text)>0):
                if(text[0]=="Name:"):
                    names[ind]=text[1]
                if(text[0]=="Range:" and isInteger(text[1])):
                    ranges[ind]=int(text[1])
                if(text[0]=="Speed:" and isInteger(text[1])):
                    speeds[ind]=int(text[1])
                if(text[0]=="Power:" and isInteger(text[1])):
                    powers[ind]=int(text[1])
                if(text[0]=="Price:" and isInteger(text[1])):
                    prices[ind]=int(text[1])
                if(text[0]=="Image:"):
                    tornit[ind]=pygame.image.load(text[1])
        for j in range(4):
            i=j+1
            if (not (i in names) or not (i in ranges) or not (i in speeds) or not (i in powers) or not (i in prices) or not (i in tornit) ):
                raise ValueError('asd')
        file.close()
    except (ValueError,IndexError):
        print("Tower data is not readable, loading defaults")
        init_towers("towerdata_default.txt")
    
def isInteger(s):
    try:
        int(s)
        return True
    except ValueError:
        return False
        
def update_screen():
  
    for i in range(12):
        for j in range(20):
            if isinstance(peli.board.get_spot(i, j),Road):
                if(peli.board.get_spot(i, j).start):
                    screen.blit(tie_start,(50*j,50*i))
                    continue
                if(peli.board.get_spot(i, j).goal):
                    screen.blit(tie_goal,(50*j,50*i))
                    continue
            
                screen.blit(tie,(50*j,50*i))
                continue
            if isinstance(peli.board.get_spot(i, j),Spot):
                screen.blit(maa,(50*j,50*i))
    for i in range(enemycount):
        if enemies[enemycount-1-i]!=None:
            if(draw_enemy(enemies[enemycount-1-i])):
                pygame.time.wait(500)
                new_text("You lose")
                draw_lose_screen()
                font=pygame.font.Font(None, 200)
                text=font.render(teksti1,1,(10,10,10))
                screen.blit(text,((1000-text.get_width())/2,100))
                pygame.display.flip()
                
                scoreboard()
                pygame.quit()
                sys.exit(0)
    for i in range(12):
        for j in range(20):
            if isinstance(peli.board.get_spot(i, j),Tower):
                draw_tower(peli.board.get_spot(i,j),50*j,50*i)
                continue
       
    draw_build()
    draw_menu()   
      
    
    pygame.display.flip()
def scoreboard():
    global score
    score=int(score)
    myname=""
    font = pygame.font.Font(None, 50)
    font2=pygame.font.Font("Mono.ttf", 30)
    teksti="Enter your name:"
    kirjoitus=True
    last_time=0
    while kirjoitus:
        if(pygame.time.get_ticks()/1000>last_time+0.1):
            pygame.draw.rect(screen,(200,191,200),(300,350,400,100),0)
            pygame.draw.rect(screen,(1,0,0),(300,350,400,100),5)
            text1=font.render(teksti,1,(10,10,10))
            text2=font2.render(myname,1,(10,10,10))
            screen.blit(text1,((1000-text1.get_width())/2,360))
            screen.blit(text2,((1000-text2.get_width())/2,410))
            pygame.display.flip()
            last_time=pygame.time.get_ticks()/1000
        for evt in pygame.event.get():
            if evt.type == pygame.KEYDOWN:
                if evt.unicode.isalpha():
                    if(len(myname)<12):
                        myname += evt.unicode
                elif evt.key == pygame.K_BACKSPACE:
                    myname = myname[:-1]

                elif evt.key == pygame.K_RETURN:
                    kirjoitus=False
                
            elif evt.type == pygame.QUIT:
                return
          
    file=open('scoreboard.txt')
    temp1=str(score)+" "+myname+"\n"
    
    line=file.readline()
    lines={}
    for i in range(10):
        a=(int(str(temp1.split()[0])))
        b=(int(str(line.split()[0])))
        if(a>b):
            lines[i]=temp1
            temp1=line
        else:
            lines[i]=line
        line=file.readline() 
    file.close()
    file=open('scoreboard.txt','r+')
    for i in range(10):
        file.write(lines[i])
    file.close()
    teksti="Hall of Fame"
    font2=pygame.font.Font("Mono.ttf", 20)

    while True:
        if(pygame.time.get_ticks()/1000>last_time+0.1):
            pygame.draw.rect(screen,(200,191,200),(300,250,400,300),0)
            pygame.draw.rect(screen,(1,0,0),(300,250,400,300),5)
            text1=font.render(teksti,1,(10,10,10))
            
            screen.blit(text1,((1000-text1.get_width())/2,260))
            for i in range(10):
                text1=font2.render(lines[i],1,(10,10,10))
                screen.blit(text1,((1000-text1.get_width())/2,320+i*20))
            pygame.display.flip()
            last_time=pygame.time.get_ticks()/1000
        
        for evt in pygame.event.get():
            if evt.type == pygame.KEYDOWN:
                return
                
            elif evt.type == pygame.QUIT:
                return
    return

def draw_lose_screen():
    s=pygame.Surface((1000,600))
    s.set_alpha(128)
    s.fill((176,0,0))
    screen.blit(s,(0,0))

def draw_tower(tower,x,y):
    ya=tower.shot_y(pygame.time.get_ticks())
    xa=tower.shot_x(pygame.time.get_ticks())
    if(ya!=0 or xa!=0):
        pygame.draw.circle(screen,(1,0,0),(x+25+ya,y+25+xa),5,0)
    screen.blit(rotatecenter(tower.pic,tower.angletoenemy(pygame.time.get_ticks())),(x,y))
    
    
    if (tower.target!= None and tower.target.gotshot(pygame.time.get_ticks(),tower.timetotarget)):
            frame=tower.target.get_frame()
            framey=tower.target.get_framey()
            xd=0
            yd=0
            if (tower.target.spot.x>tower.target.spot.next.x):
                xd=-frame
                yd=framey
            if (tower.target.spot.x<tower.target.spot.next.x):
                xd=frame
                yd=-framey
            if (tower.target.spot.y>tower.target.spot.next.y):
                xd=-framey
                yd=-frame
            if (tower.target.spot.y<tower.target.spot.next.y):
                yd=frame
                xd=framey
                
            xd=framey
            screen.blit(boom_s, (12+yd+tower.target.spot.y*50,12+xd+tower.target.spot.x*50))
    

def rotatecenter(image,angle):    
    orig_rect = image.get_rect()
    rot_image = pygame.transform.rotate(image, angle)
    rot_rect = orig_rect.copy()
    rot_rect.center = rot_image.get_rect().center
    rot_image = rot_image.subsurface(rot_rect).copy()
    return rot_image

def draw_enemy(enemy):
    kuva=enemypic[enemy.pic_index]
    ya=0
    xa=0
    frame=enemy.get_frame()
    framey=enemy.get_framey()
    if not (enemy.spot.goal):
        if (enemy.spot.x>enemy.spot.next.x):
            kuva=enemypic[enemy.pic_index]
            xa=-frame
            ya=framey
        if (enemy.spot.x<enemy.spot.next.x):
            kuva=rotatecenter(enemypic[enemy.pic_index],180)
            xa=frame
            ya=-framey
        if (enemy.spot.y>enemy.spot.next.y):
            kuva=rotatecenter(enemypic[enemy.pic_index],90)
            ya=-frame
            xa=-framey
        if (enemy.spot.y<enemy.spot.next.y):
            kuva=rotatecenter(enemypic[enemy.pic_index],270)
            ya=frame
            xa=framey
        screen.blit(kuva,(ya+enemy.spot.y*50,xa+enemy.spot.x*50))
        
        draw_enemy_hp(enemy,ya,xa)
        #print(str(int(ya+enemy.spot.y*50))+"   "+str(int(xa+enemy.spot.x*50)))         
        enemy.add_frame(25*((pygame.time.get_ticks()/1000)-enemy.get_lastmove())/enemy.get_timetonext(),pygame.time.get_ticks()/1000)
        
    else:
        for i in range(12):
            for j in range(20):
                if isinstance(peli.board.get_spot(i, j),Tower):
                    screen.blit(boom,(50*j,50*i))
        for i in range(enemycount):
            if (enemies[enemycount-1-i]!=None and enemies[enemycount-1-i]!=enemy):
                draw_enemy(enemies[enemycount-1-i])
        screen.blit(kuva,(enemy.spot.y*50,enemy.spot.x*50))
        pygame.display.flip()
        lost=True
        return True
    
def draw_enemy_hp(enemy,ya,xa):
    percentage=enemy.get_relative_hp()
    green=40*percentage
    red=40-green

    if(green>0):
        pygame.draw.rect(screen,(0,200,0),(ya+enemy.spot.y*50+5,xa+enemy.spot.x*50+5,green,5),0)
    if(red>0 and red<=40):
        pygame.draw.rect(screen,(200,0,0),(ya+enemy.spot.y*50+5+green,xa+enemy.spot.x*50+5,red,5),0)
    pygame.draw.rect(screen,(1,0,0),(ya+enemy.spot.y*50+5,xa+enemy.spot.x*50+5,40,5),1)

    
def new_text(teksti):
    if (teksti!=None):
        global teksti1
        global teksti2
        global teksti3
        teksti3=teksti2
        teksti2=teksti1
        teksti1=teksti


               
def print_text():
    
    pygame.draw.rect(screen,(200,191,200),(10,610,200,80),0)
    pygame.draw.rect(screen,(1,0,0),(10,610,200,80),1)
    font=pygame.font.Font("Mono.ttf", 10)
    text=font.render(teksti1,1,(10,10,10))
    text2=font.render(teksti2,1,(10,10,10))
    text3=font.render(teksti3,1,(10,10,10))
    screen.blit(text,(20,675))
    screen.blit(text2,(20,650))
    screen.blit(text3,(20,625))
    
def draw_a_button(x,y,sizex,sizey,normal1,normal2,chosen1,chosen2,pic,name,boole):
    pressed=False
    a=(pygame.mouse.get_pos())
    text=pygame.font.Font("mono.ttf",10).render(name,1,(10,10,10))
    if(boole or (a[0]>x and a[0]<x+sizex and a[1]>y and a[1]<y+sizey and  pygame.mouse.get_pressed()==(1,0,0))):
        pygame.draw.rect(screen,chosen1,(x,y,sizex,sizey),0)
        pygame.draw.rect(screen,chosen2,(x,y,sizex,sizey),1)
        pressed=True
    else:
        pygame.draw.rect(screen,normal1,(x,y,sizex,sizey),0)
        pygame.draw.rect(screen,normal2,(x,y,sizex,sizey),1)
    if (pic!=None):
        screen.blit(pygame.transform.scale(pic,(30,30)),(x,y+5))
        screen.blit(text,((x+40+(sizex-40)/2) - text.get_width()/2, (y+sizey/4) - text.get_height()/4))
    else:
        screen.blit(text,((x+(sizex)/2) - text.get_width()/2, (y+sizey/2) - text.get_height()/2))
    return pressed

        
      
def draw_build():
    if build:
        global build1,build2,build3,build4
        a=pygame.mouse.get_pos()
        i=int(a[0]/50)
        j=int(a[1]/50)
        #print(str(a[0])+" "+str(a[1]))
        if (build1 and a[1]<600):
            if(isinstance(peli.board.get_spot(j, i),Road) or isinstance(peli.board.get_spot(j, i),Tower)):
                screen.blit(denied,(i*50,j*50))
            else:
                screen.blit(tornit[1],(i*50,j*50))
                myrange=2
                circle=pygame.Surface((50*myrange*2,50*myrange*2))
                circle.fill((1,0,0))
                circle.set_colorkey((1,0,0))
                pygame.draw.circle(circle,(192,192,192),(50*myrange,50*myrange),50*myrange,0)
                circle.set_alpha(25)
                screen.blit(circle,((i+0.5)*50-myrange*50,(j+0.5)*50-myrange*50))
                if(pygame.mouse.get_pressed()==(1,0,0)):
                    add_tower(a, prices[1], powers[1], ranges[1], speeds[1],tornit[1],names[1])
                    #build1=False
        if (build2 and a[1]<600):
            if(isinstance(peli.board.get_spot(j, i),Road) or isinstance(peli.board.get_spot(j, i),Tower)):
                screen.blit(denied,(i*50,j*50))
            else:
                screen.blit(tornit[2],(i*50,j*50))
                myrange=3
                circle=pygame.Surface((50*myrange*2,50*myrange*2))
                circle.fill((1,0,0))
                circle.set_colorkey((1,0,0))
                pygame.draw.circle(circle,(192,192,192),(50*myrange,50*myrange),50*myrange,0)
                circle.set_alpha(25)
                screen.blit(circle,((i+0.5)*50-myrange*50,(j+0.5)*50-myrange*50))
                if(pygame.mouse.get_pressed()==(1,0,0)):
                    add_tower(a, prices[2], powers[2], ranges[2], speeds[2],tornit[2],names[2])
                    #build2=False
        if (build3 and a[1]<600):
            if(isinstance(peli.board.get_spot(j, i),Road) or isinstance(peli.board.get_spot(j, i),Tower)):
                screen.blit(denied,(i*50,j*50))
            else:
                screen.blit(tornit[3],(i*50,j*50))
                myrange=5
                circle=pygame.Surface((50*myrange*2,50*myrange*2))
                circle.fill((1,0,0))
                circle.set_colorkey((1,0,0))
                pygame.draw.circle(circle,(192,192,192),(50*myrange,50*myrange),50*myrange,0)
                circle.set_alpha(25)
                screen.blit(circle,((i+0.5)*50-myrange*50,(j+0.5)*50-myrange*50))
                if(pygame.mouse.get_pressed()==(1,0,0)):
                    add_tower(a, prices[3], powers[3], ranges[3], speeds[3],tornit[3],names[3])
                    #build3=False
        if (build4 and a[1]<600):
            if(isinstance(peli.board.get_spot(j, i),Road) or isinstance(peli.board.get_spot(j, i),Tower)):
                screen.blit(denied,(i*50,j*50))
            else:
                screen.blit(tornit[4],(i*50,j*50))
                myrange=7
                circle=pygame.Surface((50*myrange*2,50*myrange*2))
                circle.fill((1,0,0))
                circle.set_colorkey((1,0,0))
                pygame.draw.circle(circle,(192,192,192),(50*myrange,50*myrange),50*myrange,0)
                circle.set_alpha(25)
                screen.blit(circle,((i+0.5)*50-myrange*50,(j+0.5)*50-myrange*50))
                if(pygame.mouse.get_pressed()==(1,0,0)):
                    add_tower(a, prices[4], powers[4], ranges[4], speeds[4],tornit[4],names[4])
                    #build4=False
 
def print_buttons():
    global build1,build2,build3,build4,build
    teksti=("Build")
    font=pygame.font.Font("mono.ttf",16)
    text=font.render(teksti,1,(10,10,10))
    screen.blit(text,(firstx-70,firsty+space+6,buttonx,buttony))
    normal1=(200,191,200)
    normal2=(1,0,0)
    chosen1=(200,100,100)
    chosen2=(200,0,0)
    if(draw_a_button(firstx-70,firsty+space+4,50,buttony,normal1,normal2,chosen1,chosen2,None,"Build",build)):
        build=True
    if(draw_a_button(firstx-70,firsty+space+4+buttony+space,50,buttony,normal1,normal2,chosen1,chosen2,None,"Cancel",False)):
        build=False
        build1=False
        build2=False
        build3=False
        build4=False
    if build:
        if(draw_a_button(firstx,firsty+space+4,buttonx,buttony,normal1,normal2,chosen1,chosen2,tornit[1],names[1],build1)):
            build1=True
            build2=False
            build3=False
            build4=False
        if(draw_a_button(firstx,firsty+space+4+buttony+space,buttonx,buttony,normal1,normal2,chosen1,chosen2,tornit[2],names[2],build2)):
            build1=False
            build2=True
            build3=False
            build4=False
        if(draw_a_button(firstx+buttonx+space,firsty+space+4,buttonx,buttony,normal1,normal2,chosen1,chosen2,tornit[3],names[3],build3)):
            build1=False
            build2=False
            build3=True
            build4=False
        if(draw_a_button(firstx+buttonx+space,firsty+space+4+buttony+space,buttonx,buttony,normal1,normal2,chosen1,chosen2,tornit[4],names[4],build4)):
            build1=False
            build2=False
            build3=False
            build4=True

def draw_menu():
    pygame.draw.rect(screen,color,(0,600,1000,100),0)
    pygame.draw.lines(screen, (1,0,0), False,[(0,600),(998,600),(998,698),(0,698),(0,600)],4)
    print_text()
    print_stats()
    print_buttons()
    draw_info()


def draw_info():
    if build and (build1 or build2 or build3 or build4):
        if build1:
            kuva=tornit[1]
            name=names[1]
            i=1
        if build2:
            kuva=tornit[2]
            name=names[2]
            i=2
        if build3:
            kuva=tornit[3]
            name=names[3]
            i=3
        if build4:
            kuva=tornit[4]  
            name=names[4] 
            i=4
        pygame.draw.rect(screen,(200,191,200),(firstx+2*buttonx+2*space,firsty+space+4,2*buttonx-space,2*buttony+space),0)
        pygame.draw.rect(screen,(1,0,0),(firstx+2*buttonx+2*space,firsty+space+4,2*buttonx-space,2*buttony+space),1)
        screen.blit(kuva,(firstx+2*buttonx+2*space+5,firsty+space+4+(2*buttony+space-50)/2))
        text=pygame.font.Font("mono.ttf",18).render(name,1,(10,10,10))
        screen.blit(text,((firstx+2*buttonx+2*space+50+(2*buttonx-space+5-50)/2) - text.get_width()/2, (firsty+space+8) ))
        power=pygame.font.Font("mono.ttf",10).render("Power: "+str(powers[i]),1,(10,10,10))
        speed=pygame.font.Font("mono.ttf",10).render("Speed: "+str(speeds[i]),1,(10,10,10))
        myrange=pygame.font.Font("mono.ttf",10).render("Range: "+str(ranges[i]),1,(10,10,10))
        price=pygame.font.Font("mono.ttf",10).render("Price: "+str(prices[i]),1,(10,10,10))
        screen.blit(power,((firstx+2*buttonx+2*space+50+(2*buttonx-space+5-50)/4) - power.get_width()/2, (firsty+space+8+2*text.get_height()) ))
        screen.blit(speed,((firstx+2*buttonx+2*space+50+(2*buttonx-space+5-50)/4) - speed.get_width()/2, (firsty+space+8+3*text.get_height()) ))
        screen.blit(myrange,((firstx+2*buttonx+2*space+50+(2*buttonx-space+5-50)*3/4) - myrange.get_width()/2, (firsty+space+8+2*text.get_height()) ))
        screen.blit(price,((firstx+2*buttonx+2*space+50+(2*buttonx-space+5-50)*3/4) - price.get_width()/2, (firsty+space+8+3*text.get_height()) ))

        
        
        
def make_road():
    global start
    file=open('map.txt')
    first=True
    lastx=None
    lasty=None
    for line in file:
        x=int(line.split()[0])
        y=int(line.split()[1])
        
        if first:
            first=False
            peli.board.add_road(x,y)
            start=peli.board.get_spot(x,y)
        if (lastx!=None and lasty!=None):
            if(lastx>x):
                for i in range(lastx-x):
                    peli.board.add_road(lastx-1-i,y)
            if(lasty>y): 
                for i in range(lasty-y):
                    peli.board.add_road(x,lasty-1-i)
            if(lastx<x):
                for i in range(x-lastx):
                    peli.board.add_road(lastx+1+i,y)
            if(lasty<y): 
                for i in range(y-lasty):
                    peli.board.add_road(x,lasty+1+i)
        lastx=x
        lasty=y
    file.close()
    
    
    
    
def spawn_enemy(enemy_index):
    global enemycount,enemytypes
    
    enemies[enemycount]=Enemy(enemytypes[enemy_index][0]+(" ")+str(enemycount),enemytypes[enemy_index][1],enemytypes[enemy_index][2],start,enemycount,enemy_index,pygame.time.get_ticks()/1000)
    
    enemycount=enemycount+1
    
def add_tower(a,price,power,myrange,speed,pic,name):
    global towercount
    global money
    if not (isinstance(peli.board.get_spot(int(a[1]/50),int(a[0]/50)),Road)):
        if not (isinstance(peli.board.get_spot(int(a[1]/50),int(a[0]/50)),Tower)):
            if(money<price):
                new_text("Not enough money")
            else:
                new_text(peli.board.add_tower(int(a[1]/50), int(a[0]/50),price,power,myrange,towercount,speed,money,pic,name))
                towers[towercount]=peli.board.get_spot(int(a[1]/50), int(a[0]/50))
                money-=price
                towercount+=1
        else:
            new_text("Can't build on another tower")
    else:
        new_text("Can't build on road")

    
    
def remove_tower(a):
    global towercount
    global money
    if  (isinstance(peli.board.get_spot(int(a[1]/50), int(a[0]/50)),Tower)):
        del towers[peli.board.get_spot(int(a[1]/50),int(a[0]/50)).get_index()]
        money+=int(0.5*(peli.board.get_spot(int(a[1]/50), int(a[0]/50)).price))
    new_text(peli.board.remove_tower(int(a[1]/50), int(a[0]/50)))
    
    
    
          
def print_stats():
    #pygame.draw.rect(screen,color,(850,610,125,80),0)
    teksti2="Time : "+str(int(time))
    teksti="Money: "+str(int(money))
    teksti3="Score: "+str(int(score))
    teksti4="Wave : "+str(int(wave))
    font=pygame.font.Font("mono.ttf",12)
    text=font.render(teksti,1,(10,10,10))
    text2=font.render(teksti2,1,(10,10,10))
    text3=font.render(teksti3,1,(10,10,10))
    text4=font.render(teksti4,1,(10,10,10))
    screen.blit(text,(850,610))
    screen.blit(text2,(850,625))
    screen.blit(text3,(850,640))
    screen.blit(text4,(850,655))
    
def shoot_towers():
    for i in towers:
        if ((pygame.time.get_ticks()/1000)-towers[i].lastshot>(2/towers[i].speed)):
            towers[i].shoot(enemies,pygame.time.get_ticks()/1000)
            
def move_enemies(enemies):
    global money,score
    for i in enemies:
        if (enemies[i]!=None):
            if(enemies[i].is_alive()):
                
                if(time>enemies[i].prev_time+enemies[i].get_timetonext()):
                    

                    enemies[i].move(time)
                    #enemies[i].shot(10)
                    
                    enemies[i].prev_time+=enemies[i].get_timetonext()
            else:
                money+=enemies[i].price
                score+=enemies[i].price/10
                enemies[i]=None
make_road()
init_towers('towerdata.txt')
init_enemies('enemydata.txt')
init_waves('wavedata.txt')


clock=pygame.time.Clock()
    
logo = pygame.image.load("logo32x32.png")

boom=pygame.image.load("boom.png")
boom_s=pygame.image.load("boom_small.png")
tie=pygame.image.load("road.png")
tie_start=pygame.image.load("road_start.png")
tie_goal=pygame.image.load("road_goal.png")
maa=pygame.image.load("empty.png")



denied=pygame.image.load("denied.png")


pygame.display.set_icon(logo)
pygame.display.set_caption("Tower defense")

size=1000
    
    # create a surface on screen that has the size of 240 x 180
screen_width=size
screen_height=size-300
screen = pygame.display.set_mode((screen_width,screen_height))



screen.fill(color)
    



#spawn_enemy("vihu", 100, 10,start)


    
pygame.display.flip()
lastwave=0
running=True
running2=True
while running2:
    time=pygame.time.get_ticks()/1000
    a=(pygame.mouse.get_pos())
    #if pygame.mouse.get_pressed()==(1,0,0):
        #if(a[1]<=600):
            #add_tower(a, 100, 10, 5, 10)
            #new_text(peli.board.add_tower(int(a[1]/50), int(a[0]/50),100,5,5))
    if pygame.mouse.get_pressed()==(0,0,1):
        if(a[1]<=600):
            remove_tower(a)
            #spawn_enemy(randint(1,4))
    
    for event in pygame.event.get():
            # only do something if the event is of type QUIT
            if event.type == pygame.QUIT:
                # change the value to False, to exit the main loop
                running2 = False
                
    if running:      
        update_screen()
    
    if(wave>lastwave):
        lastwave+=1
        det_spawn_freq() 
    spawn()   
    shoot_towers()
    move_enemies(enemies)
    
    
    
    
