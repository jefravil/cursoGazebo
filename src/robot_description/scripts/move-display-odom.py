#! /usr/bin/env python

import rospy
from geometry_msgs.msg import Twist
from nav_msgs.msg import Odometry
import random

speed = .2
turn = 1
last_msg = None


def cambiomov(pub,linearX=0.0,angularZ=0.0):
            twist = Twist()
            twist.linear.x = linearX*speed
            twist.linear.y = 0
            twist.linear.z = 0
            twist.angular.x = 0
            twist.angular.y = 0
            twist.angular.z = angularZ*turn
            pub.publish(twist)
  
def callback(msg):
    global last_msg # Esto indica que queremos usar la variable global `last_msg`
    last_msg = msg # Ahora estamos modificando la variable global
def process_data():
    global last_msg
    if last_msg is not None:
        rospy.loginfo("Posicion X %.2f"%last_msg.pose.pose.position.x)
        rospy.loginfo("Posicion Y %.2f"% last_msg.pose.pose.position.y)

if __name__=="__main__":

    try:
        rospy.init_node('cmdvel_topic_publisher')
        pub = rospy.Publisher('/cmd_vel', Twist, queue_size=1)
        sub = rospy.Subscriber('/odom', Odometry, callback)
        count=0
        rate = rospy.Rate(2)
        while not rospy.is_shutdown() and count!=100:
            x = random.choice([-1, 1 , 0])
            th = random.choice([-1, 1, 0])
            cambiomov(pub,x,th)
            process_data()
            count+=1   
            rate.sleep()

    except rospy.ROSInterruptException:
        pass
    finally:
        for _ in range(10):
            cambiomov(pub, 0, 0)
            rospy.loginfo("Robot detenido.")