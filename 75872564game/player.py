# player.py
from graphics import *
from time import sleep

#class  Player , to initial two players 

class Player:
    def __init__(self,colour,li,p):
        self.color=colour #store the color of the player(Black or White)
        self.point=li# used to store all the location of the chess of the same color
        self.location=p#to store the location (x,y) which has been put on the chessboard
    def judge(self,win,p):#to judge whether the player wins the game
        count1=0
        count2=0
        count3=0
        count4=0
        count5=0
        count6=0
        count7=0
        count8=0
        judge1=0
        judge2=0
        judge3=0
        judge4=0
        judge5=0
        judge6=0
        judge7=0
        judge8=0
        
        tempx=p.getX()
        tempy=p.getY()

        while judge1==0:
            judge1=count1
            p_=Point(tempx,tempy)
            for i in self.point:
                if i.getX()==p_.getX() and i.getY()==p_.getY():
                    count1=count1+1
                    tempx=tempx-20
            if judge1==count1:
                judge1=1
            else:
                judge1=0
        tempx=p.getX()
        tempy=p.getY()
        while judge2==0:
            judge2=count2
            p_=Point(tempx,tempy)
            for i in self.point:
                if i.getX()==p_.getX() and i.getY()==p_.getY():
                    count2=count2+1
                    tempx=tempx+20
            if judge2==count2:
                judge2=1
            else:
                judge2=0
        tempx=p.getX()
        tempy=p.getY()
        while judge3==0:
            judge3=count3
            p_=Point(tempx,tempy)
            for i in self.point:
                if i.getX()==p_.getX() and i.getY()==p_.getY():
                    count3=count3+1
                    tempy=tempy-20
            if judge3==count3:
                judge3=1
            else:
                judge3=0
        tempx=p.getX()
        tempy=p.getY()
        while judge4==0:
            judge4=count4
            p_=Point(tempx,tempy)
            for i in self.point:
                if i.getX()==p_.getX() and i.getY()==p_.getY():
                    count4=count4+1
                    tempy=tempy+20
            if judge4==count4:
                judge4=1
            else:
                judge4=0
        tempx=p.getX()
        tempy=p.getY()
        while judge5==0:
            judge5=count5
            p_=Point(tempx,tempy)
            for i in self.point:
                if i.getX()==p_.getX() and i.getY()==p_.getY():
                    count5=count5+1
                    tempx=tempx-20
                    tempy=tempy-20
            if judge5==count5:
                judge5=1
            else:
                judge5=0
        tempx=p.getX()
        tempy=p.getY()
        while judge6==0:
            judge6=count6
            p_=Point(tempx,tempy)
            for i in self.point:
                if i.getX()==p_.getX() and i.getY()==p_.getY():
                    count6=count6+1
                    tempx=tempx+20
                    tempy=tempy+20
            if judge6==count6:
                judge6=1
            else:
                judge6=0
        tempx=p.getX()
        tempy=p.getY()
        while judge7==0:
            judge7=count7
            p_=Point(tempx,tempy)
            for i in self.point:
                if i.getX()==p_.getX() and i.getY()==p_.getY():
                    count7=count7+1
                    tempx=tempx-20
                    tempy=tempy+20
            if judge7==count7:
                judge7=1
            else:
                judge7=0
        tempx=p.getX()
        tempy=p.getY()
        while judge8==0:
            judge8=count8
            p_=Point(tempx,tempy)
            for i in self.point:
                if i.getX()==p_.getX() and i.getY()==p_.getY():
                    count8=count8+1
                    tempx=tempx+20
                    tempy=tempy-20
            if judge8==count8:
                judge8=1
            else:
                judge8=0

        if (count1+count2)>=6 or (count3+count4)>=6 or (count5+count6)>=6 or (count7+count8)>=6:
        #note that the location will be judge twice so if one wins the total count must be >= 6
            if self.color=='black':
                t=Text(Point(300,100),'Black wins the game click reset to restart the game')
            elif self.color=='white':
                t=Text(Point(300,100),'White wins the game click reset to restart the game')
            t.draw(win)
            if win.getMouse():
                t.undraw()
            return 1
        else:
            return 0
            
        
            
            
        
    def action(self,win,point_all,circle_all):
        p=win.getMouse()
        judge=1
        if p.getX()<600 and p.getY()<600:
            x=p.getX()
            y=p.getY()
        #to get the accurate location of the chess       
            if (x-int((x/20))*20)<((int(x/20)+1)*20-x):
                x=int((x/20))*20
            else:
                x=(int(x/20)+1)*20
            if (y-int((y/20))*20)<((int(y/20)+1)*20-y):
                y=int((y/20))*20
            else:
                y=(int(y/20)+1)*20
            Center=Point(x,y)
            judge=0
            for i in point_all:
                if i.getX()==Center.getX() and i.getY()==Center.getY():
                    judge=1
        if judge==0:
        #to draw the chess
            cir=Circle(Center,10)
            circle_all.append(cir)
            cir.draw(win)
            cir.setFill(self.color)
            self.point.append(Center)
            point_all.append(Center)
            self.location=Center
        else:
        #click the wrong place ,reclick        
            txt=Text(Point(300,100),'Out of the board! Click to continue!')
            txt.draw(win)
            if win.getMouse():
                txt.undraw()
            self.action(win,point_all,circle_all)
            
