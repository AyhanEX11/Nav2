#!/usr/bin/env python3
import rclpy
from nav2_simple_commander.robot_navigator import BasicNavigator
from geometry_msgs.msg import PoseStamped
import tf_transformations


def main():
    rclpy.init()
    nav = BasicNavigator()

    q_x, q_y,q_z, q_w = tf_transformations.quaternion_from_euler(0.0, 0.0, 0.0)
    initial_pose = PoseStamped()
    initial_pose.header.frame_id = 'map'
    initial_pose.header.stamp = nav.get_clock().now().to_msg()
    initial_pose.pose.position.x = 0.0
    initial_pose.pose.position.y = 0.0
    initial_pose.pose.position.z = 0.0
    initial_pose.pose.orientation.x = 0.0
    initial_pose.pose.orientation.y = 0.0
    initial_pose.pose.orientation.z = 0.0
    initial_pose.pose.orientation.w = 0.0
    nav.setInitialPose(initial_pose)

    nav.waitUntilNav2Active()

    q_x, q_y, q_z, q_w = tf_transformations.quaternion_from_euler(0.0, 0.0, 1.57)
    initial_pose = PoseStamped()
    initial_pose.header.frame_id = 'map'
    initial_pose.header.stamp = nav.get_clock().now().to_msg()
    initial_pose.pose.position.x = 2.5
    initial_pose.pose.position.y = 1.0
    initial_pose.pose.position.z = 0.0
    initial_pose.pose.orientation.x = q_x
    initial_pose.pose.orientation.y = q_y
    initial_pose.pose.orientation.z = q_z
    initial_pose.pose.orientation.w = q_w
    nav.goToPose(goal_pose)

    while not nav.isTaskComplete():
        feedback = nav.getFeedback()

    print(nav.getResult())

    

    rclpy.shutdown()

if __name__ == '__main__':
    main()