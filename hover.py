
import roslib;roslib.load_manifest('crazyflie')
import rospy
import cflib
from std_msgs.msg import String
from crazyflie.msg import *
from cflib.crazyflie import Crazyflie

class Data: pass
D = Data()

def main():
    global D
    rospy.init_node("hover")
    rospy.Subscriber("cf_accData", AccelData, accelCall)	
    rospy.Subscriber("cf_stabData", StabData, stabCall)	
    rospy.Subscriber("cf_gyroData", GyroData, gyroCall)	
    rospy.Subscriber("cf_motorData", MotorData, motorCall)
    D.dataPub = rospy.Publisher("textdata", String)
    rospy.spin()
    
    
def accelCall(data):
    global D
    x = data.x
    y = data.y
    z = data.z
    print ("Accel (x, y, z): " + str(x) +","+ str(y) +","+ str(z))
    """
    if accz<-1:
        thrust= -accz*.2
        D.dataPub.publish(String("t" + str(thrust)))
    """

def stabCall(data):
    global D
    roll = data.roll
    pitch = data.pitch
    yaw = data.yaw
    print("Stab: (roll, pitch, yaw):" + str(roll) +","+ str(pitch) + "," + str(yaw))
    D.dataPub.publish(String("r" + str(roll)))
    D.dataPub.publish(String("p" + str(pitch)))
    D.dataPub.publish(String("y" + str(yaw)))
    
def gyroCall(data):
    global D
    x = data.x
    y = data.y
    z = data.z
    print ("Gyro (x, y, z): " + str(x) +","+ str(y) +","+ str(z))
    """
    if gyrox > 1 or gyrox < -1:
        roll = -gyrox * 0.2
    if gyroy > 1 or gyroy < -1:
        pitch = -gyroy * 0.2
    if gyroz > 1 or gyroz < -1:
        yaw = -gyroz * 0.2
    D.dataPub.publish(String("r" + str(roll)))
    D.dataPub.publish(String("p" + str(pitch)))
    D.dataPub.publish(String("y" + str(yaw)))
    """

def motorCall(data):
    global D
    m1 = data.m1
    m2 = data.m2
    m3 = data.m3
    m4 = data.m4
    print("Motors (1, 2, 3, 4): "+str(m1)+","+str(m2)+","+str(m3)+","+str(m4))
    
if __name__ == "__main__":
    main()    
