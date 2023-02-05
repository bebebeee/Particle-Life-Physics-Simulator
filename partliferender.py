print('s')
import turtle
import random
import math
import time
import shutil
import os

class modball(turtle.Turtle):
        def __init__(self,*args,**kwargs):
            super(modball,self).__init__(*args,**kwargs)
            self.penup()
            self.shape('circle')
            self.velocityxy = [0,0]
            self.shapesize(stretch_wid=0.3, stretch_len=0.3)
            self.cvalues = -1
            self.speed(0)

class runfunc(): #no need to add .txt at end of file
    def __init__(self,rfile):
        self.rfilenm = rfile
        renddoc = open("./renderdata/"+self.rfilenm+".txt",'r')
        nowchar = ''
        infodic = ['','','',''] #str(170)+"!"+str(2000)+"!"+str(1400)+"!"+str(squarearea)+"~
        nowon = -1

        while True:
            nowchar = renddoc.read(1)
            if nowchar == '!':
                nowon += 1
            elif nowchar == '~':
                break
            else:
                infodic[nowon] += nowchar

        infodic = [int(i) for i in infodic]
               

        self.window = turtle.Screen()
        self.window.bgcolor("black")
        self.window.setup(width=infodic[1], height=infodic[2])
        self.window.tracer(0)


        squarearea = infodic[3]
        self.havearea = squarearea/2
        hf = self.havearea-2


        sqt = turtle.Turtle()
        sqt.color('white')
        sqt.penup()
        sqt.forward(self.havearea)
        sqt.right(-90)
        sqt.forward(self.havearea)
        sqt.pendown()
        for _ in range(4):
            sqt.right(-90)
            sqt.forward(squarearea)

        
        
        #create balls
        turtdic = []
        self.createballs(infodic[0],'red',0,turtdic,hf)
        self.createballs(infodic[0],'green',1,turtdic,hf)
        self.createballs(infodic[0],'blue',2,turtdic,hf)
        self.createballs(infodic[0],'white',3,turtdic,hf)
        self.createballs(infodic[0],'orange',4,turtdic,hf)
        self.createballs(infodic[0],'purple',5,turtdic,hf)
        self.createballs(infodic[0],'yellow',6,turtdic,hf)
        self.window.update()





        lastchara = 'as'
        valueon = 0
        valuevalue = ''
        nowlist=[]
        self.timers = 0
        
        self.window.listen()
        self.window.onkey(self.pauseg,'space')

        

        sliderturt = turtle.Turtle()
        sliderturt.penup()
        sliderturt.color('gray')
        sliderturt.goto(-self.havearea-100,self.havearea-70)
        sliderturt.shapesize(stretch_wid=1,stretch_len=9)
        sliderturt.shape('square')
        sliderturt.onclick(self.timerss)

        bturt = turtle.Turtle()
        bturt.penup()
        bturt.color('red')
        bturt.goto(-self.havearea-250,self.havearea-140)
        bturt.shapesize(stretch_wid=1.5,stretch_len=1.5)
        bturt.shape('circle')
        bturt.write("     Set speed to 0 NW", font=("Verdana",12,"normal"))
        bturt.onclick(self.restime)

        sv = turtle.Turtle()
        sv.penup()
        sv.color('grey')
        sv.goto(-self.havearea-250,self.havearea-220)
        sv.shapesize(stretch_wid=1.5,stretch_len=1.5)
        sv.shape('circle')
        sv.write("      Save Render(if like this)", font=("Verdana",12,"normal"))
        sv.onclick(self.savefile)

        af = turtle.Turtle()
        af.penup()
        af.color('grey')
        af.goto(-self.havearea-250,self.havearea-300)
        af.shapesize(stretch_wid=1.5,stretch_len=1.5)
        af.shape('circle')
        af.write("      Render Saved File", font=("Verdana",12,"normal"))
        af.onclick(self.choosefile)

        re = turtle.Turtle()
        re.penup()
        re.color('grey')
        re.goto(-self.havearea-250,self.havearea-380)
        re.shapesize(stretch_wid=1.5,stretch_len=1.5)
        re.shape('circle')
        re.write("      Replay This Render", font=("Verdana",12,"normal"))
        re.onclick(self.replayrender)

        while True: #rendering loops
            nowchar = renddoc.read(1)
            if not nowchar:
                break
            if nowchar == '[':
                continue
            if nowchar == ']':
                if lastchara == ']':
                    valueon = 0
                    valuevalue = ''
                    self.window.update()
                    time.sleep(self.timers)
                elif lastchara != ']':
                    nowlist.append(float(valuevalue))
                    turtdic[valueon].goto(nowlist[0],nowlist[1])
                    valueon += 1
                    valuevalue = ''
                nowlist = []
                lastchara = nowchar
                continue
            if nowchar == ',' and lastchara != ']':
                #moving!
                nowlist.append(float(valuevalue))
                valuevalue=''
                continue
            elif nowchar == ',':
                continue
            
                
            valuevalue += nowchar
            lastchara = nowchar
        self.window.mainloop()












    def createballs(self,numball,color,cvalue,listappend,hf):
        for _ in range(numball):
            newbody = modball()
            newbody.goto(random.uniform(-hf,hf),random.uniform(-hf,hf))
            newbody.color(color)
            newbody.cvalues = cvalue #affecton, i move  to what particles forces: me to me with force 1
            listappend.append(newbody)
    def pauseg(self):
        time.sleep(0.5)


    def timerss(self,x=0,y=0):

        if self.timers == 0:
            self.timers = 0.05
            print('ok')
        centrm = (x-(-self.havearea-100))/100
        self.timers = self.timers*4**centrm

    def restime(self,x=0,y=0):
        self.timers = 0
 


    def savefile(self,x=0,y=0):
        filename = turtle.textinput("New File","Please Enter Your New File's Name :)")
        shutil.copy("./renderdata/renderdoc.txt","./renderdata/"+filename + ".txt")
    def choosefile(self,x=0,y=0):
        allposses = os.listdir("./renderdata")
        print('check')
        filename = turtle.textinput("Render Exist","Enter File Render (DO NOT ADD .txt): "+str(allposses))
        if filename+".txt" not in allposses:
            print('Illegal File!!')
        else:
            self.window.clearscreen()
            runfunc(filename)
    def replayrender(self,x=0,y=0):
        self.window.clearscreen()
        runfunc(self.rfilenm)
