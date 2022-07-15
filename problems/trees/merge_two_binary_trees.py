"""
merge-two-binary-trees
https://leetcode.com/problems/merge-two-binary-trees/

Notes: 
Solution # 1: Nick White
Recursion
1. Add the value of both root nodes and store it in root1 node.
2. Modify the root1s left node by running step 1 with root1s left and root2s left.
3. Do the same root1s right.
4. If any one of left of right arg is None, return the other arg.
    4.1 - sum of one valid arg and one none arg is anyways equal to the valid arg.
    4.2 - if both args are none, they we expect a none. the exit condition will return the other arg which is also none. so it works out.
5. return the root1 node.

Solution # 2: Neet Code
Recursion
1. Create a new node with value from both args nodes.
2. If a node is none, consider it as zero.
3. Modify new nodes left by calling same method , send args as arg1s left and arg2s left.
4. Note that if an args left or right is none and sent to recursive call, we might ask for that none arg left. to avoid this, check if the node is not none before adding left or right as arg to the recursive call.
5. follow step 3 and 4 for new nodes, right.
6. return the new node

"""
from typing import Optional
from data_structures.Trees.Binary_Tree_Basic import TreeNode

class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        # root1 tree is modified
        if not root1:
            return root2
        if not root2:
            return root1
        root1.val = root1.val + root2.val
        root1.left = Solution().mergeTrees(root1.left, root2.left)
        root1.right =  Solution().mergeTrees(root1.right, root2.right)
        return root1
    
    
    def _mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        # this creates a new tree
        if root1 == None and root2 == None:
            return None
        val1 = root1.val if root1 else 0
        val2 = root2.val if root2 else 0
        new_node = TreeNode(val1+val2)
        new_node.left = Solution().mergeTrees(root1.left if root1 else None, root2.left if root2 else None)
        new_node.right = Solution().mergeTrees(root1.right if root1 else None, root2.right if root2 else None)
        return new_node
        