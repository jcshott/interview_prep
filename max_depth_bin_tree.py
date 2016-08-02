class Node(object):

    def __init__(self, val=None):
        self.value = val
        self.leftChild = None
        self.rightChild = None

    def __repr__(self):
        return "<value: {}, leftChild: {}, rightChild: {}>".format(self.value, self.leftChild, self.rightChild)

class BinarySearchTree(object):

    def __init__(self):
        self.root = None
        self.size = 0

    def insert(self, value):
        #create new node with value
        new_node = Node(value)
        #check if we have a root. if not, make this root and return
        if not self.root:
            self.root = new_node
            self.size += 1
            return
        # find where we have an open spot using algo that if val less than curr node, go to left, otherwise, go to right
        prev = None
        curr = self.root
        # we keep track of previous and current because this loop will stop when current is None/not a valid node so we need to know the last valid node.
        while curr:
            # if value is greater, it belongs to right, so traverse right side of tree from curr node.
            if value > curr.value:
                prev = curr
                curr = curr.rightChild
            # if val is lower, it belongs on left of curr node so traverse left side from curr node.
            elif value < curr.value:
                prev = curr
                curr = curr.leftChild
            # a check to get out if we already have this value
            else:
                print 'value already in tree, try again'
                return
        # when we hit an empty spot (non-valid node), check the last valid node and insert new_node appropriatly
        if prev.value > value:
            prev.leftChild = new_node
        else:
            prev.rightChild = new_node
        self.size += 1


    # def max_depth(self):
    #     def dfs_depth(curr):
    #         if not curr:
    #             return 0
    #         l = dfs_depth(curr.leftChild) + 1
    #         r = dfs_depth(curr.rightChild) + 1
    #
    #         return max(l,r)
    #     return dfs_depth(self.root)
    def max_depth(self, curr="root"):
        if not curr:
            return 0
        elif curr == "root":
            l = self.max_depth(self.root.leftChild) + 1
            r = self.max_depth(self.root.rightChild) + 1
        else:
            l = self.max_depth(curr.leftChild) + 1
            r = self.max_depth(curr.rightChild) + 1
        return max(l,r)


myBST = BinarySearchTree()

myBST.insert(5)

myBST.insert(7)
myBST.insert(3)
myBST.insert(6)
myBST.insert(8)
myBST.insert(9)

print myBST.max_depth()
