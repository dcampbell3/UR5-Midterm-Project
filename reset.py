from setup import * 

# P1 = [0, -61, 99, 140, 0, -178]
# points_list = [P1]  

# joint_goal = move_group.get_current_joint_values()

# for point in points_list: 
#     joint_goal = [math.radians(p) for p in point]

# move_group.go(joint_goal, wait=True)
# move_group.stop()
def return_to_start():
    waypoints = []
    wpose = move_group.get_current_pose()

    # final goal 

    wpose.pose.position.x = 0.5119164436695298
    wpose.pose.position.y =0.19130372208443258
    wpose.pose.position.z = 0.19130372208443258
    wpose.pose.orientation.x = 0.707210484455942
    wpose.pose.orientation.y =0.7070030569705926
    wpose.pose.orientation.z = 6.376270144183684e-05
    wpose.pose.orientation.w =6.35936043025721e-05
    waypoints.append(copy.deepcopy(wpose))

    (plan, fraction) = move_group.compute_cartesian_path(waypoints, 0.01, 0.0) 
    move_group.execute(plan, wait=True)

    return

print(move_group.get_current_pose())
