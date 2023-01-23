#!/usr/bin/env python3
import rospy
from geometry_msgs.msg import Twist

rospy.init_node('robot_turner')
pub = rospy.Publisher('/cmd_vel', Twist, queue_size=10)
rate = rospy.Rate(5)
now_time = rospy.get_time()
end_time = now_time + 7.8
msg = Twist()
msg.angular.z = 0.1

while rospy.get_time() < end_time:
    print(rospy.get_time())
    pub.publish(msg)
    print("Publishing")

msg.angular.z = 0.0
pub.publish(msg)
print("Rotated.")
print("Published for ", (rospy.get_time() - now_time))
