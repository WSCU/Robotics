'''
Author: Graham Montgomery
Western State Colorado University

this test is to check if the camera works as it should
'''

from Engine import *
import time as t

global e
c = camera()
start = t.time()

def loop():
    if start + 30 < t.time():
        e.stop()

e = engine(loop, .5)
e.spin()
