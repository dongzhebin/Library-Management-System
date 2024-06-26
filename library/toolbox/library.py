class Book:
    def __init__(self, number=0, name="", introduction="", left=0):
        self.number = number
        self.name = name
        self.introduction = introduction
        self.left = left

    def print(self):
        print("-------------------------------")
        print("这本书的信息如下：")
        print(f"编号: {self.number}")
        print(f"书名: {self.name}")
        print(f"简介: {self.introduction}")
        print(f"剩余数量: {self.left}")
        print("-------------------------------")

    def __eq__(self, other):
        return self.number == other.number

    def __lt__(self, other):
        return self.number < other.number

    def __gt__(self, other):
        return self.number > other.number


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


class Library:
    def __init__(self, filename):
        self.books = BTree(3)
        self.total = 0
        print("这是现在的库存信息：")
        self.read_file(filename)

    @staticmethod
    def read_book(aBook):
        with open(outFile, 'a') as file:
            file.write(f"{aBook.number}\n")
            file.write(f"{aBook.name}\n")
            file.write(f"{aBook.introduction}\n")
            file.write(f"{aBook.left}\n")

    def read_file(self, filename):
        self.total = 0
        with open(filename, 'r', encoding='utf-8') as inFile:
            lines = inFile.readlines()
            i = 0
            while i < len(lines):
                line = lines[i].strip()
                if line == '#':
                    break
                number = int(line)
                name = lines[i + 1].strip()
                introduction = lines[i + 2].strip()
                left = int(lines[i + 3].strip())
                aBook = Book(number, name, introduction, left)
                aBook.print()
                self.books.insert(aBook)
                self.total += left
                i += 4
        print(f"库存共有图书{self.total}本")


    def write_file(self, filename):
        global outFile
        outFile = filename
        with open(filename, 'w') as file:
            self.books.traverse(self.read_book)
            file.write('#')

    def search(self, num):
        return self.books.search_tree(num)

    @staticmethod
    def print_book(aBook):
        print("-------------------------------")
        print("这本书的信息如下：")
        print(f"编号: {aBook.number}")
        print(f"书名: {aBook.name}")
        print(f"简介: {aBook.introduction}")
        print(f"剩余数量: {aBook.left}")
        print("-------------------------------")

    
    def add(self):
        print("请输入图书信息(编号 书名 简介 数量)")
        num = int(input("编号: "))
        name = input("书名: ")
        introduction = input("简介: ")
        left = int(input("数量: "))
        new_book = Book(num, name, introduction, left)
        self.books.insert(new_book)
        print("这本书已入库，信息如下：")
        new_book.print()
        self.total += left

    def display(self):
        print("这是现在的库存信息：")
        self.books.traverse(self.print_book)
        print(f"库存共有图书{self.total}本")

    def remove(self):
        print("请输入要删除的图书编号：")
        num = int(input("编号: "))
        old_book = self.search(num)
        print("您即将删除这本书的所有信息：")
        old_book.print()
        print("确定要删除吗？[y/n]")
        choice = input("选择: ")
        if choice == 'y':
            self.books.remove(old_book)
            print(f"编号为{num}的书已成功从库中删除")
            self.total -= old_book.left

    def lend(self):
        print("请输入要借出的图书编号：")
        num = int(input("编号: "))
        old_book = self.search(num)
        old_book.left -= 1
        print(f"编号为{num}的图书已借出1本，下面是这本书的现存信息：")
        old_book.print()
        self.total -= 1

    def change(self):
        print("请输入要修改的图书编号：")
        num = int(input("编号: "))
        old_book = self.search(num)
        print("这是这本书的当前信息：")
        old_book.print()
        self.books.remove(old_book)
        print("请输入修改后的图书信息（编号 书名 简介 数量）")
        num = int(input("编号: "))
        name = input("书名: ")
        introduction = input("简介: ")
        left = int(input("数量: "))
        new_book = Book(num, name, introduction, left)
        self.books.insert(new_book)
        print("这本书的信息已修改为：")
        new_book.print()

    def back(self):
        print("请输入要归还的图书编号：")
        num = int(input("编号: "))
        old_book = self.search(num)
        old_book.left += 1
        print(f"编号为{num}的图书已归还，下面是这本书的现存信息：")
        old_book.print()
        self.total += 1

    def save(self, filename):
        self.write_file(filename)


def main():
    myLib = Library('books.txt')
    choice = 'y'
    while choice == 'y':
        print("请选择操作")
        print("--------------------------------")
        print("1----新书入库")
        print("2----查看库存")
        print("3----借阅")
        print("4----归还")
        print("5----删除旧书")
        print("6----修改图书信息")
        print("--------------------------------")
        option = int(input("选项: "))
        if option == 1:
            myLib.add()
        elif option == 2:
            myLib.display()
        elif option == 3:
            myLib.lend()
        elif option == 4:
            myLib.back()
        elif option == 5:
            myLib.remove()
        elif option == 6:
            myLib.change()
        choice = input("继续吗?[y/n] ")
    save_choice = input("是否保存修改？[y/n] ")
    if save_choice == 'y':
        myLib.save('books.txt')  # 需要保存时保存文件

if __name__ == "__main__":
    main()
