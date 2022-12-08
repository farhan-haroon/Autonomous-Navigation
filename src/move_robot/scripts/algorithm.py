from map_maker import map
import numpy as np
import math
import time

class path_planning():
    
    def __init__(self, st_x, st_y, st_node, en_x, en_y, en_node, st_dir, en_dir):

        self.start_x = st_x
        self.start_y = st_y
        self.start_node = st_node
        self.end_x = en_x
        self.end_y = en_y
        self.end_node = en_node
        self.start_dir = st_dir
        self.end_dir = en_dir
        self.grid = map.nim
        path = self.a_star()
    
    
    def mid_pos(self, x, y, dir): #function to check if the coordinates are in middle of the lane 

        real_x = x
        real_y = y
        err_x1 = 0
        err_x2 = 0
        err_y1 = 0
        err_y2 = 0
        lane_width1 = 0
        lane_width2 = 0

        if dir == "E" or dir == "W":

            while (True):

                if(self.grid[x, y] == 0):
                    err_x1 = x
                    break

                else:
                    x-=1

            x = real_x
            
            up_diff = abs(real_x - err_x1)
            
            while(True):

                if(self.grid[x, y] == 0):
                    err_x2 = x
                    break
                else:
                    x+=1

            x = real_x

            lo_diff = abs(real_x - err_x2)

            lane_width1 = up_diff + lo_diff
            mid_x = (x - up_diff) + (lane_width1 // 2)

            return (mid_x, y)

        else:

            while(True):

                if(self.grid[x, y] == 0):
                    err_y1 = y
                    break
                else:
                    y-=1

            y = real_y
            left_diff = abs(real_y - err_y1)
            print()

            while(True):

                if(self.grid[x, y] == 0):
                    err_y2 = y
                    break
                else:
                    y+=1

            y = real_y

            right_diff = abs(real_y - err_y2)

            lane_width2 = left_diff + right_diff
            mid_y = (y - left_diff) + (lane_width2 // 2)

            return (x, mid_y)

    def heuristic(self, x, y):

        dist = math.sqrt(((self.end_x - x)**2) + ((self.end_y - y)**2))
        return dist

    def g_cost(self, x, y):

        cost = math.sqrt(((self.start_x - x)**2) + ((self.start_y - y)**2))
        return cost

    def path_finder(self, x, y):

        up_dist = 0
        down_dist = 0
        left_dist = 0
        right_dist = 0
        real_x = x
        real_y = y

        while (True):

            if(self.grid[x, y] == 0):
                up_dist = abs(x - real_x)
                break

            else:
                x-=1

        x = real_x

        while (True):

            if(self.grid[x, y] == 0):
                down_dist = abs(x - real_x)
                break

            else:
                x+=1

        x = real_x

        while (True):

            if(self.grid[x, y] == 0):
                left_dist = abs(y - real_y)
                break

            else:
                y-=1

        y = real_y

        while (True):

            if(self.grid[x, y] == 0):
                right_dist = abs(y - real_y)
                break

            else:
                y+=1

        y = real_y

        list = [up_dist, down_dist, left_dist, right_dist]
        lar = max(list)

        if(lar == up_dist):
            print("N")

        elif(lar == down_dist):
            print("S")

        elif(lar == left_dist):
            print("W")

        else:
            print("E")


    def a_star(self):

        open_list = []
        closed_list = []
        order = []
        apt = tuple()

        open_list.append(self.start_node)
        # print(open_list[0][1])

        while (True):

            last = len(open_list)
            
            up_neighbour = ((open_list[last - 1][0] - 1), open_list[last - 1][1])
            # print("Up Neighbour: ", up_neighbour)
            down_neighbour = ((open_list[last - 1][0] +1), open_list[last - 1][1])
            # print("Down Neighbour: ", down_neighbour)
            left_neighbour = (open_list[last - 1][0], (open_list[last - 1][1] - 1))
            # print("Left Neighbour: ", left_neighbour)
            right_neighbour = (open_list[last - 1][0], (open_list[last - 1][1] + 1))
            # print("Right Neighbour: ", right_neighbour)
            
            # print() #leave a line

            up_f_cost = self.heuristic(up_neighbour[0], up_neighbour[1]) #+ self.g_cost(up_neighbour[0], up_neighbour[1])
            # print("Heuristic: ", self.heuristic(up_neighbour[0], up_neighbour[1]))
            # print("G Cost: ", self.g_cost(up_neighbour[0], up_neighbour[1]))
            # print("Up Neighbour F Cost: ", up_f_cost)
            # print()

            down_f_cost = self.heuristic(down_neighbour[0], down_neighbour[1]) #+ self.g_cost(down_neighbour[0], down_neighbour[1])
            # print("Heuristic: ", self.heuristic(down_neighbour[0], down_neighbour[1]))
            # print("G Cost: ", self.g_cost(down_neighbour[0], down_neighbour[1]))
            # print("Down Neighbour F Cost: ", down_f_cost)
            # print()

            left_f_cost = self.heuristic(left_neighbour[0], left_neighbour[1]) #+ self.g_cost(left_neighbour[0], left_neighbour[1])
            # print("Heuristic: ", self.heuristic(left_neighbour[0], left_neighbour[1]))
            # print("G Cost: ", self.g_cost(left_neighbour[0], left_neighbour[1]))
            # print("Left Neighbour F Cost: ", left_f_cost)
            # print()
            
            right_f_cost = self.heuristic(right_neighbour[0], right_neighbour[1]) #+ self.g_cost(right_neighbour[0], right_neighbour[1])
            # print("Heuristic: ", self.heuristic(right_neighbour[0], right_neighbour[1]))
            # print("G Cost: ", self.g_cost(right_neighbour[0], right_neighbour[1]))
            # print("Right Neighbour F Cost: ", right_f_cost)
            # print()

            # min_f_cost = min(up_f_cost, down_f_cost, left_f_cost, right_f_cost)
            # print("Lowest F Cost: ", min_f_cost)

            # print() #leave a line

            order.clear()
            sml = 9999999999

            if(up_f_cost < sml and up_neighbour not in closed_list):
                sml = up_f_cost
            order.append(up_f_cost)

            if(down_f_cost < sml and down_neighbour not in closed_list):
                sml = down_f_cost
            order.append(down_f_cost)
            
            if(left_f_cost < sml and left_neighbour not in closed_list):
                sml = left_f_cost
            order.append(left_f_cost)
            
            if(right_f_cost < sml and right_neighbour not in closed_list):
                sml = right_f_cost
            order.append(right_f_cost)


            order.sort()
            # print("Order: ", order)


            for i in order:
                if (i == up_f_cost and self.is_way(up_neighbour, "N") and up_neighbour not in closed_list):
                    apt = up_neighbour
                    # print("Apt: ", apt)
                    break

                elif (i == down_f_cost and self.is_way(down_neighbour, "S") and down_neighbour not in closed_list):
                    apt = down_neighbour
                    # print("Apt: ", apt)
                    break

                elif (i == left_f_cost and self.is_way(left_neighbour, "W") and left_neighbour not in closed_list):
                    apt = left_neighbour
                    # print("Apt: ", apt)
                    break

                elif (i == right_f_cost and self.is_way(right_neighbour, "E") and right_neighbour not in closed_list):
                    apt = right_neighbour
                    # print("Apt: ", apt)
                    break


            if (apt == up_neighbour):
                open_list.append(up_neighbour)
                # print("Choosing Up Neighbour")

            elif(apt == down_neighbour):
                open_list.append(down_neighbour)
                # print("Choosing Down Neighbour")

            elif(apt == left_neighbour):
                open_list.append(left_neighbour)
                # print("Choosing Left Neighbour")

            elif(apt == right_neighbour):
                open_list.append(right_neighbour)
                # print("Choosing Right Neighbour")
            
            

            closed_list.append(up_neighbour)
            closed_list.append(down_neighbour)
            closed_list.append(left_neighbour)
            closed_list.append(right_neighbour)
            closed_list.append(open_list[last - 1])

            last2 = len(open_list)
            # print("Open List: ", open_list)

            # print("Closed List: ", closed_list)

            # time.sleep(0.5)
            # print() #leave a line
            # break
            
            if(open_list[last2 - 1] == self.end_node):
                break

        print (open_list)
        print("Final List: ", open_list)

        
    
    
    
    def is_way(self, pos, dir):
        
        # print("Pos ", pos)
        # print("X: ", pos[0])
        # print("Y: ", pos[1])
        if (dir == "N"):
            # print("Checking for North")
            for i in range (1, 5):
                # print("loop ",i)
                # print(self.grid[(pos[0] - i), pos[1]])
                if (self.grid[(pos[0] - i), pos[1]] == 0):
                    # print("False")
                    return False
                # else:
                    # print("Not True")

        elif (dir == "S"):
            # print("Checking for South")
            for i in range (1, 5):
                if (self.grid[(pos[0] + i), pos[1]] == 0):
                    # print("False")
                    return False

        elif (dir == "E"):
            # print("Checking for East")
            for i in range (1, 5):
                if (self.grid[pos[0], (pos[1] + i)] == 0):
                    # print("False")
                    return False

        elif (dir == "W"):
            # print("Checking for West")
            for i in range (1,5):
                if(self.grid[pos[0], (pos[1] - i)] == 0):
                    # print("False")
                    return False

        # print(pos, " has way in "+dir)
        return True




def main():

    print("Start Co-ordinates: ")
    x1 = int(input("Start X: "))
    y1 = int(input("Start Y: "))
    start_node = (x1, y1)
    print("End Co-ordinates: ")
    x2 = int(input("End X: "))
    y2 = int(input("End Y: "))
    end_node = (x2, y2)
    dir1 = input("Start Direction: ")
    dir2 = input("End Direction: ")

    obj = path_planning(x1, y1, start_node, x2, y2, end_node, dir1, dir2)

    #For testing:
    # obj.mid_pos(x1, y1, dir1)
    # obj.path_finder(x1, y1)
    # obj.is_way((38,27), "N")

    

if __name__ == "__main__":
    
    main()
