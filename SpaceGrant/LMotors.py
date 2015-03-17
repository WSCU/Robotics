'''
Author: Graham Montgomery
Western State Colorado University

This is where the motor controllers will be defined along with anykind of output
'''

#from PiFace import pi
import os # for speaking to the motor controllers
#from subprocess import call
'''
class Output:

    def __init__(self, pin):
        self.pin = pin + 1

    def set(self, out):
        pi.digital_write(self.pin, out)

def outpin(pin):
    return Output(pin)
'''
class Motor:

    def __init__(self, serialpin):
        self.serialpin = serialpin
        os.system('./SmcCmd -d ' + str(self.serialpin) + ' --resume')

    def set(self, speed):
        #print "in motor"
        os.system('./SmcCmd -d ' + str(self.serialpin) + ' --speed ' + str(speed))

    def brake(self, power):
        os.system('./SmcCmd -d ' + str(self.serialpin) + ' --speed ' + str(power))

    def stop(self):
        self.set(0)
        
