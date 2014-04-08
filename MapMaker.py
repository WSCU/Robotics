import sys
import rospy
from std_msgs.msg import String
global d
maplength = 5
world = [[Node() for x in xrange(maplength)] for x in xrange(maplength)] 
unvisited = []


def createMap():
    #Setup the first Node
    makeNode(maplength/2,maplength/2)
    while (unvisited):
        previous = current
        current = unvisited.pop()
        

def makeNode(i,j):
    #Use the neato lasers to find the corner type
    if d.cornerType = "D"
        world[i][j].count = 1 
        world[i][j].visited = True
    elif d.cornerType = "ST"
        world[i][j].count = 2
        world[i][j]
    elif d.cornerType = "LR"
    elif d.cornerType = "LL"
    elif d.cornerType = "TU"
    elif d.cornerType = "TL"
    elif d.cornerType = "TR"
    elif d.cornerType = "+"
    
#Callback function 
def getCorner(data):
    d.cornerType = data.data 
 
def expandMap():

def move(i,j):
    
    
def main():
    d["Facing"] = North
    rospy.init_node('map_maker')
    rospy.Subscriber("hallwayType", String, getCorner)
    
    createMap()
if __name__ == "__main__":
    main()
