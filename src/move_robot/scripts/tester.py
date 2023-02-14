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
    global current_x, current_y, current_yaw, c

    p_controller_linear = 0.5
    p_controller_angular = 0.8

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

                rate = rospy.Rate(10)
                
                if (abs(current_yaw - angle_to_goal) > 0.05):

                    while not rospy.is_shutdown():

                        if (current_yaw < 0):
                            yaw = 6.28 - abs(current_yaw)

                        else:
                            yaw = current_yaw

                        if (angle_to_goal < 0):
                            goal_angle = 6.28 - abs(angle_to_goal)

                        else:
                            goal_angle = angle_to_goal

                        if (yaw < 3.14):
                            threshold = yaw + 3.14
                        else:
                            threshold = yaw - 3.14

                        if goal_angle > threshold:
                            angular_speed = -0.1
                        else:
                            angular_speed = 0.1

                        print("Angle to goal:", angle_to_goal)
                        print("Current yaw:", current_yaw)

                        print("diff:", abs(angle_to_goal) - abs(current_yaw))

                        if(abs(angle_to_goal - current_yaw) < 0.05):                            
                            speed.angular.z = 0.0
                            pub.publish(speed)
                            yaw = 0.00
                            goal_angle = 0.00
                            print("Turned")
                            break

                        else:
                            print("false")
                            speed.angular.z = angular_speed
                            speed.linear.x = 0.0
                            pub.publish(speed)

                        rate.sleep()
                

                speed.linear.x = linear_speed

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
    # path = [(32, 27), (33, 28), (34, 29), (35, 30), (36, 31), (37, 32), (38, 33), (39, 34), (40, 35), (41, 36), (42, 37), (42, 38), (42, 39), (42, 40), (42, 41), (42, 42), (42, 43), (42, 44), (42, 45), (42, 46), (42, 47), (42, 48), (42, 49), (41, 50), (41, 51), (41, 52), (41, 53), (41, 54), (41, 55), (41, 56), (41, 57), (41, 58), (41, 59), (42, 60),
        #   (43, 61), (44, 62), (45, 62), (46, 62), (47, 62), (48, 62), (49, 62), (50, 62), (51, 62), (52, 62), (53, 62), (54, 62), (55, 62), (56, 62), (57, 62), (58, 62), (59, 62), (60, 62), (61, 62), (62, 62), (63, 62), (64, 62), (65, 62), (66, 62), (67, 62), (68, 62), (69, 62), (70, 62), (71, 62), (72, 62), (73, 62), (74, 62), (75, 62), (76, 62)]

    # path = [(76, 62), (75, 61), (74, 60), (73, 59), (72, 58), (71, 57), (70, 56), (69, 55), (70, 54), (70, 53), (70, 52), (70, 51), (70, 50), (70, 49), (70, 48), (69, 47), (68, 46), (67, 45), (66, 44), (65, 43), (64, 42), (63, 41), (62, 40), (62, 39), (62, 38), (62, 37), (62, 36), (62, 35), (61, 34), (60, 33), (59, 32), (58, 31), (57, 30), (56, 29), (55, 28), (54, 27), (53, 27), (52, 27), (51, 27), (50, 27), (49, 27), (48, 27), (47, 27), (46, 27), (45, 27), (44, 27), (43, 27), (42, 27), (41, 27), (40, 27), (39, 27), (38, 27), (37, 27), (36, 27), (35, 27), (34, 27), (33, 27), (32, 27)]

    path = [(35, 30), (36, 31), (37, 32), (38, 33), (39, 34), (40, 35), (41, 36), (42, 37), (43, 37), (44, 36), (45, 35), (46, 35), (47, 35), (48, 35), (49, 35), (50, 35), (51, 35), (52, 36), (53, 37), (54, 38), (55, 39), (56, 40), (57, 41),
            (58, 42), (59, 43), (60, 44), (61, 45), (61, 46), (61, 47), (61, 48), (61, 49), (61, 50), (62, 51), (63, 52), (64, 53), (65, 54), (66, 55), (67, 56), (68, 57), (69, 58), (70, 59), (71, 60), (72, 60), (73, 60), (74, 60), (75, 60)]

    # path = [(75, 60), (74, 59), (73, 58), (72, 57), (71, 56), (70, 56), (69, 56), (68, 56), (67, 56), (66, 56), (65, 56), (64, 57), (63, 58), (62, 59), (61, 60), (60, 61), (59, 61), (58, 61), (57, 62),
            # (56, 62), (55, 62), (54, 62), (53, 62), (52, 62), (51, 62), (50, 62), (49, 62), (48, 62), (47, 62), (46, 62), (45, 62), (44, 62), (43, 62), (42, 61), (41, 60), (40, 59), (39, 58), (38, 57), (38, 56)]

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
