# -*- coding: utf-8 -*-
#
#     ||          ____  _ __
#  +------+      / __ )(_) /_______________ _____  ___
#  | 0xBC |     / __  / / __/ ___/ ___/ __ `/_  / / _ \
#  +------+    / /_/ / / /_/ /__/ /  / /_/ / / /_/  __/
#   ||  ||    /_____/_/\__/\___/_/   \__,_/ /___/\___/
#
#  Copyright (C) 2014 Bitcraze AB
#
#  Crazyflie Nano Quadcopter Client
#
#  This program is free software; you can redistribute it and/or
#  modify it under the terms of the GNU General Public License
#  as published by the Free Software Foundation; either version 2
#  of the License, or (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.

#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA  02110-1301, USA.

"""
Simple example that connects to the first Crazyflie found, ramps up/down
the motors and disconnects.
"""

import time, sys
import rospy
from std_msgs.msg import String
from threading import Thread

#FIXME: Has to be launched from within the example folder
sys.path.append("../lib")
import cflib
from cflib.crazyflie import Crazyflie

import logging
logging.basicConfig(level=logging.ERROR)
class Data: pass
D = Data()

class MotorRampExample:
    """Example that connects to a Crazyflie and ramps the motors up/down and
    the disconnects"""
    def __init__(self, link_uri):
        """ Initialize and run the example with the specified link_uri """
        
        self._cf = Crazyflie()

        self._cf.connected.add_callback(self._connected)
        self._cf.disconnected.add_callback(self._disconnected)
        self._cf.connection_failed.add_callback(self._connection_failed)
        self._cf.connection_lost.add_callback(self._connection_lost)

        self._cf.open_link(link_uri)

        print "Connecting to %s" % link_uri

    def _connected(self, link_uri):
        global D
        """ This callback is called form the Crazyflie API when a Crazyflie
        has been connected and the TOCs have been downloaded."""
        if D.logconf.valid:
            logconf.start()
        # Start a separate thread to do the motor test.
        # Do not hijack the calling thread!
        #Thread(target=self._ramp_motors).start()
        Thread(target = self._spin).start()

    def _connection_failed(self, link_uri, msg):
        """Callback when connection initial connection fails (i.e no Crazyflie
        at the speficied address)"""
        print "Connection to %s failed: %s" % (link_uri, msg)

    def _connection_lost(self, link_uri, msg):
        """Callback when disconnected after a connection has been made (i.e
        Crazyflie moves out of range)"""
        print "Connection to %s lost: %s" % (link_uri, msg)

    def _disconnected(self, link_uri):
        """Callback when the Crazyflie is disconnected (called in all cases)"""
        print "Disconnected from %s" % link_uri

    def _ramp_motors(self):
        global D
        thrust_mult = 1
        thrust_step = 200
        thrust = 10000
        pitch = 0
        roll = 0
        yawrate = 0
        while thrust >= 10000 and D.running:
            self._cf.commander.send_setpoint(roll, pitch, yawrate, thrust)
            time.sleep(0.1)
            if thrust >= 20000:
                thrust_mult = 0
            thrust += thrust_step * thrust_mult
        self._cf.commander.send_setpoint(0, 0, 0, 0)
        # Make sure that the last packet leaves before the link is closed
        # since the message queue is not flushed before closing
        time.sleep(0.1)
        self._cf.close_link()
    def _spin(self):
        global D
        while D.running:
            self._cf.commander.send_setpoint(D.roll, D.pitch, D.yawrate, D.thrust)

def logdataCB(data):
    global D
    D.pitch = data["stabilizer.pitch"]
    D.roll = data["stablilizer.roll"]
    D.gyrox = data["gyro.x"]
    D.gyroy = data["gyro.y"]
    D.gyroz = data["gyro.z"]
    D.accx = data["acc.x"]
    D.accy = data["acc.y"]
    D.accz = data["acc.z"]
    D.logPub.publish(String("Pitch,%d Roll,%d GyroX,%d GyroY,%d GyroZ,%d accX,%d accY%d, accZ%d" % (D.pitch, D.roll, D.gyrox, D.gyroy, D.gyroz, D.accx, D.accy, D.accz)))
    
def main():
    global D
    D.packet = Data()
    D.running = True
    D.roll = 0
    D.pitch = 0
    D.yawrate = 0
    D.thrust = 0
    #Subscribing and publishing
    rospy.init_node("crazyflie", anonymous = True)
    stream_name = "text_data"
    rospy.Subscriber("textdata", String, callback)
    D.logPub = rospy.Publisher("cf_logdata", String)
    #Logging
    D.logconf = LogConfig(name = "Logging", period_in_ms = 100)
    D.logconf.add_variable("stabilizer.pitch")
    D.logconf.add_variable("stabilizer.roll")
    D.logconf.add_variable("gyro.x")
    D.logconf.add_variable("gyro.y")
    D.logconf.add_variable("gyro.z")
    D.logconf.add_variable("acc.x")
    D.logconf.add_variable("acc.y")
    D.logconf.add_variable("acc.z")
    D.logconf.data_received_cb.add_callback(logdataCB)
    # Initialize the low-level drivers (don't list the debug drivers)
    cflib.crtp.init_drivers(enable_debug_driver=False)
    # Scan for Crazyflies and use the first one found
    print "Scanning interfaces for Crazyflies..."
    available = cflib.crtp.scan_interfaces()
    print "Crazyflies found:"
    for i in available:
        print i[0]

    if len(available) > 0:
        D.le = MotorRampExample(available[0][0])
    else:
        print "No Crazyflies found, cannot run example"
    rospy.spin()

def callback(data):
    global D
    m = data.data 
    print ("Received message: " + m)
    if m == 'q':
       D.le._cf.commander.send_setpoint(0, 0, 0, 0)
       D.running = False 
       D.le._cf.close_link() 
       rospy.signal_shutdown("Quit requested")
    elif m == 's':
        D.thrust = 0
        D.roll = 0
        D.pitch = 0
        D.yawrate = 0
    elif m.count(" ")>0:
        hpr,value=m.split(" ")
        if(hpr is "pitch" or hpr is "p"):
            D.pitch= int(value)
        if(hpr=="yawrate" or hpr is "y"):
            D.yawrate= int(value)
        if(hpr=="roll" or hpr is "r"):
            D.roll=int(value)
        if(hpr=="thrust" or hpr is "t"):
            D.thrust= int(value) * 1000
            print(value + ", " + str(D.thrust))
        if D.thrust <= 10000:
            print "low"
            D.thrust = 10001
        elif D.thrust > 60000:
            print "high"
            D.thrust = 60000
        print("Thrust" + value + ", " + str(D.thrust))
        print("Pitch" + str(D.pitch))
        print("roll" + str(D.roll))
        print("yaw" + str(D.yawrate))
if __name__ == '__main__':
    main()
