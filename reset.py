from setup import * 

joint_goal = move_group.get_current_joint_values()
joint_goal = [0.0004425776370799994, 0.012882975802745555, -9.476934568475315e-05, 0.0006768708517865818, -2.4944091894241183e-05, 2.9997848168150654e-05]

print(move_group.get_current_pose())
move_group.go(joint_goal, wait=True)
move_group.stop()
print(joint_goal)