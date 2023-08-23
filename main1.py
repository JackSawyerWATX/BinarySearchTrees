#!/bin/python3

import os
from collections import deque


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def arr_to_root(tree_list1):
    root1 = TreeNode(int(tree_list1[0]))
    index = 1
    queue = deque([root1])

    while queue:
        node = queue.popleft()
        if index >= len(tree_list1):
            break
        if tree_list1[index] != 'null':
            node.left = TreeNode(int(tree_list1[index]))
            queue.append(node.left)
        index += 1

        if index >= len(tree_list1): break
        if tree_list1[index] != 'null':
            node.right = TreeNode(int(tree_list1[index]))
            queue.append(node.right)
        index += 1
    return root1


"""
For reference, here is the TreeNode class definition:
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
"""


def solution(roots):
    # write your solution here

    if not roots:
        return 0

    count = 0

    if (roots.left or roots.right) or (not roots.left and roots.right):
        count += 1

    count += solution(roots.left)
    count += solution(roots.right)

    return count


if __name__ == '__main__':

    tree_list_count = int(input().strip())
    tree_list = []

    for _ in range(tree_list_count):
        tree_list_item = input()
        tree_list.append(tree_list_item)

    root = arr_to_root(tree_list)
    result = solution(root)

    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    fptr.write(str(result) + '\n')
    fptr.close()
