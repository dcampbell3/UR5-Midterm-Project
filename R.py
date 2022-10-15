import sys
import copy
import rospy
import moveit_commander
import moveit_msgs.msg
import geometry_msgs.msg
import math
from setup import *

def trace_R(scale): 
    x_len = scale / (2*(2*math.cos(math.radians(45))+1))

    waypoints = []
    wpose = move_group.get_current_pose().pose

    # Move 1
    wpose.position.z -= scale
    waypoints.append(copy.deepcopy(wpose))

    # Move 2 
    wpose.position.z += scale
    waypoints.append(copy.deepcopy(wpose))

    # Move 3 
    wpose.position.x -= x_len
    waypoints.append(copy.deepcopy(wpose))

    # Move 4
    wpose.position.x -= x_len * math.cos(math.radians(45))
    wpose.position.z -= x_len * math.cos(math.radians(45))
    waypoints.append(copy.deepcopy(wpose))

    # Move 5 
    wpose.position.z -= x_len
    waypoints.append(copy.deepcopy(wpose))

    # Move 6
    wpose.position.x += x_len * math.cos(math.radians(45))
    wpose.position.z -= x_len * math.cos(math.radians(45))
    waypoints.append(copy.deepcopy(wpose))

    # Move 7 
    wpose.position.x -= (x_len + x_len * math.cos(math.radians(45)))
    wpose.position.z -= scale/2
    return 