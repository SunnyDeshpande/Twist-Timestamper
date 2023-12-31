#!/usr/bin/env python
import rospy
from geometry_msgs.msg import Twist, TwistStamped

import time


def callback(cmdVelocity):

    baseVelocity = TwistStamped()

    baseVelocity.twist = cmdVelocity

    now = rospy.get_rostime()
    baseVelocity.header.stamp.secs = now.secs
    baseVelocity.header.stamp.nsecs = now.nsecs

    baseVelocityPub = rospy.Publisher('/RosAria/cmd_vel_stamped', TwistStamped, queue_size=1)
    baseVelocityPub.publish(baseVelocity)


def cmd_vel_listener():

    rospy.Subscriber("/cmd_vel", Twist, callback)

    rospy.spin()

if __name__ == '__main__':
    rospy.init_node('twist_timestamper', anonymous=True)
    cmd_vel_listener()

