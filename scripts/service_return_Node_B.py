#! /usr/bin/env python

import rospy
from assignment_2_2023.srv import Return, ReturnResponse
from assignment_2_2023.msg import PlanningActionGoal
#from geometry_msgs.msg import Point

class goal:
	def __init__(self):
		self.targ_x = rospy.get_param('des_pos_x')
		self.targ_y = rospy.get_param('des_pos_y')
		rospy.Service('service_goal',Return,self.callposition)
		rospy.Subscriber('/reaching_goal/goal', PlanningActionGoal, self.goal)
	def goal(self,msg):
	 	self.targ_x=msg.goal.target_pose.pose.position.x
	 	self.targ_y=msg.goal.target_pose.pose.position.y
	def callposition(self,req):
		return ReturnResponse (self.targ_x, self.targ_y)


def main ():
	rospy.init_node ('service_return_Node_B')
	goal()
	rospy.spin ()
	
	
if __name__ == '__main__':
	main()
