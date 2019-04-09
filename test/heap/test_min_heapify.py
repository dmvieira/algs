import unittest
from src.heap.min_heapify import MinHeapify

class TestMinHeapify(unittest.TestCase):

    def test_should_heapify_build(self):
        array = [3, 1, 6, 5, 2, 4]

        expected = [1, 2, 4, 5, 3, 6]
        
        heap = MinHeapify(array)

        self.assertEqual(expected, heap.build())

    def test_should_heapify_once(self):
        array = [3, 1, 6, 5, 2, 4]

        expected = [1, 2, 6, 5, 3, 4]
        
        heap = MinHeapify(array)

        self.assertEqual(expected, heap.min())