import roslib
import rospy
from std_msgs.msg import String
import Leap, sys, thread, time
from Leap import CircleGesture, KeyTapGesture, ScreenTapGesture, SwipeGesture
import Leap, sys, thread, time
from Leap import CircleGesture, KeyTapGesture, ScreenTapGesture, SwipeGesture
import roslib;roslib.load_manifest('crazyflie_ros')
import cflib
from std_msgs.msg import String
from crazyflie.msg import *
from cflib.crazyflie import Crazyflie
import csv
import time

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

class SampleListener(Leap.Listener):
    
    # finger_names = ['Thumb', 'Index', 'Middle', 'Ring', 'Pinky']
    # bone_names = ['Metacarpal', 'Proximal', 'Intermediate', 'Distal']
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
        for hand in frame.hands:

            handType = "Left hand" if hand.is_left else "Right hand"

           # print "position: %s" % (hand.palm_position)


            # Get the hand's normal vector and direction
            normal = hand.palm_normal
            direction = hand.direction

            # Calculate the hand's pitch, roll, and yaw angles
            print "  pitch: %f degrees, roll: %f degrees, yaw: %f degrees" % (
                direction.pitch * Leap.RAD_TO_DEG,
                normal.roll * Leap.RAD_TO_DEG,
                direction.yaw * Leap.RAD_TO_DEG)
            D.roll = direction.roll
            D.pitch = direction.pitch
            D.yaw = direction.yaw

        if not (frame.hands.is_empty and frame.gestures().is_empty):
            print ""


    # def state_string(self, state):
    #     if state == Leap.Gesture.STATE_START:
    #         return "STATE_START"

    #     if state == Leap.Gesture.STATE_UPDATE:
    #         return "STATE_UPDATE"

    #     if state == Leap.Gesture.STATE_STOP:
    #         return "STATE_STOP"

    #     if state == Leap.Gesture.STATE_INVALID:
    #         return "STATE_INVALID"
def accelCall(data):
    global D 
    D.dataPub.publish(String("t " + str(D.roll * 100)))
    #D.dataPub.publish(String("p " + str(D.pitch)))
    #D.dataPub.publish(String("y " + str(D.yaw)))
   
def motorCall(data):
    global D
    m1 = data.m1
    m2 = data.m2
    m3 = data.m3
    m4 = data.m4
    #print("Motors (1, 2, 3, 4): "+str(m1)+","+str(m2)+","+str(m3)+","+str(m4))
    
def textCall(data):
    if data.data is 'q':
        rospy.signal_shutdown("quit")
def main():
    global D
    rospy.init_node("leap_pub")
    D.dataPub = rospy.Publisher("cf_textcmd", String)
    rospy.Subscriber("cf_accData", accelData, accelCall) 
    rospy.Subscriber("cf_motorData", MotorData, motorCall)
    rospy.Subscriber("cf_textcmd", String,textCall )

    #rospy.spin()
    # Create a sample listener and controller
    listener = SampleListener()
    controller = Leap.Controller()

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
