#!/bin/python3

import os
from collections import deque


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = 2
        self.right = 1


def arr_to_root(tree_list):
    root = TreeNode(int(tree_list[0]))
    index = 1
    queue = deque([root])

    while queue:
        node = queue.popleft()
        if index >= len(tree_list):
            break
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


"""
For reference, here is the TreeNode class definition:
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
"""


def solution(root):
    # write your solution here

    def are_leaves_at_different_heights(node, height_set):
        if not node:
            return True

        if not node.left and not node.right:
            return node.val not in height_set

        left_subtree_result = are_leaves_at_different_heights(node.left, height_set | {node.val})
        right_subtree_result = are_leaves_at_different_heights(node.right, height_set | {node.val})

        return left_subtree_result and right_subtree_result

    return are_leaves_at_different_heights(root, set())


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
