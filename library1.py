import csv
import unittest

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
        print("The information of this book is as follows:")
        print(f"ID: {self.book_id}")
        print(f"Title: {self.title}")
        print(f"Author: {self.author}")
        print(f"Genre: {self.genre}")
        print(f"Publication Year: {self.publication}")
        print(f"Availability: {'Available' if self.availability else 'Not Available'}")
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
        self.keys = []  # Stores the keys
        self.children = []  # Stores the child nodes
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
        # BTree removal logic should be implemented here
        pass


class Library:
    def __init__(self, filename):
        self.filename = filename  # File name
        self.books = BTree(3)
        self.total = 0
        print("This is the current inventory information:")
        self.read_file(filename)

    def read_file(self, filename):
        self.total = 0
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
                aBook = Book(book_id, title, author, genre, publication, availability)
                aBook.print()
                self.books.insert(aBook)
                self.total += 1
        print(f"There are a total of {self.total} books in the inventory")

    def write_file(self, filename):
        with open(filename, 'w', newline='', encoding='utf-8') as outFile:
            writer = csv.writer(outFile)
            writer.writerow(["ID", "Title", "Author", "Genre", "Publication Year", "Availability"])
            self.books.traverse(lambda book: writer.writerow([book.book_id, book.title, book.author, book.genre, book.publication, book.availability]))
        print("The book information has been updated and saved to the file.")

    def add(self):
        print("Please enter the book information (ID Title Author Genre Publication Year Availability[True/False])")
        while True:
            try:
                book_id = int(input("ID: "))
                break
            except ValueError:
                print("Invalid ID, please enter an integer.")
        
        title = input("Title: ")
        author = input("Author: ")
        genre = input("Genre: ")
        publication = input("Publication Year: ")
        availability = input("Availability[True/False]: ").strip().lower() == 'true'
        new_book = Book(book_id, title, author, genre, publication, availability)
        self.books.insert(new_book)
        print("This book has been added to the inventory, the information is as follows:")
        new_book.print()
        self.total += 1
        self.write_file(self.filename)  # Save the file after adding

    def remove(self):
        print("Please enter the ID of the book to be deleted:")
        while True:
            try:
                book_id = int(input("ID: "))
                break
            except ValueError:
                print("Invalid ID, please enter an integer.")

        old_book = self.search(book_id)
        if old_book:
            print("You are about to delete all information of this book:")
            old_book.print()
            print("Are you sure you want to delete it? [y/n]")
            choice = input("Choice: ")
            if choice.lower() == 'y':
                self.books.remove(old_book)
                print(f"The book with ID {book_id} has been successfully removed from the inventory")
                self.total -= 1
                self.write_file(self.filename)  # Save the file after deletion
        else:
            print(f"The book with ID {book_id} does not exist.")

    def lend(self):
        print("Please enter the ID of the book to be lent:")
        while True:
            try:
                book_id = int(input("ID: "))
                break
            except ValueError:
                print("Invalid ID, please enter an integer.")

        old_book = self.search(book_id)
        if old_book and old_book.availability:
            old_book.availability = False
            print(f"The book with ID {book_id} has been lent out, the current information of this book is as follows:")
            old_book.print()
            self.write_file(self.filename)  # Save the file after lending
        else:
            print(f"The book with ID {book_id} is not available for lending.")

    def change(self):
        print("Please enter the ID of the book to be modified:")
        while True:
            try:
                book_id = int(input("ID: "))
                break
            except ValueError:
                print("Invalid ID, please enter an integer.")

        old_book = self.search(book_id)
        if old_book:
            print("This is the current information of this book:")
            old_book.print()
            self.books.remove(old_book)
            print("Please enter the modified book information (ID Title Author Genre Publication Year Availability[True/False])")
            while True:
                try:
                    book_id = int(input("ID: "))
                    break
                except ValueError:
                    print("Invalid ID, please enter an integer.")
            
            title = input("Title: ")
            author = input("Author: ")
            genre = input("Genre: ")
            publication = input("Publication Year: ")
            availability = input("Availability[True/False]: ").strip().lower() == 'true'
            new_book = Book(book_id, title, author, genre, publication, availability)
            self.books.insert(new_book)
            print("The information of this book has been updated, the new information is as follows:")
            new_book.print()
            self.write_file(self.filename)  # Save the file after modification
        else:
            print(f"The book with ID {book_id} does not exist.")

    def search(self, book_id):
        return self.books.search_tree(book_id)

    def display(self):
        print("All books currently in inventory:")
        self.books.traverse(lambda book: book.print())

def main():
    myLib = Library('library_books_dataset.csv')
    while True:
        print("Please choose the operation to perform: [a] Add book [d] Display inventory [r] Remove book [l] Lend book [c] Change book [q] Quit")
        choice = input("Choice: ").lower()
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
        elif choice == 'q':
            break
        else:
            print("Invalid choice, please re-enter.")

if __name__ == "__main__":
    main()
