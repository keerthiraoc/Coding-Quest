from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class FindElements:
    def __init__(self, root: Optional[TreeNode]):
        self.seen = set()
        self.dfs(root, 0)

    def find(self, target: int) -> bool:
        return target in self.seen

    def dfs(self, current_node, current_value):
        if current_node is None:
            return

        self.seen.add(current_value)
        self.dfs(current_node.left, current_value * 2 + 1)
        self.dfs(current_node.right, current_value * 2 + 2)


class FindElements:

    def __init__(self, root: Optional[TreeNode]):
        self.seen = set()
        self.bfs(root)

    def find(self, target: int) -> bool:
        return target in self.seen

    def bfs(self, root: TreeNode):
        queue = [root]
        root.val = 0

        while queue:
            current_node = queue.pop(0)

            self.seen.add(current_node.val)
            if current_node.left:
                current_node.left.val = current_node.val * 2 + 1
                queue.append(current_node.left)

            if current_node.right:
                current_node.right.val = current_node.val * 2 + 2
                queue.append(current_node.right)


# Your FindElements object will be instantiated and called as such:
# obj = FindElements(root)
# param_1 = obj.find(target)
