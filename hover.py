
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
    D.dataPub = rospy.Publisher("cf_textcmd", String)
    rospy.spin()
    
    
def accelCall(data):
    global D
    x = data.x
    y = data.y
    z = data.z
    print ("Accel (x, y, z): " + str(x) +","+ str(y) +","+ str(z))
    
    if z>.08:
        thrust= int(z*30000)
        D.dataPub.publish(String("t " + str(thrust)))
    

def stabCall(data):
    global D
    D.roll = data.roll
    D.pitch = data.pitch
    D.yaw = data.yaw
    print("Stab: (roll, pitch, yaw):" + str(D.roll) +","+ str(D.pitch) + "," + str(D.yaw))
    D.dataPub.publish(String("r " + str(D.roll)))
    D.dataPub.publish(String("p " + str(D.pitch)))
    D.dataPub.publish(String("y " + str(D.yaw)))
    
def gyroCall(data):
    global D
    
    x = data.x
    y = data.y
    z = data.z
    print ("Gyro (x, y, z): " + str(x) +","+ str(y) +","+ str(z))
    
    if x > 1 or x < -1:
        D.roll = -x * 0.2
    if y > 1 or y < -1:
        D.pitch = -y * 0.2
    if z > 1 or z < -1:
        D.yaw = -z * 0.2
    D.dataPub.publish(String("r " + str(D.roll)))
    D.dataPub.publish(String("p " + str(D.pitch)))
    D.dataPub.publish(String("y " + str(D.yaw)))
    

def motorCall(data):
    global D
    m1 = data.m1
    m2 = data.m2
    m3 = data.m3
    m4 = data.m4
    print("Motors (1, 2, 3, 4): "+str(m1)+","+str(m2)+","+str(m3)+","+str(m4))
    
if __name__ == "__main__":
    main()    
