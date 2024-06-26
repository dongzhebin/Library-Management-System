class BTreeNode:
    def __init__(self, t):
        self.t = t  # 最小度数
        self.keys = []  # 存储节点的关键字
        self.children = []  # 存储子节点
        self.leaf = True  # 是否是叶节点

    def split(self, parent, payload):
        new_node = BTreeNode(self.t)
        mid_point = self.size() // 2
        split_value = self.keys[mid_point]
        parent.add_key(split_value)

        new_node.children = self.children[mid_point + 1:]
        self.children = self.children[:mid_point + 1]
        new_node.keys = self.keys[mid_point + 1:]
        self.keys = self.keys[:mid_point]

        if len(new_node.children) > 0:
            new_node.leaf = False

        parent.children = parent.add_child(new_node)
        if payload < split_value:
            return self
        else:
            return new_node

    def add_key(self, value):
        self.keys.append(value)
        self.keys.sort()

    def add_child(self, new_node):
        i = len(self.children) - 1
        while i >= 0 and self.children[i].keys[0] > new_node.keys[0]:
            i -= 1
        return self.children[:i + 1] + [new_node] + self.children[i + 1:]

    def size(self):
        return len(self.keys)


class BTree:
    def __init__(self, t):
        self.t = t
        self.root = BTreeNode(t)

    def insert(self, payload):
        node = self.root
        if node.size() == (2 * self.t) - 1:
            new_root = BTreeNode(self.t)
            new_root.children.append(self.root)
            new_root.leaf = False
            node = node.split(new_root, payload)
            self.root = new_root
        while not node.leaf:
            i = node.size() - 1
            while i > 0 and payload < node.keys[i]:
                i -= 1
            i += 1
            next_node = node.children[i]
            if next_node.size() == (2 * self.t) - 1:
                node = next_node.split(node, payload)
            else:
                node = next_node
        node.add_key(payload)

    def search_tree(self, k, x=None):
        if isinstance(k, Book):
            k = k.number
        if x is not None:
            i = 0
            while i < x.size() and k > x.keys[i].number:
                i += 1
            if i < x.size() and k == x.keys[i].number:
                return x.keys[i]
            elif x.leaf:
                return None
            else:
                return self.search_tree(k, x.children[i])
        else:
            return self.search_tree(k, self.root)

    def traverse(self, func):
        self._traverse(self.root, func)

    def _traverse(self, node, func):
        for i in range(node.size()):
            if not node.leaf:
                self._traverse(node.children[i], func)
            func(node.keys[i])
        if not node.leaf:
            self._traverse(node.children[node.size()], func)

    def remove(self, payload):
        self._remove(self.root, payload)

    def _remove(self, node, payload):
        # B树删除逻辑应在这里实现
        pass
