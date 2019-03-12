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

class IndexableNode(BinaryTree):

    def _search(self, count, index):
        pass
        # Returns (found, count)

    def __get_item__(self, index):
        found, _ = self._search(0, index)
        if not found:
            raise IndexError('Index ({}) out of range'.format(index))
        return found.value

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
        self.assertEqual(0, self.tree[0])


if __name__ == '__main__':
    unittest.main()
