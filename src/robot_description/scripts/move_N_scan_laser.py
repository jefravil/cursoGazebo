#! /usr/bin/env python

import rospy
from geometry_msgs.msg import Twist
from nav_msgs.msg import Odometry
from sensor_msgs.msg import LaserScan
import random

speed = .2
turn = 1
last_msg = None
last_msg_laser = None

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
        rospy.logwarn("Posicion X %.2f"%last_msg.pose.pose.position.x)
        rospy.logwarn("Posicion Y %.2f"% last_msg.pose.pose.position.y)
        

def callbacklaser(msg):
    global last_msg_laser # Esto indica que queremos usar la variable global `last_msg`
    last_msg_laser = msg # Ahora estamos modificando la variable global
def process_dataLaser():
    global last_msg_laser
    if last_msg_laser is not None:
        min_range = min(last_msg_laser.ranges)
        rospy.loginfo(f"La distancia minima es: {min_range}")

if __name__=="__main__":

    try:
        rospy.init_node('cmdvel_topic_publisher')
        pubVel = rospy.Publisher('/cmd_vel', Twist, queue_size=1)
        subOdom = rospy.Subscriber('/odom', Odometry, callback)
        subOdom = rospy.Subscriber('/laser/scan', LaserScan, callbacklaser)
        count=0
        rate = rospy.Rate(2)
        while not rospy.is_shutdown() and count!=100:
            x = random.choice([-1, 1 , 0])
            th = random.choice([-1, 1, 0])
            cambiomov(pubVel,x,th)
            process_data()
            process_dataLaser()
            count+=1   
            rate.sleep()

    except rospy.ROSInterruptException:
        pass
    finally:
        for _ in range(10):
            cambiomov(pubVel, 0, 0)
            rospy.loginfo("Robot detenido.")