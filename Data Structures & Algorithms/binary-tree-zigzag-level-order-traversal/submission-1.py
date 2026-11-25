# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        
        result = []
        queue = deque([root])

        right = True
        while queue:
            level_size = len(queue)
            level = deque()
            
            for _ in range(level_size):
                curr_node = queue.popleft()
                if right:
                    level.append(curr_node.val)
                else:
                    level.appendleft(curr_node.val)
                if curr_node.left:
                        queue.append(curr_node.left)
                if curr_node.right:
                        queue.append(curr_node.right) 
            right = not right
            result.append(level)
        
        return result

        