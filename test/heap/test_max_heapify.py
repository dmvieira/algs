import unittest
from src.heap.max_heapify import MaxHeapify

class TestMaxHeapify(unittest.TestCase):

    def test_should_heapify_build(self):
        array = [3, 1, 6, 5, 2, 4]

        expected = [6, 5, 4, 1, 2, 3]
        
        heap = MaxHeapify(array)

        self.assertEqual(expected, heap.build())

    def test_should_heapify_once(self):
        array = [3, 1, 6, 5, 2, 4]

        expected = [6, 1, 4, 5, 2, 3]
        
        heap = MaxHeapify(array)

        self.assertEqual(expected, heap.max())