#!/usr/bin/env python3
import rospy
from nav_msgs.msg import Odometry

def listener():
    rospy.init_node('odom_reader')
    rospy.Subscriber('/odom', Odometry, callback)
    rospy.spin()

def callback(msg):
    rospy.loginfo(rospy.get_caller_id() + "I heard %s", msg.pose.pose.x)

if __name__ == '__main__':
    try:
        listener()
    except rospy.ROSInterruptException():
        pass