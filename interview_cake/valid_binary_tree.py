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


def is_valid(bt):
    if not bt.left and not bt.right:
        return True
    if bt.left:
        if bt.left.value > bt.value:
            return False
        return is_valid(bt.left)
    if bt.right:
        if bt.right.value < bt.value:
            return False
        return is_valid(bt.right)


myBT = BinaryTreeNode(50)
myBT.insert_left(30)
myBT.insert_right(80)
myBT.left.insert_left(20)
myBT.left.insert_right(60)
myBT.right.insert_right(90)
myBT.right.insert_left(70)
# print "should be true"
print is_valid(myBT)
# myBT.insert_left(3)
# myBT.insert_right(7)
# myBT.right.insert_left(6)
# myBT.left.insert_right(2)
# print "should be false"
# print is_valid(myBT)
