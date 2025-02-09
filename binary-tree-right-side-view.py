# Definition for a binary tree node.
from typing import List, Optional
from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        que = deque()
        if root:
            que.append(root)
        res = []
        while que:
            size, val = len(que), 0
            for _ in range(size):
                node = que.popleft()
                val = node.val  # store last value in each level
                if node.left:
                    que.append(node.left)
                if node.right:
                    que.append(node.right)
            res.append(val)
        return res
