#!/usr/bin/env python3

import rospy
from geometry_msgs.msg import Twist
from std_msgs.msg import String
from newfile import path_planning
import time 


class mover(path_planning):

    def __init__(self):
        super().__init__()
        self.path = super().a_star()
        # dir1 = super().start_dir
        # dir2 = super().end_dir
        # print(path)
        # print(len(path))
        self.motion()
        
    def motion(self):
        pub = rospy.Publisher('cmd_vel', Twist, queue_size=10)
        rospy.init_node('mover', anonymous=True)
        # rate = rospy.Rate(10) # 10hz
        l = len(self.path)
        print("\nPlace the TurtleBot facing North\n")
        ok = input()

        
        while not rospy.is_shutdown():

            if self.start_dir == "S":
                print("turning 180")
            elif self.start_dir == "E":
                print("turning 90")
            elif self.start_dir == "W":
                print("turning 270")

            


            # for i in range (1, len):
            #     current = self.path[i]
            #     previous = self.path[i - 1]
            #     if (current[0] == previous[0] and current[1] == (previous[1] + 1)):




def main():
    obj = mover()

if __name__ == "__main__":
    main()
