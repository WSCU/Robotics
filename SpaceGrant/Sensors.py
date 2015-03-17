'''
Author: Graham Montgomery
Western State Colorado University

This holds the sensor super class for every sensor that is written into the 
Engine. It also holds a list of every sensor that is dieclared for an individual 
project to be used by the Engine heartbeat.
'''

from PiFace import pi
from Motors import outpin
import serial
import string
import time as t
import picamera
import cv

#Global Sensor List
sensorList = []

#Sensor Class
#Super class for every sensor object, act as digital proxies to robot sensors
#IRSensor, SonarSensor, BeaconSensor
class Sensor:

    def __init__(self):
        sensorList.append(self)
        self.value = 0
    
    # update will be used by every sensor to update it's value every tick
    def update():
        pass

class Input(Sensor):

    def __init__(self, pin):
        Sensor.__init__(self)
        self.pin = pin + 1
        self.value = 0

    def update(self):
        self.value = pi.digital_read(self.pin)

class Camera(Sensor):

    def __init__(self):
        Sensor.__init__(self)
        self.camera = picamera.PiCamera()
        self.value = 0 
        self.nexttime = 0

    def update(self):
        time = self.nexttime - t.time()
        if time < 0:
            self.camera.capture("pic" + str(self.value) + ".jpg")
            self.value = (self.value + 1) % 5 
            self.nexttime = t.time() + 3 


class Sonar(Sensor):

    def __init__(self, inpin, outpin):
        Sensor.__init__(self)
        self.echo = inpin+1
        self.trig = outpin+1
        self.step = 0
    
    def update(self):
        #print "updating sonar"
        pi.digital_write(self.trig, 1)
        t.sleep(0.00001)
        pi.digital_write(self.trig, 0)

        start = t.time()
        test = start

        while pi.digital_read(self.echo) == 0:
            start = t.time()
            if test + .15 > t.time():
                end = -1
                print "failure"
                self.value = -1
                return
        
        end = start

        while pi.digital_read(self.echo) == 1:
            end = t.time()
            if end > start + .15:
                end = -1
                print "failure to get distance"
                self.value = -1
                return
            #t.sleep(.0001)

        timing = end - start
        self.value = (timing*340.29)
        print "done"

        pi.digital_write(self.trig, 0)

class Beacon(Sensor):

    def __init__(self):
        Sensor.__init__(self)
        self.updateTime = t.time()
        self.beac = 0
        self.comp = 0

    def update(self):
        ct = t.time()
        if ct > self.updateTime:
            test=serial.Serial("/dev/ttyAMA0",9600, timeout = 1)
            test.open()
            failed = False
            try:
                #print "attempting"
                line = test.readline()
                snums = line.split(",") # nums[0] beacon, nums[1] compass heading
                #inp = string.translate(line, rot13)
                try:
                    self.comp = int(str(snums[0]))
                    self.beac = int(str(snums[1]))
                except ValueError:
                    Failed = True
            except KeyboardInterrupt:
                pass
            if self.beac >= 200:
                self.value = 200
            elif failed:
                self.value = 201
            else:
                self.value = (self.comp - self.beac + 90) % 180 
            test.close()
            self.updateTime = ct + 3

def camera():
    return Camera()

def IR(pin):
    return Input(pin)

def button(pin):
    return Input(pin)
