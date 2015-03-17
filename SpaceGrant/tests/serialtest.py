#!/usr/bin/env python

import serial
import string
import time as t

rot13 = string.maketrans( 
    "ABCDEFGHIJKLMabcdefghijklmNOPQRSTUVWXYZnopqrstuvwxyz", 
    "NOPQRSTUVWXYZnopqrstuvwxyzABCDEFGHIJKLMabcdefghijklm")

test=serial.Serial("/dev/ttyAMA0",9600, timeout = 1)
test.open()

try:
    while True:
                print "attempting"
                line = test.readline()
                #inp = string.translate(line, rot13)
                print line
                t.sleep(3)
                
except KeyboardInterrupt:
    pass # do cleanup here

test.close()
