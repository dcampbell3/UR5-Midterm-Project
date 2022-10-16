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

SCALE = 0.10
EE_STEP = 0.001
JUMP_THRESHOLD = 100
# !!NOTE!! run scale with 0.25 

return_to_start()

time.sleep(3)

trace_D(SCALE, EE_STEP, JUMP_THRESHOLD)

time.sleep(3)

return_to_start() 

time.sleep(3)

trace_R(SCALE, EE_STEP, JUMP_THRESHOLD)

time.sleep(3)

return_to_start()

trace_C(SCALE, EE_STEP, JUMP_THRESHOLD)

time.sleep(3) 

return_to_start()



 