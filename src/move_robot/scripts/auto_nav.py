#!/usr/bin/env python3

import math
import rospy
from geometry_msgs.msg import Twist
from nav_msgs.msg import Odometry
from tf.transformations import euler_from_quaternion

current_x = current_y = current_yaw = None
c = 0


def callback_method(msg):
    global current_x, current_y, current_yaw
    current_x = msg.pose.pose.position.x

    current_y = msg.pose.pose.position.y
    quaternion = (msg.pose.pose.orientation.x, msg.pose.pose.orientation.y, msg.pose.pose.orientation.z,
                  msg.pose.pose.orientation.w)
    value = euler_from_quaternion(quaternion)
    current_yaw = value[2]


def mover(goal_x, goal_y):
    global current_x, current_y, c

    p_controller_linear = 0.8
    # p_controller_angular = 0.8
    rate = rospy.Rate(40)
    speed = Twist()

    while not rospy.is_shutdown():
        if current_x and current_y and current_yaw is not None:
            while not rospy.is_shutdown():

                dist = abs(math.sqrt(((goal_x - current_x) ** 2) +
                           ((goal_y - current_y) ** 2)))

                if (dist < 0.02):
                    c = c + 1
                    break

                linear_speed = dist * p_controller_linear

                # set upper limit of linear velocity
                linear_speed = min(linear_speed, 0.1)
                # set lower limit of linear velocity
                linear_speed = max(linear_speed, 0.06)

                angle_to_goal = math.atan2(
                    goal_y - current_y, goal_x - current_x)

                if (current_yaw < 0):
                    yaw = 6.28 - abs(current_yaw)

                else:
                    yaw = current_yaw

                if (angle_to_goal < 0):
                    angle_to_goal = 6.28 - abs(angle_to_goal)

                delta_heading = math.atan2(
                    math.sin(angle_to_goal - yaw), math.cos(angle_to_goal - yaw))


                if abs(angle_to_goal - yaw) > 0.02:
                    
                    # set upper limit of angular velocity
                    angular_speed = min(delta_heading, 0.15)
                    # set lower limit of angular velocity
                    angular_speed = max(delta_heading, -0.15)

                else:
                    angular_speed = 0.0

                if abs(angular_speed) > 0.05:
                    linear_speed = 0.0

                speed.linear.x = linear_speed
                speed.angular.z = angular_speed

                pub.publish(speed)
                rate.sleep()

            break

    speed.linear.x = 0.0
    speed.angular.z = 0.0

    if c > 0:
        pub.publish(speed)
        print("Done")
        c = 0

    else:
        rospy.signal_shutdown("kill")
        print("Keyboard interrupt!")


if __name__ == "__main__":

    rospy.init_node("mover")
    pub = rospy.Publisher('/cmd_vel', Twist, queue_size=10)
    rospy.Subscriber('/odom', Odometry, callback_method)

    cell_size = float(input("Enter the cell size: "))

    path = [(15, 18), (16, 19), (17, 20), (18, 21), (19, 21), (20, 21), (21, 21), (22, 21), (23, 21), (24, 21), (25, 21), (26, 21), (27, 21), (28, 21), (29, 21), (30, 22), (31, 23), (32, 24), (33, 25), (34, 26), (35, 27), (36, 28), (37, 29), (38, 29), (39, 29), (40, 29), (41, 29), (42, 29), (43, 29), (44, 29), (45, 29), (46, 29), (47, 29), (48, 29), (49, 29), (50, 29), (51, 29), (52, 29), (53, 30), (53, 31), (53, 32), (53, 33), (53, 34), (53, 35), (53, 36), (53, 37), (53, 38), (53, 39), (53, 40), (53, 41), (52, 42), (51, 43), (50, 44), (49, 45), (48, 46), (47, 46), (46, 46), (45, 46), (44, 46), (43, 46), (42, 46), (41, 46), (40, 46), (39, 46), (38, 46), (37, 47), (36, 48), (35, 48), (34, 48), (33, 48), (32, 48)]

    x_offset = int(input("Enter X offset: "))
    y_offset = int(input("Enter Y offset: "))

    print("X-offset =", x_offset)
    print("Y-offset =", y_offset)

    for node in path:
        x_goal = (node[0] - x_offset) * cell_size
        y_goal = (node[1] - y_offset) * cell_size
        print("Moving to", x_goal, y_goal)
        mover(x_goal, y_goal)

    print("Reached.")
