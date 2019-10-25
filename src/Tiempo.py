import sys
import rospy, roslib

import time

from std_msgs.msg import String


from move_base_msgs.msg import MoveBaseActionGoal
from move_base_msgs.msg import MoveBaseActionResult 


start_time=0
class Tiempo:
	
	def __init__(self):	
			
		try:
				self.goal = rospy.Subscriber("/move_base/goal",MoveBaseActionGoal, self.callback)
				self.result = rospy.Subscriber("/move_base/result",MoveBaseActionResult, self.callback2)

		except:
			print("Error Subscriber")


	def callback(self,data):
		global start_time
		start_time=time.time()
	def callback2(self,data):
		global start_time
		print("Running time= {}".format(time.time()-start_time))	

			
def main(args):

	rospy.init_node('Tiempo', anonymous=True)
	rospy.loginfo("Time")
	
	ic = Tiempo()
	try:
		rospy.spin()
	except:
		pass

			
if __name__ == '__main__':

    main(sys.argv)
