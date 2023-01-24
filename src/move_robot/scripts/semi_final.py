#!/usr/bin/env python3

# Importing the necessary libraries
import math
import rospy
from geometry_msgs.msg import Twist
import time

class mover():

    def __init__(self, path,):

        rospy.init_node('robot_mover')
        self.pub = rospy.Publisher('/cmd_vel', Twist, queue_size = 10)
        rate = rospy.Rate(10) #Hz
        self.path = path

    # Function to move the robot straight
    def move_by(self, val, t):
        if (val == 1):
            dist = 0.045 * t
        else:
            dist = 0.045 * math.sqrt(2) * t
        
        moving_time = dist / 0.05
        end_time = rospy.get_time() + moving_time
        msg = Twist()

        print("\nMoving by ", dist, "m")
        print("For time: ", moving_time,"s")
        print("At velocity: 0.05 m/s")
        print("Times: ",t, "\n")

        while rospy.get_time() < end_time:
            msg.linear.x = 0.05
            self.pub.publish(msg)

        msg.linear.x = 0.0
        self.pub.publish(msg)
        time.sleep(2)


    # Function to turn the robot left
    def turn_left(self, deg):
        
        print("\tTurning left by: ", deg, "\n")
        
        if deg == 45:
            print("\t& moving by 1 diagonal step\n")

            # Rotating the robot by 45 degrees port

            msg = Twist()
            msg.angular.z = - 0.1
            msg.linear.x = 0.0
            now_time = rospy.get_time()
            
            while rospy.get_time() < now_time + 5:
                self.pub.publish(msg)

            # Set velocities for 1 diagonal movement

            msg.linear.x = 0.05
            msg.angular.z = 0.0
            time.sleep(2)
            now_time = rospy.get_time()

            # Move by 1 diagonal distance

            while rospy.get_time() < now_time + 1.26:
                self.pub.publish(msg)

            # Stop everything

            msg.linear.x = 0.0
            self.pub.publish(msg)

            print("Rotated by 45 degrees Port.")
            time.sleep(2)

        elif deg == 90:
            print ("\t& moving by 1 straight step\n")


    # Function to turn the robot right 
    def turn_right(self, deg):
        
        print("\tTurning right by: ", deg, "\n")
        
        if deg == 45:
            print("\t& moving by 1 diagonal step\n")

            # Rotating the robot by 45 degrees Starboard.
 
            msg = Twist()
            msg.linear.x = 0.0
            msg.angular.z = 0.1
            now_time = rospy.get_time()
            
            while rospy.get_time() < now_time + 5:
                self.pub.publish(msg)

            # Set velocities for 1 diagonal movement

            msg.linear.x = 0.05
            msg.angular.z = 0.0
            time.sleep(2)
            now_time = rospy.get_time()

            # Move by 1 diagonal distance

            while rospy.get_time() < now_time + 1.26:
                self.pub.publish(msg)

            # Stop everything
            
            msg.linear.x = 0.0
            self.pub.publish(msg)

            print("Rotated by 45 degrees Starboard.")
            time.sleep(2)

        elif deg == 90:
            print ("\t& moving by 1 straight step\n")


    # Function to get the current direction by getting the previous direction
    def get_direction(self, current, previous):

        if (current[0] == previous[0] and current[1] == previous[1] + 1):
            return ("E")
        elif (current[0] == previous[0] and current[1] == previous[1] - 1):
            return ("W")
        elif (current[0] == previous[0] + 1 and current[1] == previous[1]):
            return ("S")
        elif (current[0] == previous[0] - 1 and current[1] == previous[1]):
            return ("N")
        elif (current[0] == previous[0] - 1 and current[1] == previous[1] + 1):
            return ("NE")
        elif (current[0] == previous[0] + 1 and current[1] == previous[1] + 1):
            return ("SE")
        elif (current[0] == previous[0] - 1 and current[1] == previous[1] - 1):
            return ("NW")
        elif (current[0] == previous[0] + 1 and current[1] == previous[1] - 1):
            return ("SW")

    def robot_mover(self):
        
        previous_dir = "NE"
        current_dir = ""
        l = len(self.path)
        a = b = 0

        # main computation
        for i in range (0, l - 1):
            
            # Getting the current and the previous nodes from the path
            previous = self.path[i]
            current = self.path[i + 1]

            # Getting the current directions by comparing with the previous directions
            current_dir = self.get_direction(current, previous)

            # For same previous and current directions
            if current_dir == previous_dir:
                if current_dir in ("N", "S", "E", "W"):
                    a = a + 1
                elif current_dir in ("NE", "NW", "SE", "SW"):
                    b = b + 1
                print("Previous direction: ", previous_dir, "\n")
                print("Previous node: ", previous,"\n")
                print("Current direction: ", current_dir, "\n")
                print("Currrent node: ", current,"\n")
                if current != self.path[len(self.path) - 1]:
                    previous_dir = current_dir
                    continue

            if ((current_dir != previous_dir) or current == self.path[len(self.path) - 1]):
                if a > 0:
                    self.move_by(1, a)
                elif b > 0:
                    self.move_by(math.sqrt(2), b)
                a = b = 0
                if current == self.path[len(self.path) - 1]:
                    break

            print("Previous direction: ", previous_dir, "\n")
            print("Previous node: ", previous,"\n")
            print("Current direction: ", current_dir, "\n")
            print("Currrent node: ", current,"\n")

            # For straight previous directions

            if previous_dir == "N":

                if current_dir == "NE":
                    self.turn_right(45)
                    b = b + 1
                elif current_dir == "NW":
                    self.turn_left(45)
                    b = b + 1
                elif current_dir == "E":
                    self.turn_right(90)
                    a = a + 1
                elif current_dir == "W":
                    self.turn_left(90)
                    a = a + 1

                previous_dir = current_dir
                continue


            if previous_dir == "S":

                if current_dir == "SE":
                    self.turn_left(45)
                    b = b + 1
                elif current_dir == "SW":
                    self.turn_right(45)
                    b = b + 1
                elif current_dir == "E":
                    self.turn_left(90)
                    a = a + 1
                elif current_dir == "W":
                    self.turn_right(90)
                    a = a + 1

                previous_dir = current_dir
                continue

            if previous_dir == "E":

                if current_dir == "NE":
                    self.turn_left(45)
                    b = b + 1
                elif current_dir == "SE":
                    self.turn_right(45)
                    b = b + 1
                elif current_dir == "N":
                    self.turn_left(90)
                    a = a + 1
                elif current_dir == "S":
                    self.turn_right(90)
                    a = a + 1

                previous_dir = current_dir
                continue

            if previous_dir == "W":

                if current_dir == "NW":
                    self.turn_right(45)
                    b = b + 1
                elif current_dir == "SW":
                    self.turn_left(45)
                    b = b + 1
                elif current_dir == "N":
                    self.turn_right(90)
                    a = a + 1
                elif current_dir == "S":
                    self.turn_left(90)
                    a = a + 1

                previous_dir = current_dir
                continue

            # For diagonal previous directions

            if previous_dir == "NE":

                if current_dir == "N":
                    self.turn_left(45)
                    b = b + 1
                elif current_dir == "NW":
                    self.turn_left(90)
                    a = a + 1
                elif current_dir == "E":
                    self.turn_right(45)
                    b = b + 1
                elif current_dir == "SE":
                    self.turn_right(90)
                    a = a + 1

                previous_dir = current_dir
                continue

            if previous_dir == "NW":

                if current_dir == "NE":
                    self.turn_right(90)
                    a = a + 1
                elif current_dir == "SW":
                    self.turn_left(90)
                    a = a + 1
                elif current_dir == "N":
                    self.turn_right(45)
                    b = b + 1
                elif current_dir == "W":
                    self.turn_left(45)
                    b = b + 1

                previous_dir = current_dir
                continue

            if previous_dir == "SE":

                if current_dir == "NE":
                    self.turn_left(90)
                    a = a + 1
                elif current_dir == "SW":
                    self.turn_right(90)
                    a = a + 1
                elif current_dir == "E":
                    self.turn_left(45)
                    b = b + 1
                elif current_dir == "S":
                    self.turn_right(45)
                    b = b + 1

                previous_dir = current_dir
                continue

            if previous_dir == "SW":

                if current_dir == "NW":
                    self.turn_right(90)
                    a = a + 1
                elif current_dir == "SE":
                    self.turn_left(90)
                    a = a + 1
                elif current_dir == "W":
                    self.turn_right(45)
                    b = b + 1
                elif current_dir == "S":
                    self.turn_left(45)
                    b = b + 1

                previous_dir = current_dir
                continue


def main():
    way = [(41, 15), (40, 16), (39, 17), (38, 18), (37, 19), (36, 20), (35, 21), (35, 22), (35, 23), (35, 24), (35, 25), (35, 26), (34, 27), (33, 28), (32, 29), (31, 30), (30, 31), (29, 32), (28, 33), (27, 34), (26, 35), (25, 36), (24, 36), (23, 36), (22, 35), (21, 35), (20, 35), (19, 35), (18, 36), (17, 37), (16, 38), (15, 39), (15, 40), (15, 41), (15, 42), (15, 43), (15, 44), (15, 45)]
    obj = mover(way)
    obj.robot_mover()
    print("Destination reached.")

if __name__ == '__main__':
    main()
