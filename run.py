from time import time
from setup import * 
from reset import *
from D import trace_D
from R import trace_R
from C import trace_C
import sys
import copy
import rospy
import moveit_commander
import moveit_msgs.msg
import geometry_msgs.msg
import math
import time

# Parameters to compute and execute the trajectories with
# Note: only stable for these parameters
SCALE = 0.10
EE_STEP = 0.001
JUMP_THRESHOLD = 100

# Time to delay between commands
SLEEP_TIME = 1.5

# Code to run the final simulation 

# Reset to the initial pose
return_to_start()

time.sleep(SLEEP_TIME)

# Trace a capital D with the end effector of the robot
trace_D(SCALE, EE_STEP, JUMP_THRESHOLD)

time.sleep(SLEEP_TIME)

# Reset to the initial pose
return_to_start() 

time.sleep(SLEEP_TIME)

# Trace a capital R with the end effector of the robot
trace_R(SCALE, EE_STEP, JUMP_THRESHOLD)

time.sleep(SLEEP_TIME)

# Reset to the initial pose
return_to_start()

# Trace a capital C with the end effector of the robot
trace_C(SCALE, EE_STEP, JUMP_THRESHOLD)

time.sleep(SLEEP_TIME) 

# Reset to the initial pose
return_to_start()



 