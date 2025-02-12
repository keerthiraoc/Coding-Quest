# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def findLeft(self, root: TreeNode) -> TreeNode:
        while root.left:
            root = root.left
        return root

    def helper(self, root: TreeNode) -> TreeNode:
        if not root.left:
            return root.right

        if not root.right:
            return root.left

        last_left = self.findLeft(root.right)
        last_left.left = root.left

        return root.right

    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return None

        if root.val == key:
            return self.helper(root)

        temp = root
        while temp:
            if temp.val > key:
                if temp.left and temp.left.val == key:
                    temp.left = self.helper(temp.left)
                    break
                else:
                    temp = temp.left
            else:
                if temp.right and temp.right.val == key:
                    temp.right = self.helper(temp.right)
                    break
                else:
                    temp = temp.right

        return root
