#!/bin/python3

import os
from collections import deque


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def arr_to_root(tree_list):
    root = TreeNode(int(tree_list[0]))
    index = 1
    queue = deque([root])

    while queue:
        node = queue.popleft()
        if index >= len(tree_list): break
        if tree_list[index] != 'null':
            node.left = TreeNode(int(tree_list[index]))
            queue.append(node.left)
        index += 1

        if index >= len(tree_list): break
        if tree_list[index] != 'null':
            node.right = TreeNode(int(tree_list[index]))
            queue.append(node.right)
        index += 1
    return root


def solution(root):
    def is_within_range(node, min_val, max_val):
        if not node:
            return False

        if min_val <= node.val <= max_val:
            return True

        if node.val > max_val:
            return is_within_range(node.left, min_val, max_val)

        if node.val < min_val:
            return is_within_range(node.right, min_val, max_val)

        return False

    return is_within_range(root, -3, 3)


if __name__ == '__main__':
    tree_list_count = int(input().strip())
    tree_list = []

    for _ in range(tree_list_count):
        tree_list_item = input()
        tree_list.append(tree_list_item)

    root = arr_to_root(tree_list)
    result = solution(root)

    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    fptr.write(str(1 if result else 0) + '\n')
    fptr.close()
