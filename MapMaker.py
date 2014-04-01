import sys

global d = {}
maplength = 5
world = [[Node() for x in xrange(maplength)] for x in xrange(maplength)] 
unvisited = [()]

def createMap():
    #Setup the first Node
    makeNode(maplength/2,maplength/2)
    while (unvisited):
        previous = current
        current = unvisited.pop()
        

def makeNode(i,j):
    #Use the neato lasers to find the corner type
    cornertype = getCorner()
    tank(0,0)
    if cornertype is cross:
        world[i][j].count = 4
        if world[i+1][j]!=previous
            world[i+1][j] = Node(1)
        if world[i-1][j]!=previous
            world[i-1][j] = Node(1)
        if world[i][j+1]!=previous
            world[i][j+1] = Node(1)
        if world[i][j-1]!=previous
            world[i][j-1] = Node(1)
    if cornertype is l1:
        world[i][j].count = 2
        if world[i][j+1] == previous
            world[i][j+1]= Node(1)
        if world[i][j-1] == previous
            world[i][j-1]= Node(1)
        world[i-1][j] = Node(1)
    if cornertype is l2:
        world[i][j].count = 2
        if world[i][j+1] == previous
            world[i][j+1]= Node(1)
        if world[i][j-1] == previous
            world[i][j-1]= Node(1)
        world[i+1][j] = Node(1)
    if cornertype is t:
        world[i][j].count = 3
        if world[i][j+1] == previous
            world[i][j+1]= Node(1)
        if world[i][j-1] == previous
            world[i][j-1]= Node(1)
        world[i-1][j] = Node(1)
        wordl[i+1][j] = Node(1)
    if cornertype is deadend:
        world[i][j].count = 1
        world[i][j] = Node(1)
 tank(50,50)
 
def getCorner():
    
 
def expandMap():

def move(i,j):
    
    
def main():
        d["Facing"] = North
       

    createMap()
if __name__ == "__main__":
    main()
