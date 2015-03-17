'''
Author: Graham Montgomery
Western State Colorado University

This is the file any user will import
'''

import time as t
from PiFace import pi
from Sensors import *
from Motors import *

#Engine Class
#this is the center/heartbeat of the entire system
class Engine:
    def __init__(self, loopFunction, tick):
        self.tick = tick
        self.update = loopFunction
        self.nextTime = 0
        self.spinning = False;
            
    def setNextTime(self):
        '''
        for Engine use only
        sets the next time for the engine to update
        '''
        self.nextTime = t.time() + self.tick
        
    def spinOnce(self):
        ''':
        mostly used for debugging
        ticks the engine once
        '''
        for s in sensorList:
            s.update()
        self.update()

    def spin(self):
        '''
        user level, starts the engine tick
        '''
        self.spinning = True
        self.setNextTime()
        while self.spinning:
            wait = t.time() - self.nextTime
            if wait > 0:
                self.spinOnce()
                self.setNextTime()

    def stop(self):
        '''
        user level, stops the engine tick
        '''
        self.spinning = False
        self.nextTime = 0

#top level engine factory
def engine(loopFunction, tick):
    '''
    user level engine factory
    parameters:
    loopFunction: sent as the logi center. runs every tick after sensor update
    tick: duration between engine ticks
    '''
    return Engine(loopFunction, tick)
