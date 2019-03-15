from collections.abc import Sequence
import unittest


class BinaryTree:

    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left  = left
        self.right = right

    def to_dict(self):
        return self.__traverse_dict(self.__dict__)

    def __traverse_dict(self, dict_instance):
        object = {}
        for key, value in dict_instance.items():
            object[key] = self.__traverse(value)
        return object

    def __traverse(self, value):
        if hasattr(value, '__dict__'):
            return self.__traverse_dict(value.__dict__)
        return value


class IndexableNode(BinaryTree, Sequence):

    def _search(self, count, index):
        if self.left:
            found, count = self.left._search(count, index)
            if found:
                return found, count
        if count == index:
            return self, count
        count += 1
        if self.right:
            found, count = self.right._search(count, index)
            if found:
                return found, count
        return None, count

    def __getitem__(self, index):
        found, _ = self._search(0, index)
        if not found:
            raise IndexError('Index ({}) out of range'.format(index))
        return found.value

    def __len__(self):
        _, count = self._search(0, None)
        return count


class TestIndexableNode(unittest.TestCase):

    def setUp(self):
        self.tree = IndexableNode(
                10,
                left=IndexableNode(
                    5,
                    left=IndexableNode(2),
                    right=IndexableNode(
                        6,
                        right=IndexableNode(7)
                        )
                    ),
                right=IndexableNode(
                    15,
                    left=IndexableNode(11)
                    )
                )

    def testDirectAccess(self):
        self.assertEqual(7, self.tree.left.right.right.value)

    def testIndexing(self):
        self.assertEqual(2, self.tree[0])
        self.assertEqual(5, self.tree[1])
        self.assertEqual(10, self.tree[4])

    def testIn(self):
        self.assertTrue(11 in self.tree)
        self.assertFalse(17 in self.tree)

    def testToList(self):
        self.assertEqual([2, 5, 6, 7, 10, 11, 15], list(self.tree))

    def testLen(self):
        self.assertEqual(7, len(self.tree))

    def testIndex(self):
        self.assertEqual(3, self.tree.index(7))
        self.assertEqual(6, self.tree.index(15))

    def testCount(self):
        self.assertEqual(1, self.tree.count(10))
        self.assertEqual(0, self.tree.count(3))


if __name__ == '__main__':
    unittest.main()
