import roslib
import rospy
from std_msgs.msg import String
import Leap, sys, thread, time
from Leap import CircleGesture, KeyTapGesture, ScreenTapGesture, SwipeGesture
import roslib;roslib.load_manifest('crazyflie_ros')
import cflib
from crazyflie.msg import *
from cflib.crazyflie import Crazyflie
import csv
import time
import math

class Data: pass

D = Data()
D.thrust = 0
D.lastZ = None
D.alTime = None
D.glTime = None
D.vel = None
D.pitch = 0
D.roll = 0
D.yaw = 0

D.lgx = None
D.lgy = None
D.lgz = None

D.lax = 0.0
D.lay = 0.0
D.dax = 0.0
D.day = 0.0
D.gyroCorrection = False
D.time = 0

class SampleListener(Leap.Listener):
    
    state_names = ['STATE_INVALID', 'STATE_START', 'STATE_UPDATE', 'STATE_END']

    def on_init(self, controller):
        print "Initialized"

    def on_connect(self, controller):
        print "Connected"

    def on_disconnect(self, controller):
        # Note: not dispatched when running in a debugger.
        print "Disconnected"

    def on_exit(self, controller):
        print "Exited"

    def on_frame(self, controller):
        # Get the most recent frame and report some basic information
        frame = controller.frame()
        # Get hands
        D.time = D.time + 1
        for hand in frame.hands:

            handType = "Left hand" if hand.is_left else "Right hand"
            # Get the hand's normal vector and direction
            normal = hand.palm_normal
            direction = hand.direction

            D.thrust = hand.fingers.frontmost.tip_position.y*350

            if hand.fingers.frontmost.tip_position.x < 0:
                D.roll = max(hand.fingers.frontmost.tip_position.x, -10)

            if hand.fingers.frontmost.tip_position.x > 0:
                D.roll = min(hand.fingers.frontmost.tip_position.x, 10)

            if hand.fingers.frontmost.tip_position.z < -60:
                D.pitch = max(-60-abs(hand.fingers.frontmost.tip_position.z),10)

            if hand.fingers.frontmost.tip_position.z > -60:
                D.pitch = min(-60+abs(hand.fingers.frontmost.tip_position.z),-10)

            
            if(D.time%10 == 0): 
                if(D.thrust < 40000):
                    D.dataPub.publish(String("t "+str(int(max(0,D.thrust)))))
                if(D.time > 200):
                    D.dataPub.publish(String("r "+str(int(D.roll))))
                D.dataPub.publish(String("p "+str(int(D.pitch))))
                print "Thrust: "+str(D.thrust)
                print "Pitch: "+str(D.pitch)
                print "Roll: "+str(D.roll)

def textCall(data):
    if data.data is 'q':
        rospy.signal_shutdown("quit")

def main():
    # Create a sample listener and controller
    listener = SampleListener()
    controller = Leap.Controller()

    rospy.init_node("leap_pub")
    D.dataPub = rospy.Publisher("cf_textcmd", String)
    rospy.Subscriber("cf_textcmd", String,textCall )

    # Have the sample listener receive events from the controller
    controller.add_listener(listener)
    # Keep this process running until Enter is pressed

    print "Press Enter to quit..."
    try:
        sys.stdin.readline()
    except KeyboardInterrupt:
        pass
    finally:
        # Remove the sample listener when done
        controller.remove_listener(listener)

if __name__ == "__main__":
    main()
