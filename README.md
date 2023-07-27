# Autonomous Navigation using Wheel Odometry
This is a project that implements Single-Source-Shortest-Path finding - `A-Star` algorithm on `Differential Drive Robots` using `ROS` - (Robot Operating System) and `Wheel Odometry` developed by `Mohd Farhan Haroon` at `Integral University, Lucknow`. 

This repository is the software implementation of another project under development - `Autonomous Ground Cleaning Robot`. That project will utilise this Autonomous Navigation repository and will be built completely in-house at the `Integral Robotics Lab`.

The differential drive robot that we have used is the `Turtle Bot 3 - Waffle Pi` from `ROBOTIS` that runs ROS - `NOETIC`.
The steps to setup and run the **Turtle Bot 3** are given on the [official website](https://emanual.robotis.com/docs/en/platform/turtlebot3/quick-start/) of ROBOTIS.

## Pre-requisites:
* Differential Drive Robot (Turtle Bot 3 here) 
* Ubuntu 20.04 LTS - focal fossa (or earlier till 16.04 LTS)
* ROS NOETIC on host PC
* Python - 2.7 or above

## Steps to run:
It is assumed that the robot is fully setup. 

[**Very important:** While calibration, place the Turtle Bot in such a way that the maze or the area to be covered lies in the positive quadrant of it's Odometry cartesian plane.]

Execute the following steps to implement Autonomous Navigation on your robot:

### SLAM: 
      
The first step is to generate a 2-D Map of the surroundings using the LIDAR and the SLAM (Simultaneous Localisation And Mapping) algorithm.

Execute the following commands to run SLAM and generate the Map:

1. Export the Turtle Bot 3 model and run the SLAM algorithm
```
$ export TURTLEBOT3_MODEL=${TB3_MODEL}
$ roslaunch turtlebot3_slam turtlebot3_slam.launch
```

2. Open a new trminal and launch the Tele-operation node
```
$ export TURTLEBOT3_MODEL=${TB3_MODEL}
$ roslaunch turtlebot3_teleop turtlebot3_teleop_key.launch
```

Explore the area with the Tele-operation node to generate a complete map of the surroundings.

The map is visualised using RViz that is launched with the SLAM node.

3. Save the Map
```
$ rosrun map_server map_saver -f ~/map
```
THe destination folder to save the map can be defined after _-f_ (/home/${username} in this case).

### Matrix Generation:

The `map_maker.py` converts the Map image from `.png` to a 2-D matrix of 0s and 1s. 0s represent the movalble white area of the map and 1s represent the obstacles in the map.

1. Change directory to the `catkin_ws` and clone this repository in the `src` folder.
```
$ cd ~/catkin_ws/src/
$ git clone https://github.com/farhan-haroon/Autonomous-Navigation.git
$ cd .. && catkin make
```

2. Move the `map.png` from where it is saved (/home/${username} in this case) to the package folder in the `~/catkin_ws/src/move_robot/scripts` and delete the previous map image present.

3. Open the package folder in a code editor (like VSCode) and load the `map_maker.py` file.

4. Paste the path of the map image in the line 6 and adjust the dimensions of the map matrix according to yourself in the line 12 (rows should be equal to column)

5. Uncomment the last nested `for` loop and run the program.

6. The output printed is the map matrix in 0s and 1s in the defined dimensions. Copy the matrix and paste it in a separate text file for referencing co-ordinates.

### Path Planning:

The `path_planner.py` implements the `A-Star` algorithm on the matrix and finds the shortest path between the given start and the end points.

1. Open the `path_planner.py` in the editor and run the program.

2. Enter the Start and the End co-ordinates by referring the saved matrix from the text file. [**Note:** The Start coordinates should be the current position of the robot in the real world.]

3. Also enter the size of the robot to give it wall clearance.

4. The output is the same matrix of the given dimensions with the path shown as the number `7` and the path is also printed as a list of tuples.

5. Copy the list from the terminal.

### Navigation:

1. Open the `auto_nav.py` in the editor and paste the path copied from `path_planner.py` in the line 108.

2. Open a new terminal and execute the following commands [It is assumed that the bringup is launched and the robot is placed and calibrated as mentioned earlier].
```
$ cd ~/catkin_ws/src/ && catkin make
$ source ~/.bashrc
$ rosrun move_robot auto_nav.py
```

3. Enter the size of 1 cell. [Size of 1 cell can be calculated by measuring the length of 1 side of the real maze and dividing it by the number of cells it is represented by in the matrix].

4. Enter the X and the Y offsets. [X and Y offsets are the X and the Y coordinates of the first tuple in the path. It is provided to subtract it from the path tuples X and Y coordinates so as to make the path as (0, 0), (1, 1), (2, 2) and so on].

For eg.: if the path is like (15, 30), (16, 31), (17, 31) ... , then the X offset will be 15 and Y offset will be 30.

5. Reversing the path provided will make the robot retrace it's steps back to the Start position.

## Contact 

For any bug reports or issues, please contact me at `farhanhar[at]student[dot]iul[dot]ac[dot]in`

`Mohd Farhan Haroon`

`Integral University, Lucknow.`
