import sys
import rospy
from std_msgs.msg import String
global d
world = Tmap()

def createMap():
    global d
    #Setup the first Node
    while (unvisited):
        next_node = Tmap.nextUnvisited(current)
    #next = Tmap.nextUnvisited(current)
    #generateCommands(current, next)
    #wait for it to get to the next one
    #create a node
    #loop


def makeNode(current):
    #Use the neato lasers to find the corner type
    global d
    if d.cornerType = "D"
        world[i][j].count = 1 
        world[i][j].visited = True
    elif d.cornerType = "ST"
        world[i][j].count = 2
        
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
