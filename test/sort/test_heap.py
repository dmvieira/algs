import unittest
from test.sort import CommonSort
from src.sort.heap import HeapSort

class TestHeapSort(unittest.TestCase, CommonSort):

    sort_alg = HeapSort