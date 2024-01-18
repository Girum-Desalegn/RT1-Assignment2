#! /usr/bin/env python

import rospy
import math
import time
from assignment_2_2023.srv import Average, AverageResponse
from assignment_2_2023.msg import Vel_pos
from assignment_2_2023.msg import PlanningActionGoal


class Position_speed:
	def __init__(self):
     
		self.frequency = rospy.get_param('frequency')
		
		# Time of the last print
		self.old_time = 0
		self.distance = rospy.get_param('des_pos_x')
		self.ave_vel = rospy.get_param('des_pos_y')
		self.targ_x=0
		self.targ_y=0
		rospy.Service('service_position',Average,self.call_pos_vel)
		rospy.Subscriber('/velxz_posxy', Vel_pos, self.callback)
		rospy.Subscriber('/reaching_goal/goal',PlanningActionGoal,self.target)
  
	def target(self,msg):
		self.targ_x=msg.goal.target_pose.pose.position.x
		self.targ_y=msg.goal.target_pose.pose.position.y
	def callback(self,msg):
		   
		current_time = time.time() * 1000
		
		if current_time - self.old_time > 1000 / self.frequency:
						
			self.distance = math.sqrt((self.targ_x - msg.pos_x)**2 + (self.targ_y - msg.pos_y)**2)
			self.ave_vel = math.sqrt(msg.vel_x**2 + msg.vel_z**2)
			self.old_time = current_time 
	def call_pos_vel(self,req):
		return AverageResponse (self.distance, self.ave_vel)


def main ():
	rospy.init_node ('service_subscriber_Node_C')
	Position_speed()
	rospy.spin ()
	
	
if __name__ == '__main__':
	main()
