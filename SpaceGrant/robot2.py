'''
Author: Graham Montgomery

This is the main program for the robot, that will be set to run on boot.
We will move this time!
'''

# import engine
from Engine import *


# define Motors

rMotor = Motor('51FF-7B06-4980-4956-2030-1087')
lMotor = Motor('51FF-7406-4980-4956-3330-1087')

# define beacon

#b = Beacon()

#define sensors
'''
uncomment lines after debugging
'''

but = button(0)
#sFront = Sonar(7, 7)
#sRight = Sonar(6, 6)
#sLeft = Sonar(5, 5)
#sLeft = Sonar(4, 4)

#define Motor Behaviors

def move(rSpeed, lSpeed):
    rMotor.set(rSpeed)
    lMotor.set(lSpeed)

#define special behaviors for avoidance

def avoidFront():
    move(-1600, -800)
    t.sleep(.5)
    move(1600, 1600)
    t.sleep(.25)

def turnToBeacon(deg):
    speed = 1600
    if deg > 89:
        deg -= 89*2
        speed *= -1
    move(speed, -speed)
    t.sleep(deg/89)

#define logic

def logic():
    if b.value is 200:
        move(0,0)
    elif b.value is 0:
        move(1600, 1600)
    elif b.value > 89:
        move(800, -800)
    else:
        move(-800, 800)

def dunes():
    if b.value < 170 or b.value > 10:
        turnToBeacon(b.value)
    elif sFront.value != -1 and sFront.value < .3:
        avoidFront()
    else:
        move(3000, 3000)

class data:
    def __init__(self):
        pass

global g 
g = data()
g.count = 0

def fbb():
    global g
    '''
    if g.count is 22/2:
        move(0, 0)
        e.stop()
    elif g.count <= 8/2:
        sl = 1600 - g.count * 400
    elif g.count <= 13/2:
        sl = 0
    #elif g.count <= 21/2:
        #sl = (-1600) + (g.count - 21/2) * 400
    '''
    #print sl
    if g.count is 0:
        move(2000,2500)
    if but.value is 1:
        move(0,0)
        e.stop()
    g.count = g.count + 1
    


e = engine(fbb, .1)

t.sleep(5)
e.spin() 
