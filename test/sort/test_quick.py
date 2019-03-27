import unittest
from test.sort import CommonSort
from src.sort.quick import QuickSort

class TestQuickSort(unittest.TestCase, CommonSort):

    sort_alg = QuickSort