import pygame
from pygame.locals import *
import sys
import random
from threading import Thread
import time 
def disan():
    pygame.init()
    pygame.init()
    screen=pygame.display.set_mode((1600,666))
    bg=pygame.image.load('disan.png').convert_alpha()
    pygame.display.update()
    x=800
    y=300
    color=255,255,255
    width=15
    wh=10
    n=1
    xx=900
    yy=200
    xx1=20
    yy1=20
    xx2=1580
    yy2=20
    c1=255,0,0
    while 1:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                sys.exit()
        keys=pygame.key.get_pressed()
        if keys[K_a]:
            x-=2
        if keys[K_d]:
            x+=2
        if keys[K_w]:
            y-=2
        if keys[K_s]:
            y+=2
        elif keys[K_ESCAPE]:
            sys.exit() 
        if n==1:
            x1=random.randrange(10,1580)
            y1=random.randrange(10,646)
            n=0
        if x>1585 or x<15:
            x=800
        if y >651 or y<15:
            y=400
        if x1-width+2<x<x1+width-1 and y1-width+2<y<y1+width-1:
            width+=2
            n=1
        xx+=6
        if xx>1580 or xx<20:
            xx=20
        c2=0,0,255
        p2=xx,yy
        xx1+=6
        yy1+=4
        if xx1>1300 and yy1>646:
            xx1=20
            yy1=20
        p3=xx1,yy1
        wh1=25
        xx2-=6
        yy2+=4
        if width <15:
            sys.exit()
        if xx2<300 and yy2>646:
            xx2=1580
            yy2=20
        p5=xx2,yy2
        if xx-wh-width<=x<=xx+wh+width and yy-wh-width<=y<=yy+wh+width:
            if width >15:
                width-=15
            else:
                sys.exit()
        if xx1-wh-width<=x<=xx1+wh+width and yy1-wh-width<=y<=yy1+wh+width:
            if width >15:
                width-=15
            else:
                sys.exit()
        if xx2-wh+2<=x<=xx2+wh+width and yy2-wh-width<=y<=yy2+wh+width:
            if width >15:
                width-=15
            else:
                sys.exit()
        if width>50:
            color=125,125,125
            xx+=9
        if width >35:
            color=197,229,149
            xx1+=8
            yy1+=5
            xx2-=8
            yy2+=5
            if keys[K_LEFT]:
                x=100
            if keys[K_RIGHT]:
                x=100
            if keys[K_UP]:
                y=300
            if keys[K_DOWN]:
                y=600
        position=x,y
        screen.blit(bg,(0,0))
        p4=x1,y1
        pygame.draw.circle(screen,color,position,width)
        pygame.draw.circle(screen,c2,p2,wh1)
        pygame.draw.circle(screen,c2,p3,wh1)
        pygame.draw.circle(screen,c2,p5,wh1)
        pygame.draw.circle(screen,c1,p4,wh)
        pygame.display.update()

def jinru():
    pygame.init()
    screen=pygame.display.set_mode((1600,670))
    bg=pygame.image.load('kk.png').convert_alpha()
    pos_x=780
    pos_y=50
    nnn=1
    width=10
    width1=10
    xx=300
    yy=300
    cr=0,255,0
    xx1=300
    yy1=300
    while True:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                sys.exit()
        if width<10:
            diyi()
        keys=pygame.key.get_pressed()
        if keys[K_a]:
            pos_x-=2
        if keys[K_d]:
            pos_x+=2
        if keys[K_w]:
            pos_y-=2
        if keys[K_s]:
            pos_y+=2
        elif keys[K_ESCAPE]:
            sys.exit()   
        if pos_x>1600 :
            pos_x=1600
        if pos_x<0:
            pos_x=0 
        if pos_y>670:
            pos_y=670 
        if pos_y<0:
            pos_y=0               
        color=255,255,0
        color1=255,0,0
        screen.fill((0,0,200))
        position=pos_x,pos_y
        if nnn==1:
            x=random.randrange(0,1590)
            y=random.randrange(0,660)
            nnn=0
        position1=x,y
        if x-width+2<pos_x<x+width-1 and y-width+2<pos_y<y+width-1:
            nnn=1
            width+=2
        if width>=28:
            color=0,255,0
            s=pygame.image.load('qt2.png').convert_alpha()
            screen.blit(s,(pos_x,pos_y))
            if pos_x>1580 or pos_x<0:
                pos_x=670
            if pos_y>670 or pos_y<0:
                pos_y=400   
            if keys[K_o]:
                pos_x=780
        if width>=50:
            color=0,0,255
            s=pygame.image.load('by.png').convert_alpha()
            screen.blit(s,(pos_x,pos_y))
            if keys[K_o]:
                pos_x=780
            if keys[K_p]:
                nnn=1
        wh=20
        if 0<xx<1580:
            if width>50:
                xx+=8
            else:
                xx+=6
        if  xx>=1580:
            xx=1
        if 0<yy1<670 :
            if width>50:
                yy1-=8
            else:
                yy1-=6
        if  yy1<=0:
            yy1=669
        if width>65:
            disan()
        if xx-wh<=pos_x+width<=xx+wh and yy-wh<=pos_y<=yy+wh+width:
            if width >10:
                width-=10
            else:
                diyi()
        if xx1-wh+2<=pos_x<=xx1+wh+width and yy1-wh<=pos_y+width<=yy1+wh:
            if width >10:
                width-=10
            else:
                diyi()
        pp=xx,yy
        pp1=xx1,yy1
        screen.blit(bg,(0,0))
        pygame.draw.circle(screen,cr,pp,wh)
        pygame.draw.circle(screen,cr,pp1,wh)
        pygame.draw.circle(screen,color,position,width)
        pygame.draw.circle(screen,color1,position1,width1)
        pygame.display.update()
        
def diyi():
    pygame.init()
    screen=pygame.display.set_mode((600,500))    
    bg = pygame.image.load("./background.png").convert()  
    pos_x=300
    pos_y=250
    clock=pygame.time.Clock()
    color=255,255,0
    color1=160,100,0
    screen.fill((0,0,200))
    position=pos_x,pos_y
    position1=pos_x-220,pos_y-200
    width=10
    screen.blit(bg,(0,0))
    pygame.draw.circle(screen,color,position,width)
    pygame.display.update()
    while True:
        clock.tick(30)
        for event in pygame.event.get():
            if event.type==MOUSEBUTTONUP:
                while 1:
                    m_x,m_y=event.pos
                    if pos_x<m_x :
                        pos_x+=1
                    elif pos_x>m_x:
                        pos_x-=1
                    if pos_x==m_x :
                        if pos_y>m_y:
                            pos_y-=1
                        elif pos_y<m_y :
                            pos_y+=1
                    if 70<pos_x<90 and 40<pos_y<60:
                        jinru()
                    if pos_x==m_x and pos_y==m_y:
                        break
                    
                    screen.fill((0,0,200))
                    color=255,255,0
                    position=pos_x,pos_y
                    width=10
                    pygame.draw.circle(screen,color,position,width)
                    pygame.draw.circle(screen,color1,position1,width)
                    pygame.display.update()
            
            if event.type==pygame.QUIT:
                sys.exit()


            
