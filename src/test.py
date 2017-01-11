#! /usr/bin/env python

# BEGIN ALL

#! /usr/bin/env python

import rospy

import actionlib
from voice.msg import TextAction, TextGoal, TextResult

rospy.init_node('text_action_client')
# BEGIN PART_1

client = actionlib.SimpleActionClient('text_to_speech', TextAction)
client.wait_for_server()
# END PART_1

# BEGIN PART_2
goal = TextGoal()
goal.text = "Hello World"
client.send_goal(goal)
# END PART_2
# BEGIN PART_3
client.wait_for_result()
print client.get_result().response
# END PART_3
# END ALL
