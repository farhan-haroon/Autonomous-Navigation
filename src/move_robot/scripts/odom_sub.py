#!/usr/bin/env python3

# Importing the necessary libraries
import math
#import rospy
#from geometry_msgs.msg import Twist

# Declarations and initialisations
previous_dir = "NE"
current_dir = ""
path = [(41, 15), (40, 16), (39, 17), (38, 18), (37, 19), (36, 20), (35, 21), (35, 22), (35, 23), (35, 24), (35, 25), (35, 26), (34, 27), (33, 28), (32, 29), (31, 30), (30, 31), (29, 32), (28, 33), (27, 34), (26, 35), (25, 36), (24, 36), (23, 36), (22, 35), (21, 35), (20, 35), (19, 35), (18, 36), (17, 37), (16, 38), (15, 39), (15, 40), (15, 41), (15, 42), (15, 43), (15, 44), (15, 45)]
l = len(path)
a = b = 0

# ros node, publisher, and rate declarations
#pub = rospy.Publisher('/cmd_vel', Twist, queue_size = 10)
#rospy.init_node('move_to_location')
#rate = rospy.Rate(5)

# Function to move the robot straight
def move_by(val, t):
    print("\nMoving by ", val)
    print("For time: ", t,"\n")

# Function to turn the robot left
def turn_left(deg):
    print("\tTurning left by: ", deg, "\n")
    if deg == 45:
        print("\t& moving by 1 diagonal step\n")
    elif deg == 90:
        print ("\t& moving by 1 straight step\n")

# Function to turn the robot right 
def turn_right(deg):
    print("\tTurning right by: ", deg, "\n")
    if deg == 45:
        print("\t& moving by 1 diagonal step\n")
    elif deg == 90:
        print ("\t& moving by 1 straight step\n")

# Function to get the current direction by getting the previous direction
def get_direction(current, previous):

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


# main computation
for i in range (0, l - 1):

    # Getting the current and the previous nodes from the path
    previous = path[i]
    current = path[i + 1]

    # Getting the current directions by comparing with the previous directions
    current_dir = get_direction(current, previous)

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
        if current != path[len(path) - 1]:
            previous_dir = current_dir
            continue
        
    if ((current_dir != previous_dir) or current == path[len(path) - 1]):
        if a > 0:
            move_by(1, a)
        elif b > 0:
            move_by(math.sqrt(2), b)
        a = b = 0
        if current == path[len(path) - 1]:
            break

    print("Previous direction: ", previous_dir, "\n")
    print("Previous node: ", previous,"\n")
    print("Current direction: ", current_dir, "\n")
    print("Currrent node: ", current,"\n")


    # For straight previous directions

    if previous_dir == "N":

        if current_dir == "NE":
            turn_right(45)
            b = b + 1
        elif current_dir == "NW":
            turn_left(45)
            b = b + 1
        elif current_dir == "E":
            turn_right(90)
            a = a + 1
        elif current_dir == "W":
            turn_left(90)
            a = a + 1

        previous_dir = current_dir
        continue

    if previous_dir == "S":

        if current_dir == "SE":
            turn_left(45)
            b = b + 1
        elif current_dir == "SW":
            turn_right(45)
            b = b + 1
        elif current_dir == "E":
            turn_left(90)
            a = a + 1
        elif current_dir == "W":
            turn_right(90)
            a = a + 1

        previous_dir = current_dir
        continue

    if previous_dir == "E":

        if current_dir == "NE":
            turn_left(45)
            b = b + 1
        elif current_dir == "SE":
            turn_right(45)
            b = b + 1
        elif current_dir == "N":
            turn_left(90)
            a = a + 1
        elif current_dir == "S":
            turn_right(90)
            a = a + 1

        previous_dir = current_dir
        continue

    if previous_dir == "W":

        if current_dir == "NW":
            turn_right(45)
            b = b + 1
        elif current_dir == "SW":
            turn_left(45)
            b = b + 1
        elif current_dir == "N":
            turn_right(90)
            a = a + 1
        elif current_dir == "S":
            turn_left(90)
            a = a + 1

        previous_dir = current_dir
        continue

# For diagonal previous directions

    if previous_dir == "NE":

        if current_dir == "N":
            turn_left(45)
            b = b + 1
        elif current_dir == "NW":
            turn_left(90)
            a = a + 1
        elif current_dir == "E":
            turn_right(45)
            b = b + 1
        elif current_dir == "SE":
            turn_right(90)
            a = a + 1

        previous_dir = current_dir
        continue

    if previous_dir == "NW":

        if current_dir == "NE":
            turn_right(90)
            a = a + 1
        elif current_dir == "SW":
            turn_left(90)
            a = a + 1
        elif current_dir == "N":
            turn_right(45)
            b = b + 1
        elif current_dir == "W":
            turn_left(45)
            b = b + 1

        previous_dir = current_dir
        continue

    if previous_dir == "SE":

        if current_dir == "NE":
            turn_left(90)
            a = a + 1
        elif current_dir == "SW":
            turn_right(90)
            a = a + 1
        elif current_dir == "E":
            turn_left(45)
            b = b + 1
        elif current_dir == "S":
            turn_right(45)
            b = b + 1

        previous_dir = current_dir
        continue
    
    if previous_dir == "SW":

        if current_dir == "NW":
            turn_right(90)
            a = a + 1
        elif current_dir == "SE":
            turn_left(90)
            a = a + 1
        elif current_dir == "W":
            turn_right(45)
            b = b + 1
        elif current_dir == "S":
            turn_left(45)
            b = b + 1

        previous_dir = current_dir
        continue
    
    
