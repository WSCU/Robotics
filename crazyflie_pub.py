import roslib
import rospy
from std_msgs.msg import String

def main():
    rospy.init_node("textdata")
    pub = rospy.Publisher("textdata", String)
    
    while rospy.is_shutdown() == False:
        message = raw_input(":: ")
        pub.publish(String(message))
        if message == 'q':
            break
    return

if __name__ == "__main__":
    main()
