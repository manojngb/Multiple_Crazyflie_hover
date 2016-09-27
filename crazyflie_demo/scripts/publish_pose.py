#!/usr/bin/env python

import rospy
import tf
from geometry_msgs.msg import PoseStamped
from time import time
import math

if __name__ == '__main__':
    rospy.init_node('publish_pose', anonymous=True)
    worldFrame = rospy.get_param("~worldFrame", "/world")
    name = rospy.get_param("~name")
    r = rospy.get_param("~rate")
    x = rospy.get_param("~x")
    y = rospy.get_param("~y")
    z = rospy.get_param("~z")
    count = 0;
    rate = rospy.Rate(r)

    msg = PoseStamped()
    msg.header.seq = 0
    msg.header.stamp = rospy.Time.now()
    Start_timestamp =  time()
    msg.header.frame_id = worldFrame
    msg.pose.position.x = x
    msg.pose.position.y = y
    msg.pose.position.z = z
    quaternion = tf.transformations.quaternion_from_euler(0, 0, 0)
    msg.pose.orientation.x = quaternion[0]
    msg.pose.orientation.y = quaternion[1]
    msg.pose.orientation.z = quaternion[2]
    msg.pose.orientation.w = quaternion[3]

    pub = rospy.Publisher(name, PoseStamped, queue_size=1)

    while not rospy.is_shutdown():
        if (time() - Start_timestamp < 20):
            msg.header.seq += 1
            msg.header.stamp = rospy.Time.now()
            x = rospy.get_param("~x")
            y = rospy.get_param("~y")
            z = rospy.get_param("~z")
            msg.pose.position.x = x
            msg.pose.position.y = y
            msg.pose.position.z = z
            pub.publish(msg)
            ##print "constant"
            rate.sleep()
        else:
            msg.header.seq += 1
            msg.header.stamp = rospy.Time.now()
            x = rospy.get_param("~x")
            y = rospy.get_param("~y")
            z = rospy.get_param("~z")
            t = 2*3.14*(float(count)/r)*(1/4.0)
            msg.pose.position.x = float(0.15*math.cos(t))
            msg.pose.position.y = float(0.1*math.sin(t))
            ##msg.pose.position.y = y
            msg.pose.position.z = z
            pub.publish(msg)
            if (count <= 16*r):
                count = count + 1
            else:
                count = 0
            ##print "circle %d " % count
            """print msg.pose.position.x
            print msg.pose.position.y"""
            rate.sleep()