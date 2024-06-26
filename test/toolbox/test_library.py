import sys
sys.path.append('d:/palace')
from library.toolbox.library import Book, BTreeNode, BTree, Library
import unittest

class TestBTree(unittest.TestCase):

    def setUp(self):
        self.btree = BTree(3)
        self.book1 = Book(1, "Book One", "Introduction One", 5)
        self.book2 = Book(2, "Book Two", "Introduction Two", 3)
        self.book3 = Book(3, "Book Three", "Introduction Three", 7)
        self.book4 = Book(4, "Book Four", "Introduction Four", 2)
        self.book5 = Book(5, "Book Five", "Introduction Five", 9)

    def test_insert(self):
        self.btree.insert(self.book1)
        self.btree.insert(self.book2)
        self.btree.insert(self.book3)
        self.btree.insert(self.book4)
        self.btree.insert(self.book5)
        self.assertEqual(self.btree.search_tree(1), self.book1)
        self.assertEqual(self.btree.search_tree(2), self.book2)
        self.assertEqual(self.btree.search_tree(3), self.book3)
        self.assertEqual(self.btree.search_tree(4), self.book4)
        self.assertEqual(self.btree.search_tree(5), self.book5)

    def test_search(self):
        self.btree.insert(self.book1)
        self.btree.insert(self.book2)
        self.btree.insert(self.book3)
        self.assertIsNone(self.btree.search_tree(10))
        self.assertEqual(self.btree.search_tree(1), self.book1)
        self.assertEqual(self.btree.search_tree(2), self.book2)
        self.assertEqual(self.btree.search_tree(3), self.book3)

    def test_traverse(self):
        self.btree.insert(self.book1)
        self.btree.insert(self.book2)
        self.btree.insert(self.book3)
        self.btree.insert(self.book4)
        self.btree.insert(self.book5)
        result = []
        def collect_books(book):
            result.append(book.number)
        self.btree.traverse(collect_books)
        self.assertEqual(result, [1, 2, 3, 4, 5])

    def test_remove(self):
        self.btree.insert(self.book1)
        self.btree.insert(self.book2)
        self.btree.insert(self.book3)
        self.btree.insert(self.book4)
        self.btree.insert(self.book5)
        self.btree.remove(self.book3)
        self.assertIsNone(self.btree.search_tree(3))
        self.assertEqual(self.btree.search_tree(1), self.book1)
        self.assertEqual(self.btree.search_tree(2), self.book2)
        self.assertEqual(self.btree.search_tree(4), self.book4)
        self.assertEqual(self.btree.search_tree(5), self.book5)

if __name__ == '__main__':
    unittest.main()
