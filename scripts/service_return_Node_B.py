#! /usr/bin/env python
import rospy
# from std_srvs.srv import *
from assignment_2_2023.srv import Return, ReturnResponse

#when called the server does this
def callback(req):
	targ_x = rospy.get_param('des_pos_x')
	targ_y = rospy.get_param('des_pos_y')
	return ReturnResponse(targ_x, targ_y)



def main ():
	rospy.init_node ('last_target')
	serv = rospy.Service ('get_last_target', Return, callback)
	rospy.spin ()
	
		
		
if __name__ == '__main__':
	main()
