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

    p_controller_linear = 0.5
    # p_controller_angular = 0.8

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
                linear_speed = min(linear_speed, 0.06)
                # set lower limit of linear velocity
                linear_speed = max(linear_speed, 0.04)

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

                # set upper limit of angular velocity
                angular_speed = min(delta_heading, 0.1)
                # set lower limit of angular velocity
                angular_speed = max(delta_heading, -0.1)

                if (angular_speed > 0.05 or angular_speed < -0.05):
                    linear_speed = 0.0

                speed.linear.x = linear_speed
                speed.angular.z = angular_speed

                pub.publish(speed)
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

    path = [(35, 30), (36, 31), (37, 32), (38, 33), (39, 34), (40, 35), (41, 36), (42, 36), (43, 35), (44, 34), (45, 34), (46, 34), (47, 34), (48, 34), (49, 34), (50, 34), (51, 34), (52, 34), (53, 35), (54, 36), (55, 37), (56, 38), (57, 39), (58, 40),
    (59, 41), (60, 42), (60, 43), (60, 44), (60, 45), (60, 46), (60, 47), (60, 48), (60, 49), (60, 50), (60, 51), (61, 52), (62, 53), (63, 54), (64, 55), (65, 56), (66, 57), (67, 58), (68, 59), (69, 60), (70, 60), (71, 60), (72, 60), (73, 60), (74, 60)]

    # path = [(74, 60), (73, 60), (72, 60), (71, 60), (70, 60), (69, 60), (68, 60), (67, 60), (66, 60), (65, 60), (64, 60), (63, 60), (62, 60), (61, 60), (60, 61), (59, 61), (58, 61), (57, 62), (56, 62), (55, 62),
    # (54, 62), (53, 62), (52, 62), (51, 62), (50, 62), (49, 62), (48, 62), (47, 62), (46, 62), (45, 62), (44, 62), (43, 62), (42, 61), (41, 60), (40, 60), (39, 60), (38, 60), (37, 60), (36, 60), (35, 60)]

    # path = [(35, 60), (36, 59), (37, 58), (38, 57), (39, 58), (40, 59), (41, 60), (42, 61), (43, 62), (44, 62), (45, 62), (46, 62), (47, 62), (48, 62), (49, 62), (50, 62), (51, 62), (52, 62), (53, 62), (54, 62),
            # (55, 62), (56, 62), (57, 62), (58, 61), (59, 61), (60, 61), (61, 60), (61, 59), (61, 58), (61, 57), (61, 56), (61, 55), (61, 54), (60, 53), (59, 52), (58, 51), (57, 50), (56, 49), (55, 48), (54, 48)]

    # x_offset = path[0][0]
    # y_offset = path[0][1]

    x_offset = 35
    y_offset = 30

    print("X-offset =", x_offset)
    print("Y-offset =", y_offset)

    for node in path:
        x_goal = (node[0] - x_offset) * cell_size
        y_goal = (node[1] - y_offset) * cell_size
        print("Moving to", x_goal, y_goal)
        mover(x_goal, y_goal)

    print("Reached.")
