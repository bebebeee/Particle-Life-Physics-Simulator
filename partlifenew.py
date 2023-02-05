print('s')
import turtle
import random
import math
import time
import sys
import partliferender
#import partliferender

window = turtle.Screen()
window.bgcolor("black")
window.setup(width=2000, height=1400)
window.tracer(0)


squarearea = 1350
havearea = squarearea/2
hf = havearea-2


sqt = turtle.Turtle()
sqt.color('white')
sqt.penup()
sqt.forward(havearea)
sqt.right(-90)
sqt.forward(havearea)
sqt.pendown()
for _ in range(4):
    sqt.right(-90)
    sqt.forward(squarearea)

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
    def __init__(self,adval,*args,**kwargs):
        super(chooser,self).__init__(*args,**kwargs)
        self.penup()
        self.color('white')
        self.shape('square')
        self.controlwhat = []
        self.onclick(self.incrul)
        self.adval = adval
       

        
    def incrul(self,x,y):
        global rules
        self.inputrules = rules
        self.inputrules[self.controlwhat[0]][self.controlwhat[1]] += self.adval
        print(str(self.inputrules))
        rules = self.inputrules

    
def createballs(numball,color,cvalue,listappend,hf):
    for _ in range(numball):
        newbody = modball()
        newbody.goto(random.uniform(-hf,hf),random.uniform(-hf,hf))
        newbody.color(color)
        newbody.cvalues = cvalue #affecton, i move  to what particles forces: me to me with force 1
        listappend.append(newbody)


#create balls
turtdic = []
createballs(150,'red',0,turtdic,hf)
createballs(150,'green',1,turtdic,hf)
createballs(150,'blue',2,turtdic,hf)
createballs(150,'white',3,turtdic,hf)
createballs(150,'orange',4,turtdic,hf)
createballs(150,'purple',5,turtdic,hf)
createballs(150,'yellow',6,turtdic,hf)

window.update()

#setup factors for forces and stuff
rules = []
for _ in range(7):
    rules.append([])
    for x in range(7):
        rules[-1].append(round(random.uniform(-2,2),2))
print(str(rules))
#rules = [[0,0],[0,0]]
#7's rules = [[1.69, 0.59, 0.25, 1.58, -0.71, 1.86, 1.66], [0.62, 0.15, -1.95, -0.18, 1.42, -1.26, -0.9], [1.84, -1.73, -1.87, -0.57, 1.48, -1.18, 1.87], [0.1, -1.56, 1.63, -0.59, -0.45, -1.83, 1.07], [-1.77, 1.28, 1.61, -0.45, 1.06, 0.2, -0.22], [-1.43, -0.39, -0.89, 0.1, -1.69, -0.29, -0.6], [-0.09, -1.02, 0.37, 0.5, 0.95, 0.86, -1.55]]
#6's rules = [[0.27, 1.94, 0.08, 1.94, -2.49, 0.74], [-1.47, 1.06, 1.79, -1.86, -2.08, -0.27], [-1.03, 0.82, 0.06, 1.83, -4.12, -1.0], [0.03, 1.12, 1.15, 0.41, -1.13, -0.18], [-1.09, -0.37, 0.41, 5.9, -4.28, -0.07], [1.88, 0.82, -0.11, -0.48, -2.17, -1.92]]
#6's rules = [[0.37, -1.32, 0.72, 0.61, -1.05, 1.61], [-1.0699999999999998, 0.15000000000000002, -0.72, -0.52, -1.76, 0.56], [-1.51, -2.1399999999999997, 1.7, 0.99, -1.41, -0.23], [1.37, -0.6, -0.95, -0.8999999999999999, -0.27, 0.51], [1.63, 0.15, 1.28, 0.98, -0.16000000000000003, 0.03], [-1.69, 0.08, 1.87, -1.28, 0.31999999999999995, 1.63]]

#PARAMATERS LOGIC FOR SIM
cf = 1.6 #making this bigger will "zoom" out, and it will seem bigger
farthestpoint = 200/cf
peak1 = 21/cf #first point wheree force incresing
seperateforce = 0.5
peak2 = 100/cf


#turtle graphics options bar
def incran(x=0,y=0):
    global farthestpoint
    farthestpoint += 20
    print(str(farthestpoint))
def dncran(x=0,y=0):
    global farthestpoint
    farthestpoint -= 20
    print(str(farthestpoint))
def resetr(x=0,y=0):
    global rules
    rules = []
    for _ in range(7):
        rules.append([])
        for x in range(7):
            rules[-1].append(round(random.uniform(-2,2),2))
    print(str(rules))
def disrule(x=0,y=0):
    global rules
    for c in range(7):
        for x in range(7):
            rules[c][x]=0
def respos(x=0,y=0):
    global turtdic
    for thing in turtdic:
        thing.goto(random.uniform(-hf,hf),random.uniform(-hf,hf))
def exitred(x=0,y=0):
    window.clearscreen()
    newwnd = partliferender.runfunc("renderdoc")
    
    
    

inct = turtle.Turtle()
inct.penup()
inct.shape('circle')
inct.shapesize(stretch_len=1.5,stretch_wid=1.5)
inct.color('dark gray')
inct.goto(-havearea-250,havearea-50)
inct.write("   Click => ++ Radius Affect", font=("Verdana",12,"normal"))
inct.onclick(incran)
dec = turtle.Turtle()
dec.penup()
dec.shape('circle')
dec.shapesize(stretch_len=1.5,stretch_wid=1.5)
dec.color('dark gray')
dec.goto(-havearea-250,havearea-120)
dec.write("   Click => -- Radius Affect", font=("Verdana",12,"normal"))
dec.onclick(dncran)
res = turtle.Turtle()
res.penup()
res.shape('circle')
res.shapesize(stretch_len=1.5,stretch_wid=1.5)
res.color('dark gray')
res.goto(-havearea-250,havearea-190)
res.write("   Click => Reset Rules", font=("Verdana",12,"normal"))
res.onclick(resetr)
sign = turtle.Turtle()
sign.penup()
sign.goto(-havearea-250,havearea-270)
sign.pencolor('White')
sign.write("adds 1", font=("Verdana",19,"normal"))
for col1 in range(7):
    for col2 in range(7):
        rnturt = chooser(0.25)
        rnturt.controlwhat = [col1,col2]
        rnturt.goto(-havearea-270+40*col2,havearea-290-40*col1)
sign.goto(-havearea-250,havearea-580)
sign.pencolor('White')
sign.write("mins 1", font=("Verdana",19,"normal"))
for col1 in range(7):
    for col2 in range(7):
        rnturt = chooser(-0.25)
        rnturt.controlwhat = [col1,col2]
        rnturt.inputrules = rules
        rnturt.goto(-havearea-270+40*col2,havearea-600-40*col1)
setz = turtle.Turtle()
setz.penup()
setz.goto(-havearea-250,havearea-1020)
setz.shape('circle')
setz.shapesize(stretch_len=1.5,stretch_wid=1.5)
setz.color('dark gray')
setz.write("   Click => Rules to 0",font=("Verdana",12,"normal"))
setz.onclick(disrule)
setp = turtle.Turtle()
setp.penup()
setp.goto(-havearea-250,havearea-1100)
setp.shape('circle')
setp.shapesize(stretch_len=1.5,stretch_wid=1.5)
setp.color('dark gray')
setp.write("   Click => Reset Pos",font=("Verdana",12,"normal"))
setp.onclick(respos)

exa = turtle.Turtle()
exa.goto(-havearea-250,havearea-1180)
exa.shape('circle')
exa.shapesize(stretch_len=1.5,stretch_wid=1.5)
exa.color('red')
exa.write("   Click => Q goto render",font=("Verdana",12,"normal"))
exa.onclick(exitred)


renderfile = open("./renderdata/renderdoc.txt","w")
renderfile.write("!"+str(150)+"!"+str(2000)+"!"+str(1400)+"!"+str(squarearea)+"~") #paramaters for game -- !#playrs + screenwid + screenhei + squarearea!

while True:
    for b1i in range(len(turtdic)):
        b1 = turtdic[b1i]
        for b2 in turtdic[b1i+1:]:
            #alternate positions for second point!!!!!, find closet pont, to have affection
            #find shortset distance to point affection
            disx = b1.xcor()-b2.xcor()
            disy = b1.ycor()-b2.ycor()

            #check xes
            disxalt = b1.xcor()-(b2.xcor()+squarearea)
            disxaltop = b1.xcor()-(b2.xcor()-squarearea)
            disyalt = b1.ycor()-(b2.ycor()+squarearea) #square on top
            disyaltop = b1.ycor()-(b2.ycor()-squarearea) #square on the botttom
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

            
            r1 = rules[b1.cvalues][b2.cvalues] 
            r2 = rules[b2.cvalues][b1.cvalues]


            #error divison by 0
            if disxy <= 1:
                continue
            if disxy >= farthestpoint:
                continue
            #we will do piecewise function, NOT ABSOLUTE VALUE, for less complexity. These are rules for particles(not gravity physics, because not beautiful)
            elif disxy <= peak1: #the intensity of seperate dots, line slope
                ruleb1 = (seperateforce/(peak1))*disxy-seperateforce
                ruleb2 = (seperateforce/(peak1))*disxy-seperateforce
            elif disxy <= peak2:
                #rules control repel or attract
                ruleb1 = (r1/(peak2-peak1))*(disxy-peak1)
                ruleb2 = (r2/(peak2-peak1))*(disxy-peak1)
            else:
                #rules control repel or attract
                ruleb1 = 0-(r1/(farthestpoint-peak2))*(disxy-farthestpoint)
                ruleb2 = 0-(r2/(farthestpoint-peak2))*(disxy-farthestpoint)
         

            #deal with ball 1:
            overallForce1 = ruleb1/200 #distance, overall force (1/(disxy**2))* #ADD THIS IN FOR SQRT DISTANCE
            overallX1 = 0-overallForce1*disx #these are forces applyed
            overallY1 = 0-overallForce1*disy
            #deal with ball 2: 
            overallForce2 = ruleb2/200 #distance, overall force (1/(disxy**2))* #ADD THIS IN FOR SqRT DISTANCE
            overallX2 = overallForce2*disx #these are forces applyed
            overallY2 = overallForce2*disy

            if disxy <= peak1:
                overallX1 = 0-ruleb1*disx
                overallY1 = 0-ruleb1*disy
                overallX2 = ruleb2*disx
                overallY2 - ruleb2*disy

            #deal with accelaration ball 1:
            b1.velocityxy[0] = 0.35*b1.velocityxy[0]+overallX1
            b1.velocityxy[1] = 0.35*b1.velocityxy[1]+overallY1
            #deal with accelaration ball 2:
            b2.velocityxy[0] = 0.35*b2.velocityxy[0]+overallX2
            b2.velocityxy[1] = 0.35*b2.velocityxy[1]+overallY2
            #move the ball actually
            b1.move()
            b2.move()

            #out of bounds
            if b1.xcor() >= havearea:
                b1.setx(b1.xcor()-squarearea-1)
                

            elif b1.xcor() <= -havearea:
                b1.setx(b1.xcor()+squarearea+1)

            if b1.ycor() >= havearea:
                b1.sety(b1.ycor()-squarearea-1)
            elif b1.ycor() <= -havearea:
                b1.sety(b1.ycor()+squarearea+1)

            if b2.xcor() >= havearea:
                b2.setx(b2.xcor()-squarearea-1)
            elif b2.xcor() <= -havearea:
                b2.setx(b2.xcor()+squarearea+1)

            if b2.ycor() >= havearea:
                b2.sety(b2.ycor()-squarearea-1)
            elif b2.ycor() <= -havearea:
                b2.sety(b2.ycor()+squarearea+1)

    #rendering part -- delete this part if no rendering
    renderfile.write(str([[round(i.xcor(),2),round(i.ycor(),2)] for i in turtdic])) #add positions to document
    

    window.update()


window.mainloop()
 