import sys
import rospy
from Node import *
from std_msgs.msg import String
global d
world = Tmap()

def createMap():
    global d
    #Setup the first Node
    while (unvisited):
        next_node, unvisited = world.nextUnvisited(current)
        if next_node is not None:
            commands = world.generateCommands(current, next_node)
            #parse commands to get final facing direction after moving
            for e in commands:
                if e[0] == "L":
                    d.facing = (d.facing - 1) % 4
                elif e[0] == "R":
                    d.facing = (d.facing + 1) % 4
                elif e[0] == "TRND":
                    d.facing = (d.facing - 2) % 4
            #send the commands with the publisher
            d.pub.publish(commands)
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
        if d.facing == 0:
            current.setSouth(TMapNode(d.nodeCount, "H"))
        elif d.facing == 1:
            current.setWest(TMapNode(d.nodeCount, "H"))
        elif d.facing == 2:
            current.setNorth(TMapNode(d.nodeCount, "H"))
        elif d.facing == 3:
            current.setEast(TmapNode(d.nodeCount, "H"))
    elif d.cornerType = "ST"
        if d.facing == 0:
            current.setSouth(TMapNode(d.nodeCount, "H"))
            current.setNorth(TMapNode(d.nodeCount, "H"))
        elif d.facing == 1:
            current.setWest(TMapNode(d.nodeCount, "H"))
            current.setEast(TMapNode(d.nodeCount, "H"))
        elif d.facing == 2:
            current.setNorth(TMapNode(d.nodeCount, "H"))
            current.setSouth(TMapNode(d.nodeCount, "H"))
        elif d.facing == 3:
            current.setEast(TmapNode(d.nodeCount, "H"))
            current.setWest(TMapNode(d.nodeCount, "H"))
    elif d.cornerType = "LR"
        if d.facing == 0:
            current.setEast(TmapNode(d.nodeCount, "H"))
            current.setSouth(TMapNode(d.nodeCount, "H"))
        elif d.facing == 2:
            current.setNorth(TMapNode(d.nodeCount, "H"))
            current.setEast(TmapNode(d.nodeCount, "H"))
        elif d.facing == 3:
            current.setEast(TmapNode(d.nodeCount, "H"))
    elif d.cornerType = "LL"
        if d.facing == 0:
            current.setSouth(TMapNode(d.nodeCount, "H"))
            current.setWest(TMapNode(d.nodeCount, "H"))
        elif d.facing == 1:
            current.setWest(TMapNode(d.nodeCount, "H"))
        elif d.facing == 2:
            current.setNorth(TMapNode(d.nodeCount, "H"))
            current.setWest(TMapNode(d.nodeCount, "H"))
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
    global d
    d.nodeCount = 0
    d.facing = sys.argv[1]
    main()
