#!/usr/bin/env python3
from map_maker import map
import time
import numpy as np


class Node():

    def __init__(self, parent, x, y):
        
        self.parent = parent
        self.x = x
        self.y = y

def path_finder():

    grid = map.nim
    open_list = []
    closed_list = []
    print("Enter Start Co-ordinates: ")
    st_x = input("Enter X: ")
    st_y = input("Enter Y: ")
    print("Enter End Co-rdinates: ")
    en_x = input("Enter X: ")
    en_y = input("Enter Y: ")
    start_node = Node(None, st_x, st_y)
    end_node = Node(None, en_x, en_y)
    print("Start Node: ", start_node.x, start_node.y)
    print("Start Node Parent: ", start_node.parent)

def main():

    path_finder()

if __name__ == "__main__":
    
    main()