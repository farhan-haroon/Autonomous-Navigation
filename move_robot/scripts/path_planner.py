#!/usr/bin/env python3

from map_maker import map
import heapq

# Function to determine the validity of the cell

def walkable(grid, x, y, robot_radius):
    for i in range(-robot_radius, robot_radius+1):
        for j in range(-robot_radius, robot_radius+1):
            if not (0 <= x + i < len(grid) and 0 <= y + j < len(grid[0])):
                return False
            if grid[x + i][y + j] == 0:
                return False
    return True

# Function to find the path

def find_path(grid, start, goal, robot_radius):
    # Create a priority queue to store potential path squares
    heap = [(0, start)]
    # Create a dictionary to store the cost of each square
    cost = {start: 0}
    # Create a dictionary to store the parent of each square
    parent = {start: None}
    # Create a set to store visited squares
    visited = set()

    while heap:
        # Pop the square with the lowest cost from the heap
        current = heapq.heappop(heap)[1]

        # If the current square is the goal square, return the path
        if current == goal:
            path = []
            while current != start:
                path.append(current)
                current = parent[current]
            path.append(start)
            return path[::-1]

        # Mark the current square as visited
        visited.add(current)

        # Check the squares adjacent to the current square
        for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1), (1, -1), (-1, 1), (-1, -1), (1, 1)]:
            x, y = current
            next_square = (x + dx, y + dy)
            # If the next square is outside the grid or is an obstacle, skip it
            if not walkable(grid, x + dx, y + dy, robot_radius):
                continue
            # If the next square has been visited, skip it
            if next_square in visited:
                continue
            # Calculate the cost of the next square
            next_cost = cost[current] + 1
            # If the next square is not in the heap or has a higher cost, update it
            if next_square not in cost or next_cost < cost[next_square]:
                cost[next_square] = next_cost
                priority = next_cost + (abs(goal[0] - x - dx) + abs(goal[1] - y - dy))
                heapq.heappush(heap, (priority, next_square))
                parent[next_square] = current

    # If no path was found, return None
    return None


grid = map.nim

# Start and goal coordinates and Robot radius for obstacle clearance

print("Enter Start Co-ordinates: ")
st_x = int(input("Enter X: "))
st_y = int(input("Enter Y: "))
start = (st_x, st_y)

print("Enter End Co-ordinates: ")
en_x = int(input("Enter X: "))
en_y = int(input("Enter Y: "))
goal = (en_x, en_y)

ROBOT_RADIUS = int(input("Robot Radius: "))

if __name__ == "__main__":
    path = find_path(grid, start, goal, ROBOT_RADIUS)
    print(path)
    planned_grid = grid

    for point in path:
        planned_grid[point[0], point[1]] = "0"

    for i in range (0, 70):
        for j in range (0, 70):
            print(planned_grid[i, j], end = "")
        print()
