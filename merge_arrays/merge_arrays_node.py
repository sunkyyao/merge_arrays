#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from std_msgs.msg import Int32MultiArray

class MergeArraysNode(Node):

    def __init__(self):
        super().__init__('merge_arrays_node')
        self.subscription1 = self.create_subscription(
            Int32MultiArray,
            '/input/array1',
            self.array1_callback,
            10
        )
        self.subscription2 = self.create_subscription(
            Int32MultiArray,
            '/input/array2',
            self.array2_callback,
            10
        )
        self.publisher = self.create_publisher(
            Int32MultiArray,
            '/output/array',
            10
        )
        self.array1 = []
        self.array2 = []

    def array1_callback(self, msg):
        self.array1 = msg.data
        self.merge_and_publish()

    def array2_callback(self, msg):
        self.array2 = msg.data
        self.merge_and_publish()

    def merge_and_publish(self):
        merged_array = sorted(self.array1 + self.array2)
        msg = Int32MultiArray(data=merged_array)
        self.publisher.publish(msg)
        self.get_logger().info('Merged and published the sorted array.')

def main(args=None):
    rclpy.init(args=args)
    node = MergeArraysNode()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
