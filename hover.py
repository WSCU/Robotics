
import roslib
import rospy
import cflib
from std_msgs.msg import String
from cflib.crazyflie import Crazyflie

class Data: pass
    D = Data()

def main():
    rospy.Subscriber("cf_accData", AccelData, accCall)	
    rospy.Subscriber("cf_stabData", StabData, hoverCall)	
    rospy.Subscriber("cf_gyroData", GyroData, hoverCall)	
    rospy.Subscriber("cf_motorData", MotorData, hoverCall)
    
    
def accelCall(data):
    global D
    x = data.x
    y = data.y
    z = data.z
    print ("Received message: " + x +","+ y +","+ z)
    if accz<-1:
        thrust= -accz*.2
        D.dataPub.publish(String(t thrust))



def stabCall(data):
    global D
    roll = data.roll
    pitch = data.pitch
    yaw = data.yaw
    print("Received message:" + roll +","+ pitch + "," + yaw)
    D.dataPub.publish(String(r roll))
    D.dataPub.publish(String(p pitch))
    D.dataPub.publish(String(y yaw))
    
def gyro(data):
    global D
    x = data.x
    y = data.y
    z = data.z
    print ("Received message: " + x +","+ y +","+ z)
    if gyrox > 1 or gyrox < -1:
        roll = -gyrox * 0.2
    if gyroy > 1 or gyroy < -1:
        pitch = -gyroy * 0.2
    if gyroz > 1 or gyroz < -1:
        yaw = -gyroz * 0.2
    D.dataPub.publish(String(r roll))
    D.dataPub.publish(String(p pitch))
    D.dataPub.publish(String(y yaw))

