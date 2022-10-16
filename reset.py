from setup import * 

# Function to set the angles to an initial position
def return_to_start():

    # Set of angles to go to 
    P1 = [0, -61, 99, 140, 0, -178]

    joint_goal = move_group.get_current_joint_values()

    # Convert angles from degrees to radians
    joint_goal = [math.radians(p) for p in P1]

    # Go to angles specified
    move_group.go(joint_goal, wait=True)
    move_group.stop()

    print("Returned to Start")

    return

return_to_start()