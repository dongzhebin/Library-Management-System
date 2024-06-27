

# 测试代码
import sys
sys.path.append('d:/palace')
from library.toolbox.library import Book, BTree, Library
import unittest


class TestBTree(unittest.TestCase):

    def setUp(self):
        self.btree = BTree(3)
        self.books = [
            Book(1, "Book One", "Author A", "Fiction", "2001", True),
            Book(2, "Book Two", "Author B", "Science", "2002", True),
            Book(3, "Book Three", "Author C", "Fiction", "2003", True),
            Book(4, "Book Four", "Author D", "History", "2004", True),
            Book(5, "Book Five", "Author E", "Science", "2005", True)
        ]
        for book in self.books:
            self.btree.insert(book)

    def test_insert(self):
        book = Book(6, "Book Six", "Author F", "Science", "2006", True)
        self.btree.insert(book)
        result = self.btree.search_tree(6)
        self.assertIsNotNone(result)
        self.assertEqual(result.book_id, 6)

    def test_search_existing(self):
        result = self.btree.search_tree(1)
        self.assertIsNotNone(result)
        self.assertEqual(result.book_id, 1)

    def test_search_non_existing(self):
        result = self.btree.search_tree(100)
        self.assertIsNone(result)

    def test_traverse(self):
        result = []
        self.btree.traverse(lambda book: result.append(book.book_id))
        expected = [1, 2, 3, 4, 5]
        self.assertListEqual(result, expected)

if __name__ == '__main__':
    unittest.main()


# 测试代码
import sys
sys.path.append('d:/palace')
from library.toolbox.library import Book, BTree, Library
import unittest


class TestBTree(unittest.TestCase):

    def setUp(self):
        self.btree = BTree(3)
        self.books = [
            Book(1, "Book One", "Author A", "Fiction", "2001", True),
            Book(2, "Book Two", "Author B", "Science", "2002", True),
            Book(3, "Book Three", "Author C", "Fiction", "2003", True),
            Book(4, "Book Four", "Author D", "History", "2004", True),
            Book(5, "Book Five", "Author E", "Science", "2005", True)
        ]
        for book in self.books:
            self.btree.insert(book)

    def test_insert(self):
        book = Book(6, "Book Six", "Author F", "Science", "2006", True)
        self.btree.insert(book)
        result = self.btree.search_tree(6)
        self.assertIsNotNone(result)
        self.assertEqual(result.book_id, 6)

    def test_search_existing(self):
        result = self.btree.search_tree(1)
        self.assertIsNotNone(result)
        self.assertEqual(result.book_id, 1)

    def test_search_non_existing(self):
        result = self.btree.search_tree(100)
        self.assertIsNone(result)

    def test_traverse(self):
        result = []
        self.btree.traverse(lambda book: result.append(book.book_id))
        expected = [1, 2, 3, 4, 5]
        self.assertListEqual(result, expected)

if __name__ == '__main__':
    unittest.main()
