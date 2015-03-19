'''
Author: Graham Montgomery
Western State Colorado University

This is where the motor controllers will be defined along with anykind of output
'''

from PiFace import pi
import os # for speaking to the motor controllers

class Output:

    def __init__(self, pin):
        self.pin = pin + 1

    def set(self, out):
        pi.digital_write(self.pin, out)

def outpin(pin):
    return Output(pin)

def light(pin):
    return Output(pin)

class Motor:
    
    _AllMotors = []

    def _FullStop_():
        for motor in _AllMotors:
            motor.stop()

    def _ResetAll_():
        for motor in _AllMotors:
            os.system('/home/pi/Robotics/SpaceGrant/./SmcCmd -d ' + str(motor.serialpin) + ' --stop')
            os.system('/home/pi/Robotics/SpaceGrant/./SmcCmd -d ' + str(motor.serialpin) + ' --resume')

    def __init__(self, serialpin):
        self.serialpin = serialpin
        os.system('/home/pi/Robotics/SpaceGrant/./SmcCmd -d ' + str(self.serialpin) + ' --resume')

    def set(self, speed): 
        os.system('/home/pi/Robotics/SpaceGrant/./SmcCmd -d ' + str(self.serialpin) + ' --speed ' + str(speed))

    def brake(self, power):
        os.system('/home/pi/Robotics/SpaceGrant/./SmcCmd -d ' + str(self.serialpin) + ' --speed ' + str(power))

    def stop(self):
        self.set(0)
        
