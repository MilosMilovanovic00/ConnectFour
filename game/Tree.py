class TreeNode(object):
    def __init__(self, data):
        self.data = data
        self.parent = None
        self.children = []

    def add_child(self, child):
        self.children.append(child)
        child.parent = self

    def is_root(self):
        return self.parent == None

    def is_leaf(self):
        return self.children == []


class Tree(object):

    def __init__(self):
        self.root = None

    def is_empty(self):
        return self.root == None

    def depth(self, node):
        if node.is_root():
            return 0
        else:
            return 1 + self.depth(node.parent)

    def height(self, node):
        if node.is_leaf():
            return 0
        else:
            return 1 + max(self.height(child) for child in node.children)

    def tree_height(self):
        return self.height(self.root)
