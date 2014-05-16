from button import Button
from player import Player
from graphics import *

#class Gboard , to draw the chessboard
class Gboard:
    def __init__(self):
        self.win=GraphWin("Five-in-a-row",600,700)
        self.b1=Button(self.win,Point(200,650),80,40,'Start')
        self.b2=Button(self.win,Point(400,650),80,40,'Restart')
        self.point_all=[]
        self.circle_all=[]
        x=0
        y=0
        #draw the chess board
        for i in range(31):
            Line(Point(x,600),Point(x,0)).draw(self.win)
            Line(Point(0,y),Point(600,y)).draw(self.win)
            x=x+20
            y=y+20

    #reset the game
    def reset(self):
        for ele in self.circle_all:
            ele.undraw()
        self.circle_all=[]        
        self.point_all=[]
        self.b1.activate()
        self.b2.deactivate()
        

    #the process of the game   
    def run(self):
        li1=[]
        li2=[]
        ptemp=Point(0,0)
        cl1='black'
        cl2='white'
        p1=Player(cl1,li1,ptemp)
        p2=Player(cl2,li2,ptemp)
        self.b1.activate()
        p=Point(0,0)
        p=self.win.getMouse()
        while self.b1.clicked(p)==0:
            p=self.win.getMouse()
        self.b1.deactivate()    
        self.b2.activate()
        judge_1=1
        judge_2=1
        
        while judge_1==1 and judge_2==1:
            p1.action(self.win,self.point_all,self.circle_all)
            if p1.judge(self.win,p1.location)==1:
                    judge_1=0
            else:
                p2.action(self.win,self.point_all,self.circle_all)
                if p2.judge(self.win,p2.location)==1:
                    judge_2=0

        
        p=self.win.getMouse()
        if self.b2.clicked(p)==0:
            p=self.win.getMouse()
   
        self.reset()
        self.run()
        if self.win.getMouse():
            self.win.close()

        
            
        
        
            
        
        
        
        
        
        
