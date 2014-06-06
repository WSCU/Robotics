import roslib
import rospy
from std_msgs.msg import String

def main():
    rospy.init_node("cf_textcmd")
    pub = rospy.Publisher("cf_textcmd", String)
    
    while rospy.is_shutdown() == False:
        message = raw_input(":: ")
        pub.publish(String(message))
        if message == 'h':
            break
    return

if __name__ == "__main__":
    main()
