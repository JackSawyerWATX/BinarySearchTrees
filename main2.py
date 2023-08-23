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