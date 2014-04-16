import sys
import rospy
from std_msgs.msg import String
global d
world = Tmap()

def createMap():
    global d
    #Setup the first Node
    while (unvisited):
        next_node, unvisited = world.nextUnvisited(current)
        if next_node is not None:
            world.generateCommands(current ,next_node)
            #wait for it to move
            current = next_node
            makeNode(current)
    #next = Tmap.nextUnvisited(current)
    #generateCommands(current, next)
    #wait for it to get to the next one
    #create a node
    #loop


def makeNode(current):
    #Use the neato lasers to find the corner type
    global d
    
    if d.cornerType = "D"
    
    elif d.cornerType = "ST"
    
    elif d.cornerType = "LR"
    
    elif d.cornerType = "LL"
    
    elif d.cornerType = "TU"
    
    elif d.cornerType = "TL"
    
    elif d.cornerType = "TR"
    
    elif d.cornerType = "+"
    
#Callback function 
def getCorner(data):
    d.cornerType = data.data 
 
def move(start,end):
    world.generateCommands(start, end)
    
def main():
    d.facing = North
    rospy.init_node('map_maker')
    rospy.Subscriber("hallwayType", String, getCorner)
    d.pub = rospy.Publisher("navCommand", NavCommand)
    
    createMap()
if __name__ == "__main__":
    main()
