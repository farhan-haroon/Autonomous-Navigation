#!/usr/bin/env python3
from map_maker import map
import math

grid = map.nim

class Node():

    def __init__(self, parent_x, parent_y, pos_x, pos_y):
        
        self.parent_x = parent_x
        self.parent_y = parent_y
        self.pos_x = pos_x
        self.pos_y = pos_y


def is_movable(row, col):
    
    if (grid[row][col] == 1):
        return False
    else:
        return True


def is_destination(row, col, dest_r, dest_c):

    if (grid[row][col] == grid[dest_r][dest_c]):
        return True
    else:
        return False


def get_gcost(row, col, st_x, st_y):

    cost = math.sqrt()

def path_finder():

    open_list = []
    closed_list = []
    print("Enter Start Co-ordinates: ")
    st_x = input("Enter X: ")
    st_y = input("Enter Y: ")
    print("Enter End Co-rdinates: ")
    en_x = input("Enter X: ")
    en_y = input("Enter Y: ")
    start_node = Node(None, None, st_x, st_y)
    end_node = Node(None, None, en_x, en_y)
    #print("Start Node: ", start_node.pos_x, start_node.pos_y)
    #print("Start Node Parent: ", start_node.parent_x, start_node.parent_y)








def main():

    path_finder()

if __name__ == "__main__":
    
    main()
