import roslib
import rospy
import cflib
from std_msgs.msg import String
from cflib.crazyflie import Crazyflie

class Data: pass
    D = Data()

def main():
    rospy.Subscriber("cf_logdata", String, callback)	

def hoverCall(data):
    global D
    m = data.data
    print ("Received message: " + m)
    pitch,roll,thrust,gyrox,gyroy,gyroz,accx,accy,accz = m.split(" ")
    """
    if gyrox > 1 or gyrox < -1:
        roll = -gyrox * 0.2
    if gyroy > 1 or gyroy < -1:
        pitch = -gyroy * 0.2





    D.dataPub.publish(String())
    """

