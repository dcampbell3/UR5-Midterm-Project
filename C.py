import sys
import copy
import rospy
import moveit_commander
import moveit_msgs.msg
import geometry_msgs.msg
import math
from setup import *

def trace_C(scale, ee_step, jump_threshold): 

    # Perform geometric calculation for length of line segment for the given letter
    segment_len = scale / (2*math.cos(math.radians(45))+1)

    # Array to store the resulting waypoints
    waypoints = []

    wpose = move_group.get_current_pose().pose

    # Move 1 
    wpose.position.x += segment_len
    waypoints.append(copy.deepcopy(wpose))

    # Move 2 
    wpose.position.x += segment_len * math.cos(math.radians(45))
    wpose.position.z -= segment_len * math.cos(math.radians(45))
    waypoints.append(copy.deepcopy(wpose))

    # Move 3 
    wpose.position.z -= segment_len
    waypoints.append(copy.deepcopy(wpose))

    # Move 4 
    wpose.position.x -= segment_len * math.cos(math.radians(45))
    wpose.position.z -= segment_len * math.cos(math.radians(45))
    waypoints.append(copy.deepcopy(wpose))

    # Move 5
    wpose.position.x -= segment_len
    waypoints.append(copy.deepcopy(wpose))

    # Create and execute the Cartesian trajectory from the calculated waypoints
    (plan, fraction) = move_group.compute_cartesian_path(waypoints, ee_step, jump_threshold)
    move_group.execute(plan, wait=True)

    print("Traced C")
    return
