# Definition for a binary tree node.
from collections import deque
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        max_sum, ans, level = float("-inf"), 0, 0

        que = deque()
        que.append(root)

        while que:
            level += 1
            sum_at_current_level = 0
            for _ in range(len(que)):
                node = que.popleft()
                sum_at_current_level += node.val

                if node.left:
                    que.append(node.left)
                if node.right:
                    que.append(node.right)

            if max_sum < sum_at_current_level:
                max_sum, ans = sum_at_current_level, level

        return ans


class Solution:
    def dfs(
        self, node: Optional[TreeNode], level: int, sum_of_nodes_at_level: List[int]
    ) -> None:
        if node is None:
            return None

        if len(sum_of_nodes_at_level) == level:
            sum_of_nodes_at_level.append(node.val)
        else:
            sum_of_nodes_at_level[level] += node.val

        self.dfs(node.left, level + 1, sum_of_nodes_at_level)
        self.dfs(node.right, level + 1, sum_of_nodes_at_level)

    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        sum_of_nodes_at_level = []
        self.dfs(root, 0, sum_of_nodes_at_level)

        max_sum = float("-inf")
        ans = 0

        for i in range(len(sum_of_nodes_at_level)):
            if max_sum < sum_of_nodes_at_level[i]:
                max_sum = sum_of_nodes_at_level[i]
                ans = i + 1

        return ans
