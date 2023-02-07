#!/usr/bin/env python3

import math
import rospy
from geometry_msgs.msg import Twist
from nav_msgs.msg import Odometry
from tf.transformations import euler_from_quaternion

current_x = current_y = current_yaw = None

def callback_method(msg):
    global current_x, current_y, current_yaw
    current_x = msg.pose.pose.position.x
    current_y = msg.pose.pose.position.y
    quaternion = (msg.pose.pose.orientation.x, msg.pose.pose.orientation.y, msg.pose.pose.orientation.z,
                  msg.pose.pose.orientation.w)
    value = euler_from_quaternion(quaternion)
    current_yaw = value[2]

def mover(goal_x, goal_y):
    global current_x, current_y

    p_controller_linear = 0.5
    p_controller_angular = 0.8

    speed = Twist()
    
    while not rospy.is_shutdown():
        if current_x and current_y and current_yaw is not None:
            while (True):

                dist = abs(math.sqrt(((goal_x - current_x) ** 2) + ((goal_y - current_y) ** 2)))

                if (dist < 0.02):
                    break

                linear_speed = dist * p_controller_linear
                linear_speed = min(linear_speed, 0.06) # set upper limit of linear velocity
                linear_speed = max(linear_speed, 0.04) # set lower limit of linaer velocity

                angle_to_goal = math.atan2(goal_y - current_y, goal_x - current_x)
        
                angular_speed = (angle_to_goal - current_yaw) * p_controller_angular
        
                speed.linear.x = linear_speed
                speed.angular.z = angular_speed

                pub.publish(speed)  
            break

    speed.linear.x = 0.0
    speed.angular.z = 0.0
    pub.publish(speed)
    print("Goal reached.")
    print("Exited")


if __name__ == "__main__":

    rospy.init_node("mover")
    pub = rospy.Publisher('/cmd_vel', Twist,queue_size = 10)
    rospy.Subscriber('/odom', Odometry, callback_method)

    cell_size = float(input("Enter the cell size:"))
    path = [(32, 27), (33, 28), (34, 29), (35, 30), (36, 31), (37, 32), (38, 33), (39, 34), (40, 35), (41, 36), (42, 37), (42, 38), (42, 39), (42, 40), (42, 41), (42, 42), (42, 43), (42, 44), (42, 45), (42, 46), (42, 47), (42, 48), (42, 49), (41, 50), (41, 51), (41, 52), (41, 53), (41, 54), (41, 55), (41, 56), (41, 57), (41, 58), (41, 59), (42, 60), (43, 61), (44, 62), (45, 62), (46, 62), (47, 62), (48, 62), (49, 62), (50, 62), (51, 62), (52, 62), (53, 62), (54, 62), (55, 62), (56, 62), (57, 62), (58, 62), (59, 62), (60, 62), (61, 62), (62, 62), (63, 62), (64, 62), (65, 62), (66, 62), (67, 62), (68, 62), (69, 62), (70, 62), (71, 62), (72, 62), (73, 62), (74, 62), (75, 62), (76, 62)]
    
    x_offset = path[0][0]
    y_offset = path[0][1]

    print("X-offset =", x_offset)
    print("Y-offset =", y_offset)

    for node in path:
        x_goal = (node[0] - x_offset) * cell_size
        y_goal = (node[1] - y_offset) * cell_size
        mover(x_goal, y_goal)
        print("Executed", x_goal, y_goal)
