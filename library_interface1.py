import sys
import csv
import traceback
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget, QMessageBox, QInputDialog

class Book:
    def __init__(self, book_id=0, title="", author="", genre="", publication="", availability=True, borrow_count=0):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.genre = genre
        self.publication = publication
        self.availability = availability
        self.borrow_count = borrow_count

    def print(self):
        print("-------------------------------")
        print("Book information:")
        print(f"ID: {self.book_id}")
        print(f"Title: {self.title}")
        print(f"Author: {self.author}")
        print(f"Genre: {self.genre}")
        print(f"Publication Year: {self.publication}")
        print(f"Availability: {'Available' if self.availability else 'Not Available'}")
        print(f"Borrow Count: {self.borrow_count}")
        print("-------------------------------")

    def __eq__(self, other):
        return self.book_id == other.book_id

    def __lt__(self, other):
        return self.book_id < other.book_id

    def __gt__(self, other):
        return self.book_id > other.book_id

class BTreeNode:
    def __init__(self, t):
        self.t = t  # Minimum degree
        self.keys = []  # Keys
        self.children = []  # Child nodes
        self.leaf = True  # Is leaf node

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

    def remove_key(self, value):
        self.keys.remove(value)

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

    def search_by_title(self, keyword, x=None):
        results = []
        if x is not None:
            for book in x.keys:
                if keyword.lower() in book.title.lower():
                    results.append(book)
            if not x.leaf:
                for child in x.children:
                    results.extend(self.search_by_title(keyword, child))
        else:
            results = self.search_by_title(keyword, self.root)
        return results

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
        if isinstance(payload, Book):
            payload = payload.book_id
        self._remove(self.root, payload)

    def _remove(self, node, payload):
        if payload in [book.book_id for book in node.keys]:
            for i, book in enumerate(node.keys):
                if book.book_id == payload:
                    node.remove_key(book)
                    return
        elif not node.leaf:
            for i, book in enumerate(node.keys):
                if payload < book.book_id:
                    self._remove(node.children[i], payload)
                    return
            self._remove(node.children[-1], payload)

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

class User:
    def __init__(self, nickname, username, password):
        self.nickname = nickname
        self.username = username
        self.password = password
        self.borrow_history = []
        self.most_borrowed_genre = ""
        self.most_borrowed_author = ""
        

class Library:
    def __init__(self, filename):
        self.filename = filename
        self.books = BTree(3)
        self.total = 0
        self.users = []
        self.logged_in_user = None
        print("Current inventory information:")
        self.read_file(filename)

    def read_file(self, filename):
        self.total = 0
        try:
            with open(filename, 'r', newline='', encoding='utf-8') as inFile:
                reader = csv.reader(inFile)
                next(reader)  # Skip header
                for row in reader:
                    book_id = int(row[0])
                    title = row[1]
                    author = row[2]
                    genre = row[3]
                    publication = row[4]
                    availability = row[5].strip().lower() == 'true'
                    borrow_count = int(row[6]) if len(row) > 6 else 0  # Check for borrow_count
                    aBook = Book(book_id, title, author, genre, publication, availability, borrow_count)
                    aBook.print()
                    self.books.insert(aBook)
                    self.total += 1
            print(f"There are {self.total} books in inventory")
        except Exception as e:
            print(f"Failed to read file: {e}")
            traceback.print_exc()

    def write_file(self, filename):
        try:
            with open(filename, 'w', newline='', encoding='utf-8') as outFile:
                writer = csv.writer(outFile)
                writer.writerow(["ID", "Title", "Author", "Genre", "Publication Year", "Availability", "Borrow Count"])
                self.books.traverse(lambda book: writer.writerow([book.book_id, book.title, book.author, book.genre, book.publication, book.availability, book.borrow_count]))
            print("Book information has been updated and saved to the file.")
        except Exception as e:
            print(f"Failed to write file: {e}")
            traceback.print_exc()

    def read_user_file(self, filename):
        try:
            with open(filename, 'r', newline='', encoding='utf-8') as inFile:
                reader = csv.reader(inFile)
                next(reader)  # Skip header
                for row in reader:
                    nickname, username, password, borrow_history, most_borrowed_genre, most_borrowed_author = row
                    user = User(nickname, username, password)
                    user.borrow_history = borrow_history.split(';') if borrow_history else []
                    user.most_borrowed_genre = most_borrowed_genre
                    user.most_borrowed_author = most_borrowed_author
                    self.users.append(user)
        except FileNotFoundError:
            print("User file not found. Starting with an empty user list.")
        except Exception as e:
            print(f"Failed to read user file: {e}")
            traceback.print_exc()

    def write_user_file(self, filename):
        try:
            with open(filename, 'w', newline='', encoding='utf-8') as outFile:
                writer = csv.writer(outFile)
                writer.writerow(["Nickname", "Username", "Password", "Borrow History", "Most Borrowed Genre", "Most Borrowed Author"])
                for user in self.users:
                    writer.writerow([user.nickname, user.username, user.password, ';'.join(user.borrow_history), user.most_borrowed_genre, user.most_borrowed_author])
            print("User information has been updated and saved to the file.")
        except Exception as e:
            print(f"Failed to write file: {e}")
            traceback.print_exc()
            
    def find_user(self, username):
        for user in self.users:
            if user.username == username:
                return user
        return None
    
    def register(self, nickname, username, password):
        if self.find_user(username):
            return False, "Username already exists."
        new_user = User(nickname, username, password)
        self.users.append(new_user)
        self.write_user_file('users.csv')
        return True, "Registration successful."

    def login(self, username, password):
        user = self.find_user(username)
        if user and user.password == password:
            self.logged_in_user = user
            return True, "Login successful."
        else:
            return False, "Invalid username or password."

    def is_unique(self, book_id, title):
        for book in self.books.root.keys:
            if book.book_id == book_id or book.title == title:
                return False
        return True

    def remove_book(self, book_id):
        book = self.books.search_tree(book_id)
        if book:
            self.books.remove(book)
            self.total -= 1
            self.write_file(self.filename)
            return True
        return False
    def borrow_book(self, title):
        books = self.books.search_by_title(title)
        if books:
            for book in books:
                if book.availability:
                    book.availability = False
                    book.borrow_count += 1
                    self.write_file(self.filename)
                    return True, book
            return False, "Book is not available for borrowing."
        return False, "Book not found."
    def return_book(self, title):
        books = self.books.search_by_title(title)
        if books:
            for book in books:
                if not book.availability:
                    book.availability = True
                    self.write_file(self.filename)
                    return True, book
            return False, "The book is not currently borrowed."
        return False, "Book not found."
    
    def recommend_books(self):
        try:
            # 找到借阅次数最多的书
            most_borrowed_book = None

            def update_most_borrowed(book):
                nonlocal most_borrowed_book
                if most_borrowed_book is None or book.borrow_count > most_borrowed_book.borrow_count:
                    most_borrowed_book = book

            self.books.traverse(update_most_borrowed)
            if most_borrowed_book is None:
                return "No books found."

            # 获取相同类别的书
            genre = most_borrowed_book.genre
            recommended_books = []

            def add_if_same_genre(book):
                if book.genre == genre and book != most_borrowed_book:
                    recommended_books.append(book)

            self.books.traverse(add_if_same_genre)

            if recommended_books:
                return recommended_books
            else:
                return "No other books found in the same genre."
        except Exception as e:
            import traceback
            traceback.print_exc()
            return f"An error occurred: {e}"

    def _update_most_borrowed(self, book, most_borrowed_book):
        if most_borrowed_book is None or book.borrow_count > most_borrowed_book.borrow_count:
            most_borrowed_book = book

    def _add_if_same_genre(self, book, genre, recommended_books):
        if book.genre == genre:
            recommended_books.append(book)

class LibraryGUI(QMainWindow):
    def __init__(self, library):
        super().__init__()
        self.library = library
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Library Management System')

        layout = QVBoxLayout()

        self.registerButton = QPushButton('Register', self)
        self.registerButton.clicked.connect(self.register)
        layout.addWidget(self.registerButton)

        self.loginButton = QPushButton('Login', self)
        self.loginButton.clicked.connect(self.login)
        layout.addWidget(self.loginButton)

        self.searchButton = QPushButton('Search Book', self)
        self.searchButton.clicked.connect(self.search_book)
        layout.addWidget(self.searchButton)

        self.addButton = QPushButton('Add Book', self)
        self.addButton.clicked.connect(self.add_book)
        layout.addWidget(self.addButton)

        self.deleteButton = QPushButton('Delete Book', self)
        self.deleteButton.clicked.connect(self.delete_book)
        layout.addWidget(self.deleteButton)

        self.modifyButton = QPushButton('Modify Book', self)
        self.modifyButton.clicked.connect(self.modify_book)
        layout.addWidget(self.modifyButton)

        self.displayButton = QPushButton('Display Inventory', self)
        self.displayButton.clicked.connect(self.display_inventory)
        layout.addWidget(self.displayButton)

        self.recommendButton = QPushButton('Recommend Books', self)
        self.recommendButton.clicked.connect(self.recommend_books)
        layout.addWidget(self.recommendButton)

        self.borrowButton = QPushButton('Borrow Book', self)
        self.borrowButton.clicked.connect(self.borrow_book)
        layout.addWidget(self.borrowButton)

        self.returnButton = QPushButton('Return Book', self)
        self.returnButton.clicked.connect(self.return_book)
        layout.addWidget(self.returnButton)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

    def add_book(self):
        try:
            book_id, ok1 = QInputDialog.getInt(self, 'Add Book', 'Enter book ID:')
            if not ok1:
                return
            title, ok2 = QInputDialog.getText(self, 'Add Book', 'Enter book title:')
            if not ok2:
                return
            author, ok3 = QInputDialog.getText(self, 'Add Book', 'Enter author:')
            if not ok3:
                return
            genre, ok4 = QInputDialog.getText(self, 'Add Book', 'Enter genre:')
            if not ok4:
                return
            publication, ok5 = QInputDialog.getText(self, 'Add Book', 'Enter publication year:')
            if not ok5:
                return
            availability, ok6 = QInputDialog.getItem(self, 'Add Book', 'Enter availability:', ['True', 'False'], 0, False)
            if not ok6:
                return
            borrow_count, ok7 = QInputDialog.getInt(self, 'Add Book', 'Enter borrow count:')
            if not ok7:
                return

            aBook = Book(book_id, title, author, genre, publication, availability == 'True', borrow_count)
            if self.library.is_unique(book_id, title):
                self.library.books.insert(aBook)
                self.library.total += 1
                self.library.write_file(self.library.filename)
                QMessageBox.information(self, 'Success', 'Book added successfully.')
            else:
                QMessageBox.warning(self, 'Error', 'Book ID or Title already exists.')
        except Exception as e:
            QMessageBox.critical(self, 'Error', f'An error occurred: {e}')
            traceback.print_exc()

    def delete_book(self):
        try:
            book_id, ok = QInputDialog.getInt(self, 'Delete Book', 'Enter book ID to delete:')
            if not ok:
                return
            if self.library.remove_book(book_id):
                QMessageBox.information(self, 'Success', 'Book deleted successfully.')
            else:
                QMessageBox.warning(self, 'Error', 'Book ID not found.')
        except Exception as e:
            QMessageBox.critical(self, 'Error', f'An error occurred: {e}')
            traceback.print_exc()

    def display_inventory(self):
        if self.library.total == 0:
            QMessageBox.information(self, 'Inventory', 'No books in inventory.')
        else:
            books_info = []
            self.library.books.traverse(lambda book: books_info.append(f"ID: {book.book_id}, Title: {book.title}, Author: {book.author}, Genre: {book.genre}, Publication: {book.publication}, Availability: {book.availability}, Borrow Count: {book.borrow_count}"))
            QMessageBox.information(self, 'Inventory', '\n'.join(books_info))

    def search_book(self):
        try:
            search_keyword, ok = QInputDialog.getText(self, 'Search Book', 'Enter keyword to search:')
            if not ok:
                return
            books = self.library.books.search_by_title(search_keyword)
            if books:
                book_info = "\n\n".join([f"ID: {book.book_id}\nTitle: {book.title}\nAuthor: {book.author}\nGenre: {book.genre}\nPublication Year: {book.publication}\nAvailability: {'Available' if book.availability else 'Not Available'}\nBorrow Count: {book.borrow_count}" for book in books])
                QMessageBox.information(self, 'Books Found', book_info)
            else:
                QMessageBox.warning(self, 'Error', 'No books found matching the keyword.')
        except Exception as e:
            QMessageBox.critical(self, 'Error', f'An error occurred: {e}')
            traceback.print_exc()

    def borrow_book(self):
        try:
            title, ok = QInputDialog.getText(self, 'Borrow Book', 'Enter book title to borrow:')
            if not ok:
                return
            success, result = self.library.borrow_book(title)
            if success:
                book = result
                QMessageBox.information(self, 'Success', f'You have successfully borrowed "{book.title}".')
            else:
                QMessageBox.warning(self, 'Error', result)
        except Exception as e:
            QMessageBox.critical(self, 'Error', f'An error occurred: {e}')
            traceback.print_exc()

    def return_book(self):
        try:
            title, ok = QInputDialog.getText(self, 'Return Book', 'Enter book title to return:')
            if not ok:
                return
            success, result = self.library.return_book(title)
            if success:
                book = result
                QMessageBox.information(self, 'Success', f'You have successfully returned "{book.title}".')
            else:
                QMessageBox.warning(self, 'Error', result)
        except Exception as e:
            QMessageBox.critical(self, 'Error', f'An error occurred: {e}')
            traceback.print_exc()

    def login(self):
        try:
            username, ok1 = QInputDialog.getText(self, 'Login', 'Enter your username:')
            if not ok1:
                return
            password, ok2 = QInputDialog.getText(self, 'Login', 'Enter your password:')
            if not ok2:
                return

            for user in self.library.users:
                if user.username == username and user.password == password:
                    self.library.logged_in_user = user
                    QMessageBox.information(self, 'Login', f'Welcome, {user.nickname}!')
                    return

            QMessageBox.warning(self, 'Login', 'Invalid username or password.')
        except Exception as e:
            QMessageBox.critical(self, 'Error', f'An error occurred: {e}')
            traceback.print_exc()

    def register(self):
        try:
            nickname, ok1 = QInputDialog.getText(self, 'Register', 'Enter your nickname:')
            if not ok1:
                return
            username, ok2 = QInputDialog.getText(self, 'Register', 'Enter your username:')
            if not ok2:
                return
            password, ok3 = QInputDialog.getText(self, 'Register', 'Enter your password:')
            if not ok3:
                return

            user = User(nickname, username, password)
            self.library.users.append(user)
            self.library.write_user_file('users.csv')
            QMessageBox.information(self, 'Register', 'Registration successful!')
        except Exception as e:
            QMessageBox.critical(self, 'Error', f'An error occurred: {e}')
            traceback.print_exc()

    def recommend_books(self):
        try:
            recommended_books = self.library.recommend_books()
            if isinstance(recommended_books, str):
                QMessageBox.warning(self, 'Error', recommended_books)
            else:
                book_info = "\n\n".join([f"ID: {book.book_id}\nTitle: {book.title}\nAuthor: {book.author}\nGenre: {book.genre}\nPublication Year: {book.publication}\nAvailability: {'Available' if book.availability else 'Not Available'}\nBorrow Count: {book.borrow_count}" for book in recommended_books])
                QMessageBox.information(self, 'Recommended Books', book_info)
        except Exception as e:
            import traceback
            traceback.print_exc()
            QMessageBox.critical(self, 'Error', f'An error occurred: {e}')
            
    def modify_book(self):
        book_id, ok = QInputDialog.getInt(self, 'Modify Book', 'Enter book ID to modify:')
        if not ok:
            return

        book = self.library.books.search_tree(book_id)
        if book is None:
            QMessageBox.warning(self, 'Error', 'Book not found.')
            return

        new_title, ok1 = QInputDialog.getText(self, 'Modify Book', 'Enter new title:', text=book.title)
        if not ok1:
            return
        new_author, ok2 = QInputDialog.getText(self, 'Modify Book', 'Enter new author:', text=book.author)
        if not ok2:
            return
        new_genre, ok3 = QInputDialog.getText(self, 'Modify Book', 'Enter new genre:', text=book.genre)
        if not ok3:
            return
        new_publication, ok4 = QInputDialog.getText(self, 'Modify Book', 'Enter new publication year:', text=book.publication)
        if not ok4:
            return
        new_availability, ok5 = QInputDialog.getItem(self, 'Modify Book', 'Enter new availability:', ['True', 'False'], 0, False)
        if not ok5:
            return
        new_borrow_count, ok6 = QInputDialog.getInt(self, 'Modify Book', 'Enter new borrow count:', value=book.borrow_count)
        if not ok6:
            return
        

        # 更新书籍信息
        book.title = new_title
        book.author = new_author
        book.genre = new_genre
        book.publication = new_publication
        book.availability = new_availability == 'True'
        book.borrow_count = new_borrow_count

        # 更新CSV文件
        self.library.write_file(self.library.filename)
        QMessageBox.information(self, 'Success', 'Book modified successfully.')

    

def main():
    library = Library('library_books_dataset.csv')
    library.read_user_file('users.csv')

    app = QApplication(sys.argv)
    gui = LibraryGUI(library)
    gui.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
