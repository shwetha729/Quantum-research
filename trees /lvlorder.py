# Question 1: Given a tree, print the node in level order from left to right.
# Please create the tree data and function and test cases and an analysis of time/space complexity
#

# Classic breadthfirst psuedocode
# printTree(Node root)

#    if(root == NULL) return

#    else
#       create a queue 'q'
#       q.enqueue(root)

#       while(q is not empty)
#            root = q.dequeue
#            print(root)

#            if(leftChild != NULL)
#               q.enqueue(leftChild)
#            if(rightChild != NULL)
#               q.enqueue(rightChild)

# The given node structure from challenge


class TreeNode:
    def __init__(self, data):
        self.data = data
        self.right = None
        self.left = None

# function


def LevelOrder(root):
    # Base Case
    if root is None:
        return

    # empty queue for level order traversal
    queue = []

    # Enqueue Root and initialize height
    queue.append(root)

    while(len(queue) > 0):
        # Print front queue and remove it from queue
        print(queue[0].data),
        TreeNode = queue.pop(0)

        # Enqueue left child
        if TreeNode.left is not None:
            queue.append(TreeNode.left)

        # Enqueue right child
        if TreeNode.right is not None:
            queue.append(TreeNode.right)


# test cases
root = TreeNode(1)
root.left = TreeNode(6)
root.right = TreeNode(3)
root.left.left = TreeNode(7)
root.left.right = TreeNode(5)

print("Level Order from left to right:")
LevelOrder(root)

# time complexity = O(n)
# space complexity = O(n) at worst case
