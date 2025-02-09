from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        """
        recursive dfs, CACHE, tree, path

        time: o(n) we only traverse once
        space: o(n)
        """

        def dfs(node, curr_path_sum):
            # exit condition
            if not node:
                return

            # calculate curr path sum and required old path sum
            curr_path_sum += node.val
            old_path_sum = curr_path_sum - targetSum

            # do this first, before updating the cache with curr path sum
            # if cache has this required old path sum,
            # update the number of valid paths
            self.path_count += cache.get(old_path_sum, 0)

            # update the cache with the curr path sum
            cache[curr_path_sum] = cache.get(curr_path_sum, 0) + 1

            dfs(node.left, curr_path_sum)
            dfs(node.right, curr_path_sum)

            # when moving to a different branch, the curr path sum is no longer available
            # because curr path sum is a local variable and after recursion, it resets
            # but cache is global, we need to change it manually
            # so, decrement its frequency (like backtracking)
            cache[curr_path_sum] -= 1

        self.path_count = 0
        cache = {0: 1}
        dfs(root, 0)
        return self.path_count

        """
        
        brute force
        no cache, check all possible sums

                10, 15, 18, 21, 16, 17, 7, 18
            5, 8, 11, 6, 7, 8       -3, 8
        3, 6, 1        2, 3          11
        3, -2            1

        time: o(n * 3h)
                worst case skewed tree h = n -> o(3n^2)
                avarege case balanced h = logn -> o(3nlogn)
        space: o(h)
        

        def dfs(node):
            if not node:
                return []
            
            left = dfs(node.left)
            right = dfs(node.right)
            values = ([node.val] + [node.val + value for value in left] 
                    + [node.val + value for value in right])
            
            for value in values:
                if value == targetSum:
                    self.res += 1
            return values
        

        self.res = 0
        dfs(root)
        return self.res
        """


class Solution(object):
    def pathSum(self, root, target):
        # define global result and path
        self.result = 0
        cache = {0: 1}

        # recursive to get result
        self.dfs(root, target, 0, cache)

        # return result
        return self.result

    def dfs(self, root, target, currPathSum, cache):
        # exit condition
        if root is None:
            return
        # calculate currPathSum and required oldPathSum
        currPathSum += root.val
        oldPathSum = currPathSum - target
        # update result and cache
        self.result += cache.get(oldPathSum, 0)
        cache[currPathSum] = cache.get(currPathSum, 0) + 1

        # dfs breakdown
        self.dfs(root.left, target, currPathSum, cache)
        self.dfs(root.right, target, currPathSum, cache)
        # when move to a different branch, the currPathSum is no longer available, hence remove one.
        cache[currPathSum] -= 1


class Solution:
    count = 0

    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:

        def dfs(root, start, curr_sum):
            if not root:
                return

            curr_sum -= root.val
            if curr_sum == 0:
                self.count += 1

            dfs(root.left, False, curr_sum)
            dfs(root.right, False, curr_sum)

            if start:
                dfs(root.left, True, targetSum)
                dfs(root.right, True, targetSum)

        dfs(root, True, targetSum)
        return self.count
