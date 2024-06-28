class Book:
    def __init__(self, book_id=0, title="", author="", genre="", publication="", availability=True):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.genre = genre
        self.publication = publication
        self.availability = availability

    def print(self):
        print("-------------------------------")
        print("这本书的信息如下：")
        print(f"ID: {self.book_id}")
        print(f"标题: {self.title}")
        print(f"作者: {self.author}")
        print(f"类型: {self.genre}")
        print(f"出版年份: {self.publication}")
        print(f"可借阅: {'可借阅' if self.availability else '不可借阅'}")
        print("-------------------------------")

    def __eq__(self, other):
        return self.book_id == other.book_id

    def __lt__(self, other):
        return self.book_id < other.book_id

    def __gt__(self, other):
        return self.book_id > other.book_id

    def __repr__(self):
        return f"Book({self.book_id}, {self.title}, {self.author}, {self.genre}, {self.publication}, {self.availability})"
class BTreeNode:
    def __init__(self, t):
        self.t = t  # 最小度数
        self.keys = []  # 存储键
        self.children = []  # 存储子节点
        self.leaf = True  # 是否为叶节点

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
            k = k.book_id
        if x is not None:
            i = 0
            while i < x.size() and k > x.keys[i].book_id:
                i += 1
            if i < x.size() and k == x.keys[i].book_id:
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
        # BTree 删除逻辑应在此处实现
        pass
import csv

class Library:
    def __init__(self, filename):
        self.filename = filename  # 文件名
        self.books = BTree(3)
        self.total = 0
        self.user_history = {}
        print("这是当前的库存信息：")
        self.read_file(filename)

    def read_file(self, filename):
        self.total = 0
        with open(filename, 'r', newline='', encoding='utf-8') as inFile:
            reader = csv.reader(inFile)
            next(reader)  # 跳过标题行
            for row in reader:
                book_id = int(row[0])
                title = row[1]
                author = row[2]
                genre = row[3]
                publication = row[4]
                availability = row[5].strip().lower() == 'true'
                aBook = Book(book_id, title, author, genre, publication, availability)
                aBook.print()
                self.books.insert(aBook)
                self.total += 1
        print(f"库存中共有 {self.total} 本书")

    def write_file(self, filename):
        with open(filename, 'w', newline='', encoding='utf-8') as outFile:
            writer = csv.writer(outFile)
            writer.writerow(["ID", "Title", "Author", "Genre", "Publication Year", "Availability"])
            self.books.traverse(lambda book: writer.writerow([book.book_id, book.title, book.author, book.genre, book.publication, book.availability]))
        print("书籍信息已更新并保存到文件。")

    def add(self):
        print("请输入书籍信息 (ID 标题 作者 类型 出版年份 可借阅[True/False])")
        while True:
            try:
                book_id = int(input("ID: "))
                break
            except ValueError:
                print("无效的ID，请输入整数。")
        
        title = input("标题: ")
        author = input("作者: ")
        genre = input("类型: ")
        publication = input("出版年份: ")
        availability = input("可借阅[True/False]: ").strip().lower() == 'true'
        new_book = Book(book_id, title, author, genre, publication, availability)
        self.books.insert(new_book)
        print("这本书已添加到库存，信息如下：")
        new_book.print()
        self.total += 1
        self.write_file(self.filename)  # 添加后保存文件

    def remove(self):
        print("请输入要删除的书籍ID：")
        while True:
            try:
                book_id = int(input("ID: "))
                break
            except ValueError:
                print("无效的ID，请输入整数。")

        old_book = self.search(book_id)
        if old_book:
            print("你即将删除这本书的所有信息：")
            old_book.print()
            print("你确定要删除它吗？[y/n]")
            choice = input("选择: ")
            if choice.lower() == 'y':
                self.books.remove(old_book)
                print(f"ID为 {book_id} 的书籍已成功从库存中删除")
                self.total -= 1
                self.write_file(self.filename)  # 删除后保存文件
        else:
            print(f"ID为 {book_id} 的书籍不存在。")

    def lend(self):
        user_id = input("请输入你的用户ID: ")
        print("请输入要借出的书籍ID：")
        while True:
            try:
                book_id = int(input("ID: "))
                break
            except ValueError:
                print("无效的ID，请输入整数。")

        old_book = self.search(book_id)
        if old_book and old_book.availability:
            old_book.availability = False
            print(f"ID为 {book_id} 的书籍已被借出，这本书的当前信息如下：")
            old_book.print()
            self.write_file(self.filename)  # 借出后保存文件
            if user_id not in self.user_history:
                self.user_history[user_id] = []
            self.user_history[user_id].append(old_book)
        else:
            print(f"ID为 {book_id} 的书籍不可借阅。")

    def change(self):
        print("请输入要修改的书籍ID：")
        while True:
            try:
                book_id= int(input("ID: "))
                break
            except ValueError:
                print("无效的ID，请输入整数。")

        old_book = self.search(book_id)
        if old_book:
            print("这本书的当前信息如下：")
            old_book.print()
            self.books.remove(old_book)
            print("请输入修改后的书籍信息 (ID 标题 作者 类型 出版年份 可借阅[True/False])")
            while True:
                try:
                    book_id = int(input("ID: "))
                    break
                except ValueError:
                    print("无效的ID，请输入整数。")
            
            title = input("标题: ")
            author = input("作者: ")
            genre = input("类型: ")
            publication = input("出版年份: ")
            availability = input("可借阅[True/False]: ").strip().lower() == 'true'
            new_book = Book(book_id, title, author, genre, publication, availability)
            self.books.insert(new_book)
            print("这本书的信息已更新，新信息如下：")
            new_book.print()
            self.write_file(self.filename)  # 修改后保存文件
        else:
            print(f"ID为 {book_id} 的书籍不存在。")

    def search(self, book_id):
        return self.books.search_tree(book_id)

    def display(self):
        print("当前库存中的所有书籍：")
        self.books.traverse(lambda book: book.print())

    def recommend(self):
        user_id = input("请输入你的用户ID: ")
        if user_id in self.user_history and len(self.user_history[user_id]) > 0:
            print(f"用户 {user_id} 的借阅历史如下：")
            for book in self.user_history[user_id]:
                book.print()
            print("根据你的借阅历史，为你推荐以下书籍：")
            # 实现推荐逻辑，这里简单起见，直接推荐最新添加的书籍
            latest_book = self.user_history[user_id][-1]
            latest_book.print()
        else:
            print(f"用户 {user_id} 没有借阅历史记录或者用户不存在。")

def main():
    myLib = Library('library_books_dataset.csv')
    while True:
        print("请选择操作: [a] 添加书籍 [d] 显示库存 [r] 删除书籍 [l] 借阅书籍 [c] 修改书籍 [rec] 推荐书籍 [q] 退出")
        choice = input("选择: ").lower()
        if choice == 'a':
            myLib.add()
        elif choice == 'd':
            myLib.display()
        elif choice == 'r':
            myLib.remove()
        elif choice == 'l':
            myLib.lend()
        elif choice == 'c':
            myLib.change()
        elif choice == 'rec':
            myLib.recommend()
        elif choice == 'q':
            break
        else:
            print("无效的选择，请重新输入。")

if __name__ == "__main__":
    main()
