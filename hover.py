import roslib;roslib.load_manifest('crazyflie')
import rospy
import cflib
from std_msgs.msg import String
from crazyflie.msg import *
from cflib.crazyflie import Crazyflie
import csv
import time
class Data: pass

D = Data()
D.thrust = 45000
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
def main():
    global D
    rospy.init_node("hover")
    D.dataPub = rospy.Publisher("cf_textcmd", String)
    rospy.Subscriber("cf_accData", AccelData, accelCall)	
    rospy.Subscriber("cf_stabData", StabData, stabCall)	
    rospy.Subscriber("cf_gyroData", GyroData, gyroCall)	
    rospy.Subscriber("cf_motorData", MotorData, motorCall)
    rospy.Subscriber("cf_textcmd", String,textCall )
    rospy.spin()
    
    
def accelCall(data):
    global D
    x = data.x
    y = data.y
    z = data.z
    D.time = time.time()
    if D.lastZ is not None and D.alTime is not None:
        D.deltaTime = D.time - D.alTime
        
        #D.deltaZ += z + D.lastZ * D.deltaTime
        D.vel = D.lastZ + z * D.deltaTime
        writer = csv.writer(open("veldata.csv", "ab"), dialect = 'excel')
        writer.writerow([D.vel])
        D.dax = D.lax + x * D.deltaTime
        D.day = D.lay + y * D.deltaTime
        if D.vel<1:
            D.thrust= int(D.thrust*1.15)
            D.dataPub.publish(String("t " + str(D.thrust)))
        elif D.vel>1:
            D.thrust= int (D.thrust * 0.94) 
            D.dataPub.publish(String("t " + str(D.thrust)))
        else:
            D.dataPub.publish(String("t " + str(D.thrust)))
        #print("accel: %f %f" % (D.dax, D.day))
        #print (repr(D.dax) + " " + repr(D.day))
    #writer = csv.writer(open("acceldata.csv" , "ab"), dialect = 'excel')
    #row = [x, y, z]
    #writer.writerow(row)
    if not D.gyroCorrection:
        if D.lax is not None and D.lay is not None and D.alTime is not None:

            print "Accel (x, y, z): " + str(x) +","+ str(y) +","+ str(z) + " " + str(D.deltaTime)
            if D.dax < 0:
                D.pitch = 6
            elif D.dax > 0:
                D.pitch = -6
            
            if D.day < 0:
                D.roll = 6
            elif D.day > 0:
                D.roll = -6

            D.dataPub.publish(String("r " + str(D.roll)))
            D.dataPub.publish(String("p " + str(D.pitch)))
            D.lax = x
            D.lay = y
    D.lastZ = z
    D.alTime = D.time
    D.gyroCorrection = False

def stabCall(data):
    global D
    #print("Stab: (roll, pitch, yaw):" + str(D.roll) +","+ str(D.pitch) + "," + str(D.yaw))

def gyroCall(data):
    global D
    D.gyroCorrection = True
    x = data.x
    y = data.y
    z = data.z
    pitch = 0
    roll = 0
    #print ("Gyro (x, y, z): " + str(x) +","+ str(y) +","+ str(z))
    D.time = time.time()
    if D.lgx is not None and D.lgy is not None and D.lgz is not None and D.glTime is not None:
        D.deltaTime = D.time - D.glTime
        D.dgx = D.lgx + x * D.deltaTime
        D.dgy = D.lgy + y * D.deltaTime
        D.dgz = D.lgz + z * D.deltaTime
        print ("%d %d %d" % (D.dgx, D.dgy, D.dgz))
    else:
        D.dgx = x
        D.dgy = y
        D.dgz = z
    if D.dgx > 0:
        roll = D.dgy * -.1
    elif D.dgx < 0:
        roll = abs(D.dgy * .1)
    if D.dgy > 0:
        pitch = D.dgy * -.1
    elif D.dgy < 0:
        pitch = abs(D.dgy * .1)
  
    D.dataPub.publish(String("r " + str(roll)))
    D.dataPub.publish(String("p " + str(pitch)))
    #D.dataPub.publish(String("y " + str(D.yaw)))
    D.lgx = x
    D.lgy = y
    D.lgz = z
    D.glTime = D.time
 

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
    
if __name__ == "__main__":
    main()    
