#!/usr/bin/env python
import rospy
import numpy as np
import cv2
from sensor_msgs.msg import Image
from cv_bridge import CvBridge, CvBridgeError

bridge = CvBridge() #Instantiate CvBridge

def callback(data):
    try:   
        cv2_img = bridge.imgmsg_to_cv2(data, "bgr8")
    except CvBridgeError as e:
        print(e)
    else:
        cv2.imshow("Python Received data", cv2_img)
        cv2.waitKey(10)


def listener():

    rospy.init_node('python_img_sub', anonymous=True)

    rospy.Subscriber("image_topic", Image, callback, queue_size = 1)

    rospy.spin()

if __name__ == '__main__':
    listener()
