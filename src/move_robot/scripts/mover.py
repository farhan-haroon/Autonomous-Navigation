#!/usr/bin/env python3

import rospy
from geometry_msgs.msg import Twist
from std_msgs.msg import String
from path_generator import path_planning
import time 


class mover(path_planning):

    def __init__(self):
        super().__init__()
        self.path = super().a_star()
        self.dir1 = self.start_dir
        self.dir2 = self.end_dir
        # print(path)
        # print(len(path))
        self.publisher = rospy.Publisher('cmd_vel', Twist, queue_size=10)
        rospy.init_node('mover', anonymous=True)
        self.motion()
        
    def motion(self):

        cmd = Twist()
        
        print("\nPlace the TurtleBot facing North\n")
        ok = input()

        if self.start_dir == "S":
           print("Turning 180")

        elif self.start_dir == "E":
            print("Turning 90")
            
        elif self.start_dir == "W":
            print("Turning 270")

        l = len(self.path)
        old_dir = self.dir1

        while not rospy.is_shutdown():

            for i in range (1, len):
                current = self.path[i]
                previous = self.path[i - 1]
                
                if (current[0] == previous[0] and current[1] == (previous[1] + 1)):
                    new_dir = "E"
                elif (current[0] == previous[0] and current[1] == (previous[1] - 1)):
                    new_dir = "W"
                elif (current[0] == (previous[0] + 1) and current[1] == previous[1]):
                    new_dir = "S"
                elif(current[0] == (previous[0] - 1) and current[1] == previous[1]):
                    new_dir = "N"

                if new_dir == old_dir:
                    cmd.linear.x = 1.0
                    self.publish(cmd, 2, False)       

                elif (new_dir == "E"):

                    if old_dir == "N":
                        cmd.angular.z = 1.0
                        self.publish(cmd, 2, True)

                    elif old_dir == "S":
                        cmd.angular







    def publish(self, amp, turn):
        
        obj = Twist()

        if (turn == True):
            self.publisher.publish(amp)
            time.sleep(2)
            


def main():
    obj = mover()

if __name__ == "__main__":
    main()
