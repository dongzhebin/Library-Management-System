class BTreeNode:
    def __init__(self, book, left=None, right=None):
        self.book = book
        self.left = left
        self.right = right