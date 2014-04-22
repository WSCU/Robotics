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
    #TODO:
    #we need to add checking for already found nodes, do this later
    global d
    
    if d.cornerType = "D":
        pass
    elif d.cornerType = "ST"
        if d.facing == 0:
            current.setNorth(TMapNode(nodeCount(), "H"))
        elif d.facing == 1:
            current.setEast(TMapNode(nodeCount(), "H"))
        elif d.facing == 2:
            current.South(TMapNode(nodeCount(), "H"))
        elif d.facing == 3:
            current.setWest(TMapNode(nodeCount(), "H"))
    elif d.cornerType = "LR"
        if d.facing == 0:
            current.setEast(TmapNode(nodeCount(), "H"))
        elif d.facing == 2:
            current.setEast(TmapNode(nodeCount(), "H"))
        elif d.facing == 3:
            #TODO
    elif d.cornerType = "LL"
        if d.facing == 0:
            current.setWest(TMapNode(nodeCount(), "H"))
        elif d.facing == 1:
            current.setWest(TMapNode(nodeCount(), "H"))
        elif d.facing == 2:
            #TODO
    elif d.cornerType = "TU"
         if d.facing == 0 or d.facing == 2:
            current.setEast(TMapNode(nodeCount(), "H"))
            current.setWest(TMapNode(nodeCount(), "H"))
        elif d.facing == 1:
            current.setSouth(TMapNode(nodeCount(), "H"))
            #TODO
        elif d.facing == 3:
            current.setSouth(TMapNode(nodeCount(), "H"))
            #TODO
    elif d.cornerType = "TL":
        if d.facing == 3:
            current.setNorth(TMapNode(nodeCount(), "H"))
            current.setSouth(TMapNode(nodeCount(), "H"))
        elif d.facing == 0:
            current.setEast(TMapNode(nodeCount(), "H"))
        elif d.facing == 2:
            current.setEast(TMapNode(nodeCount(), "H"))
    elif d.cornerType = "TR"
        if d.facing == 1:
            current.setNorth(TMapNode(nodeCount(), "H"))
            current.setSouth(TMapNode(nodeCount(), "H"))
        elif d.facing == 0:
            current.setWest(TMapNode(nodeCount(), "H"))
        elif d.facing == 2:
            curretn.setWest(TmapNode(nodeCount(), "H"))
    elif d.cornerType = "+"
        
def nodeCount():
    global d    
    d.nodeCount += 1;
    return d.nodeCount -1;
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
