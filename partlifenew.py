print('s')
import turtle
import random
import math
import time
import sys
import partliferender
 
from numba import jit

#import partliferender

class modball(turtle.Turtle):
    def __init__(self,*args,**kwargs):
        super(modball,self).__init__(*args,**kwargs)
        self.penup()
        self.shape('circle')
        self.velocityxy = [0,0]
        self.shapesize(stretch_wid=0.3, stretch_len=0.3)
        self.cvalues = -1
        self.speed(0)

    def move(self):
        self.goto(self.xcor()+self.velocityxy[0],self.ycor()+self.velocityxy[1])

class chooser(turtle.Turtle):
    def __init__(self,adval,rulesli,*args,**kwargs):
        super(chooser,self).__init__(*args,**kwargs)
        self.penup()
        self.color('white')
        self.shape('square')
        self.controlwhat = []
        self.onclick(self.incrul)
        self.adval = adval #value to add ecah time press
        self.rulesli = rulesli

            
    def incrul(self,x,y):
        
        self.rulesli[self.controlwhat[0]][self.controlwhat[1]] += self.adval
        print(str(self.rulesli))
        




class runrender():

    def __init__(self):

        #BElow everything moving one of the generators
        self.dlbl = turtle.Turtle()
        self.dlbl.shape('square')
        self.dlbl.penup()
        self.dlbl.shapesize(stretch_len=67,stretch_wid=67)
        self.dlbl.ondrag(self.genballbase)
        #--------------------------------------

        self.window = turtle.Screen()
        self.window.bgcolor("black")
        self.window.setup(width=2000, height=1400)
        self.window.tracer(0)


        self.squarearea = 1350
        self.halfarea = self.squarearea/2
        self.hf = self.halfarea-2


        sqt = turtle.Turtle()
        sqt.color('white')
        sqt.penup()
        sqt.forward(self.halfarea)
        sqt.right(-90)
        sqt.forward(self.halfarea)
        sqt.pendown()
        for _ in range(4):
            sqt.right(-90)
            sqt.forward(self.squarearea)



        #create balls
        self.turtdic = []
        self.createballs(150,'red',0,self.turtdic)
        self.createballs(150,'green',1,self.turtdic)
        self.createballs(0,'blue',2,self.turtdic)
        self.createballs(0,'white',3,self.turtdic)

        self.colorlist = ['red','green','blue']
        self.window.update()

        #setup factors for forces and stuff
        self.rules = []
        for _ in range(4):
            self.rules.append([])
            for x in range(4):
                self.rules[-1].append(round(random.uniform(-2,2),2))
        print(str(self.rules))
        #self.rules = [[0,0],[0,0]]
        #self.rules = [[-1.43, -0.6, -1.67, 0.59, -0.19, 0.92, 1.17], [1.71, 1.02, -0.33, -0.71, 0.72, -1.28, -1.85], [-1.5, 0.96, 1.06, -0.5, -1.21, 1.08, -0.64], [-0.77, -1.99, 1.69, -1.95, 1.17, 0.89, -0.67], [1.82, 0.99, -0.96, 0.87, 0.26, 1.3, -1.86], [-1.36, -1.55, 0.36, 0.19, -0.2, -0.2, 1.13], [0.6, -1.58, -1.66, -0.28, -0.51, 1.33, -1.88]]
        #7's self.rules = [[1.69, 0.59, 0.25, 1.58, -0.71, 1.86, 1.66], [0.62, 0.15, -1.95, -0.18, 1.42, -1.26, -0.9], [1.84, -1.73, -1.87, -0.57, 1.48, -1.18, 1.87], [0.1, -1.56, 1.63, -0.59, -0.45, -1.83, 1.07], [-1.77, 1.28, 1.61, -0.45, 1.06, 0.2, -0.22], [-1.43, -0.39, -0.89, 0.1, -1.69, -0.29, -0.6], [-0.09, -1.02, 0.37, 0.5, 0.95, 0.86, -1.55]]
        #6's self.rules = [[0.27, 1.94, 0.08, 1.94, -2.49, 0.74], [-1.47, 1.06, 1.79, -1.86, -2.08, -0.27], [-1.03, 0.82, 0.06, 1.83, -4.12, -1.0], [0.03, 1.12, 1.15, 0.41, -1.13, -0.18], [-1.09, -0.37, 0.41, 5.9, -4.28, -0.07], [1.88, 0.82, -0.11, -0.48, -2.17, -1.92]]
        #6's self.rules = [[0.37, -1.32, 0.72, 0.61, -1.05, 1.61], [-1.0699999999999998, 0.15000000000000002, -0.72, -0.52, -1.76, 0.56], [-1.51, -2.1399999999999997, 1.7, 0.99, -1.41, -0.23], [1.37, -0.6, -0.95, -0.8999999999999999, -0.27, 0.51], [1.63, 0.15, 1.28, 0.98, -0.16000000000000003, 0.03], [-1.69, 0.08, 1.87, -1.28, 0.31999999999999995, 1.63]]

        #PARAMATERS LOGIC FOR SIM
        cf = 1.4 #making this bigger will "zoom" out, and the overall box will seem bigger
        self.farthestpoint = 500/cf
        self.peak1 = 45/cf #first point wheree force incresing
        self.seperateforce = 0.18
        self.peak2 = 140/cf


        
            
            
#-----------------------------options------------------------------------------------------------------
        inct = turtle.Turtle()
        inct.penup()
        inct.shape('circle')
        inct.shapesize(stretch_len=1.5,stretch_wid=1.5)
        inct.color('dark gray')
        inct.goto(-self.halfarea-250,self.halfarea-50)
        inct.write("   Click => ++ Radius Affect", font=("Verdana",12,"normal"))
        inct.onclick(self.incran)
        dec = turtle.Turtle()
        dec.penup()
        dec.shape('circle')
        dec.shapesize(stretch_len=1.5,stretch_wid=1.5)
        dec.color('dark gray')
        dec.goto(-self.halfarea-250,self.halfarea-120)
        dec.write("   Click => -- Radius Affect", font=("Verdana",12,"normal"))
        dec.onclick(self.dncran)
        res = turtle.Turtle()
        res.penup()
        res.shape('circle')
        res.shapesize(stretch_len=1.5,stretch_wid=1.5)
        res.color('dark gray')
        res.goto(-self.halfarea-250,self.halfarea-190)
        res.write("   Click => Reset self.rules", font=("Verdana",12,"normal"))
        res.onclick(self.resetr)
        sign = turtle.Turtle()
        sign.penup()
        sign.goto(-self.halfarea-250,self.halfarea-270)
        sign.pencolor('White')
        sign.write("adds 1", font=("Verdana",19,"normal"))
        for col1 in range(4):
            for col2 in range(4):
                rnturt = chooser(0.25,self.rules)
                rnturt.controlwhat = [col1,col2]
                rnturt.goto(-self.halfarea-270+40*col2,self.halfarea-290-40*col1)
        sign.goto(-self.halfarea-250,self.halfarea-580)
        sign.pencolor('White')
        sign.write("mins 1", font=("Verdana",19,"normal"))
        for col1 in range(4):
            for col2 in range(4):
                rnturt = chooser(-0.25,self.rules)
                rnturt.controlwhat = [col1,col2]
                
                rnturt.goto(-self.halfarea-270+40*col2,self.halfarea-600-40*col1)
        setz = turtle.Turtle()
        setz.penup()
        setz.goto(-self.halfarea-250,self.halfarea-1020)
        setz.shape('circle')
        setz.shapesize(stretch_len=1.5,stretch_wid=1.5)
        setz.color('dark gray')
        setz.write("   Click => self.rules to 0",font=("Verdana",12,"normal"))
        setz.onclick(self.disrule)
        setp = turtle.Turtle()
        setp.penup()
        setp.goto(-self.halfarea-250,self.halfarea-1100)
        setp.shape('circle')
        setp.shapesize(stretch_len=1.5,stretch_wid=1.5)
        setp.color('dark gray')
        setp.write("   Click => Reset Pos",font=("Verdana",12,"normal"))
        setp.onclick(self.respos)

        exa = turtle.Turtle()
        exa.goto(-self.halfarea-250,self.halfarea-1180)
        exa.shape('circle')
        exa.shapesize(stretch_len=1.5,stretch_wid=1.5)
        exa.color('red')
        exa.write("   Click => Q goto render",font=("Verdana",12,"normal"))
        exa.onclick(self.exitred)

        rer = turtle.Turtle()
        rer.goto(-self.halfarea-250,self.halfarea-1180)
        rer.shape('circle')
        rer.shapesize(stretch_len=1.5,stretch_wid=1.5)
        rer.color('red')
        rer.write("   Click => Delete render",font=("Verdana",12,"normal"))
        rer.onclick(self.exitred)
        
        self.gentha = turtle.Turtle()
        self.gentha.color('dark red')
        self.gentha.shape('square')
        self.gentha.penup()
        self.gentha.shapesize(stretch_len=2,stretch_wid=2)
        self.gentha.ondrag(self.genball)
        
        self.rnoncol = 0
        self.gencols = ["red",0]

        self.eraser = turtle.Turtle()
        self.eraser.color('white')
        self.eraser.shape('square')
        self.eraser.goto(500,500)
        self.eraser.penup()
        self.eraser.shapesize(stretch_len=2,stretch_wid=2)
        self.eraser.ondrag(self.delball)

        chbalcol = turtle.Turtle()
        chbalcol.penup()
        chbalcol.color('dark gray')
        chbalcol.shape('circle')
        chbalcol.goto(self.halfarea+20,self.halfarea-50)
        chbalcol.shapesize(stretch_len=1.5,stretch_wid=1.5)
        chbalcol.write("   Click => Change generator",font=("Verdana",12,"normal"))
        chbalcol.onclick(self.changegenball)
#-----------------------------------------------------------------------------------------------------------



        self.renderfile = open("./renderdata/renderdoc.txt","w")
        self.renderfile.write("!"+str(50)+"!"+str(2000)+"!"+str(1400)+"!"+str(self.squarearea)+"~") #paramaters for game -- !#playrs + screenwid + screenhei + self.squarearea!


        self.movinglist = [[0,0] for i in range(len(self.turtdic))]

        self.runprogram()

        self.window.mainloop()






    #turtle graphics options bar
 
    #@jit(nopython=True)
    def runprogram(self):
        while True:
            for b1i in range(len(self.turtdic)):
                b1 = self.turtdic[b1i]
                for b2i in range(b1i+1,len(self.turtdic)):

                    b2 = self.turtdic[b2i]

                    #alternate positions for second point!!!!!, find closet pont, to have affection
                    #find shortset distance to point affection
                    disx = b1.xcor()-b2.xcor()
                    disy = b1.ycor()-b2.ycor()

                    #check xes
                    disxalt = b1.xcor()-(b2.xcor()+self.squarearea)
                    disxaltop = b1.xcor()-(b2.xcor()-self.squarearea)
                    disyalt = b1.ycor()-(b2.ycor()+self.squarearea) #square on top
                    disyaltop = b1.ycor()-(b2.ycor()-self.squarearea) #square on the botttom
                    if not (abs(disxalt) < abs(disxaltop)):
                        disxalt = disxaltop
                    if not (abs(disyalt) < abs(disyaltop)):
                        disyalt = disyaltop
                    
                    finalDistanceX = math.sqrt(disxalt**2+disy**2)
                    finalDistanceY = math.sqrt(disx**2+disyalt**2)
                    disxy = math.sqrt(disx**2+disy**2) 

                    if finalDistanceX < disxy:
                        disxy = finalDistanceX
                        disx = disxalt

                    if finalDistanceY < disxy:
                        disxy = finalDistanceY
                        disy = disyalt
                        disx = b1.xcor()-b2.xcor()

                    
                    r1 = self.rules[b1.cvalues][b2.cvalues] 
                    r2 = self.rules[b2.cvalues][b1.cvalues]


                    #error divison by 0
                    if disxy <= 1:
                        continue
                    if disxy >= self.farthestpoint:
                        continue
                    #we will do piecewise function, NOT ABSOLUTE VALUE, for less complexity. These are self.rules for particles(not gravity physics, because not beautiful)
                    elif disxy <= self.peak1: #the intensity of seperate dots, line slope
                        ruleb1 = (self.seperateforce/(self.peak1))*disxy-self.seperateforce
                        ruleb2 = (self.seperateforce/(self.peak1))*disxy-self.seperateforce
                    elif disxy <= self.peak2:
                        #self.rules control repel or attract
                        ruleb1 = (r1/(self.peak2-self.peak1))*(disxy-self.peak1)
                        ruleb2 = (r2/(self.peak2-self.peak1))*(disxy-self.peak1)
                    else:
                        #self.rules control repel or attract
                        ruleb1 = 0-(r1/(self.farthestpoint-self.peak2))*(disxy-self.farthestpoint)
                        ruleb2 = 0-(r2/(self.farthestpoint-self.peak2))*(disxy-self.farthestpoint)
                

                    #deal with ball 1:
                    overallForce1 = ruleb1/200 #distance, overall force (1/(disxy**2))* #ADD THIS IN FOR SQRT DISTANCE
                    overallX1 = 0-overallForce1*disx #these are forces applyed
                    overallY1 = 0-overallForce1*disy
                    #deal with ball 2: 
                    overallForce2 = ruleb2/200 #distance, overall force (1/(disxy**2))* #ADD THIS IN FOR SqRT DISTANCE
                    overallX2 = overallForce2*disx #these are forces applyed
                    overallY2 = overallForce2*disy

                    if disxy <= self.peak1:
                        overallX1 = 0-ruleb1*disx
                        overallY1 = 0-ruleb1*disy
                        overallX2 = ruleb2*disx
                        overallY2 - ruleb2*disy

                    
                    #MOVINGT HE BALL AND THE VELOCITYS AND PUT INTO THE LIST
               
                    self.movinglist[b1i][0] += overallX1
                    self.movinglist[b1i][1] += overallY1
                    self.movinglist[b2i][0] += overallX2
                    self.movinglist[b2i][1] += overallY2




                    #out of bounds
                    if b1.xcor() >= self.halfarea:
                        b1.setx(b1.xcor()-self.squarearea-1)
                        

                    elif b1.xcor() <= -self.halfarea:
                        b1.setx(b1.xcor()+self.squarearea+1)

                    if b1.ycor() >= self.halfarea:
                        b1.sety(b1.ycor()-self.squarearea-1)
                    elif b1.ycor() <= -self.halfarea:
                        b1.sety(b1.ycor()+self.squarearea+1)

                    if b2.xcor() >= self.halfarea:
                        b2.setx(b2.xcor()-self.squarearea-1)
                    elif b2.xcor() <= -self.halfarea:
                        b2.setx(b2.xcor()+self.squarearea+1)

                    if b2.ycor() >= self.halfarea:
                        b2.sety(b2.ycor()-self.squarearea-1)
                    elif b2.ycor() <= -self.halfarea:
                        b2.sety(b2.ycor()+self.squarearea+1)

            #rendering part -- delete this part if no rendering
            self.renderfile.write(str([[round(i.xcor(),2),round(i.ycor(),2)] for i in self.turtdic])) #add positions to document
            

            self.window.update()

            for itemturti in range(len(self.turtdic)):
                itemturt = self.turtdic[itemturti]
                itemturt.velocityxy[0] = self.movinglist[itemturti][0] + 0.55*itemturt.velocityxy[0] #these are forces now, and accelaton last
                itemturt.velocityxy[1] = self.movinglist[itemturti][1] + 0.55*itemturt.velocityxy[1]
                itemturt.move()

                self.movinglist[itemturti] = [0,0]


                if itemturt.xcor() >= self.halfarea:
                    itemturt.setx(itemturt.xcor()-self.squarearea-1)
                        

                elif itemturt.xcor() <= -self.halfarea:
                    itemturt.setx(itemturt.xcor()+self.squarearea+1)

                if itemturt.ycor() >= self.halfarea:
                    itemturt.sety(itemturt.ycor()-self.squarearea-1)
                elif itemturt.ycor() <= -self.halfarea:
                    itemturt.sety(itemturt.ycor()+self.squarearea+1)





    def incran(self,x=0,y=0):
        self.farthestpoint += 20
        print(str(self.farthestpoint))
    def dncran(self,x=0,y=0):
        self.farthestpoint -= 20
        print(str(self.farthestpoint))
    def resetr(self,x=0,y=0):
        for c in range(4):
            for x in range(4):
                self.rules[c][x]=round(random.uniform(-2,2),2)
        print(str(self.rules))
    def disrule(self,x=0,y=0):
        for c in range(4):
            for x in range(4):
                self.rules[c][x]=0
    def respos(self,x=0,y=0):
        for thing in self.turtdic:
            thing.goto(random.uniform(-self.hf,self.hf),random.uniform(-self.hf,self.hf))
    def exitred(self,x=0,y=0):
        self.window.clearscreen()
        newwnd = partliferender.runfunc("renderdoc")
    def createballs(self,numball,color,cvalue,listappend,x=None,y=None):
        for _ in range(numball):
            newbody = modball()
            newbody.goto(random.uniform(-self.hf,self.hf),random.uniform(-self.hf,self.hf))
            newbody.color(color)
            newbody.cvalues = cvalue #affecton, i move  to what particles forces: me to me with force 1
            listappend.append(newbody)
        if x != None:
            newbody.goto(x,y)

    def genball(self,x=0,y=0): #makes reds
        self.gentha.ondrag(None)
        self.createballs(1,self.gencols[0],self.gencols[1],self.turtdic,x=self.gentha.xcor(),y=self.gentha.ycor())
        self.movinglist.append([0,0])
        self.gentha.goto(x,y)
        self.gentha.ondrag(self.genball)
    
    def genballbase(self,x=0,y=0): #makes basis for generatior
        
        self.createballs(1,self.gencols[0],self.gencols[1],self.turtdic,x=self.gentha.xcor(),y=self.gentha.ycor())
        self.movinglist.append([0,0])
        self.gentha.goto(x,y)
        

    def changegenball(self,x=0,y=0):
        self.rnoncol += 1
        if self.rnoncol == len(self.colorlist):
            self.rnoncol = 0

        self.gencols = [self.colorlist[self.rnoncol],self.rnoncol]
        self.gentha.color("dark " + self.gencols[0])

    def delball(self,x=0,y=0): #this function deletes turtles
        #self.eraser.ondrag(None)
        self.eraser.goto(x,y)
        for eraserballi in range(len(self.turtdic)): 
            eraserball = self.turtdic[eraserballi]
            if abs(eraserball.xcor()-x)<40 and abs(eraserball.ycor()-y)<40:
                #within range, erase balls!!!!    
                self.turtdic.pop(eraserballi)
                self.movinglist.pop(eraserballi)      
                eraserball.hideturtle()
        self.eraser.ondrag(self.delball)



mygame = runrender()
 