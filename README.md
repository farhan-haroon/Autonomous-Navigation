# Autonomous Navigation 
This is a project that implements Single-Source-Shortest-Path finding - **A-Star** algorithm on **Differential Drive Robots** using **ROS** - (Robot Operating System) and **Wheel Odometry** developed by **Mohd Farhan Haroon** at **Integral University, Lucknow.**. 

This repository is the software implementation of another project under development - **Autonomous Ground Cleaning Robot**. That project will utilise this Autonomous Navigation repository and will be built completely in-house at the **Integral Robotics Lab**.

The differential drive robot that we have used is the **Turtle Bot 3 - Waffle Pi** from **ROBOTIS** that runs ROS - **NOETIC**.
The steps to setup and run the **Turtle Bot 3** are given on the [official website](https://emanual.robotis.com/docs/en/platform/turtlebot3/quick-start/) of ROBOTIS.

## Pre-requisites:
* Differential Drive Robot (Turtle Bot 3 here) 
* Ubuntu 20.04 LTS - focal fossa
* ROS NOETIC on host PC
* Python - 2.7 or above

## Steps to run:
It is assumed that the robot is fully setup. 
Execute the following steps to implement Autonomous Navigation on your robot:

### SLAM: 
      
The first step is to generate a 2-D Map of the surroundings using the LIDAR and the SLAM (Simultaneous Localisation And Mapping) algorithm.

Execute the following commands to run SLAM and generate the Map:

1. Export the Turtle Bot 3 model to bring up basic packages
```
export TURTLEBOT3_MODEL=${TB3_MODEL}
```


2. Run the SLAM algorithm
```
roslaunch turtlebot3_slam turtlebot3_slam.launch
```
