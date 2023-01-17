#!/usr/bin/env python3

import rospy
from geometry_msgs.msg import Twist

def mover():
    pub = rospy.Publisher('cmd_vel', Twist, queue_size = 10)
    rospy.init_node('mover_node')
    rate = rospy.Rate(1) #Hz
    msg = Twist()
    msg.linear.x = 0.1
    while not rospy.is_shutdown():
        pub.publish(msg)
        rate.sleep()

if __name__ == "__main__":
    try:
        mover()
    except ROSInterruptException:
        pass
