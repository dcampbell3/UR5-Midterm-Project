from setup import * 

# P1 = [0, -61, 99, 140, 0, -178]
# points_list = [P1]  

# joint_goal = move_group.get_current_joint_values()

# for point in points_list: 
#     joint_goal = [math.radians(p) for p in point]

# move_group.go(joint_goal, wait=True)
# move_group.stop()
def return_to_start():
    P1 = [0, -61, 99, 140, 0, -178]

    points_list = [P1]  

    joint_goal = move_group.get_current_joint_values()

    for point in points_list: 
        joint_goal = [math.radians(p) for p in point]
        move_group.go(joint_goal, wait=True)
        move_group.stop()

    return

print(move_group.get_current_pose())
