import sys
import copy
import rospy
import moveit_commander
import moveit_msgs.msg
import geometry_msgs.msg
import math
from setup import *

def trace_D(scale):
    '''
    d = 0.5 / (2*math.cos(math.radians(45))+1)

    waypoints = []
    wpose = move_group.get_current_pose().pose

    #Move 2: 
    wpose.position.z -= 0.5
    waypoints.append(copy.deepcopy(wpose))

    #Move 3: 
    wpose.position.x -= d
    waypoints.append(copy.deepcopy(wpose))

    #Move 4: 
    wpose.position.x -= d * math.cos(math.radians(45))
    wpose.position.z += d * math.cos(math.radians(45))
    waypoints.append(copy.deepcopy(wpose))

    #Move 5: 
    wpose.position.z += d
    waypoints.append(copy.deepcopy(wpose))

    #Move 6: 
    wpose.position.x += d * math.cos(math.radians(45))
    wpose.position.z += d * math.cos(math.radians(45))
    waypoints.append(copy.deepcopy(wpose))

    #Move 7: 
    wpose.position.x += d
    waypoints.append(copy.deepcopy(wpose))

    (plan, fraction) = move_group.compute_cartesian_path(waypoints, 0.01, 0.0) 
    move_group.execute(plan, wait=True)
    '''

    x_len = scale / (2*math.cos(math.radians(45))+1)

    waypoints = []
    wpose = move_group.get_current_pose().pose

    #Move 2: 
    wpose.position.z -= scale
    waypoints.append(copy.deepcopy(wpose))

    #Move 3: 
    wpose.position.x -= x_len
    waypoints.append(copy.deepcopy(wpose))

    #Move 4: 
    wpose.position.x -= x_len * math.cos(math.radians(45))
    wpose.position.z += x_len * math.cos(math.radians(45))
    waypoints.append(copy.deepcopy(wpose))

    #Move 5: 
    wpose.position.z += x_len
    waypoints.append(copy.deepcopy(wpose))

    #Move 6: 
    wpose.position.x += x_len * math.cos(math.radians(45))
    wpose.position.z += x_len * math.cos(math.radians(45))
    waypoints.append(copy.deepcopy(wpose))

    #Move 7: 
    wpose.position.x += x_len
    waypoints.append(copy.deepcopy(wpose))

    (plan, fraction) = move_group.compute_cartesian_path(waypoints, 0.01, 0.0) 
    move_group.execute(plan, wait=True)
    return
