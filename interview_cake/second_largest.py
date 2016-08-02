class BinaryTreeNode:

    def __init__(self, value):
        self.value = value
        self.left  = None
        self.right = None

    def insert_left(self, value):
        self.left = BinaryTreeNode(value)
        return self.left

    def insert_right(self, value):
        self.right = BinaryTreeNode(value)
        return self.right

def second_largest(node):
    # write the body of your function here
    prev = node
    curr = node
    while curr.right:
        prev = curr
        curr = curr.right
    return prev.value

# run your function through some test cases here
# remember: debugging is half the battle!
myBST = BinaryTreeNode(50)
myBST.insert_left(30)
myBST.insert_right(80)
myBST.right.insert_right(90)
myBST.right.insert_left(70)

print second_largest(myBST)
