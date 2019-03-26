import unittest
from test.sort import CommonSort
from src.sort.merge import MergeSort

class TestMergeSort(unittest.TestCase, CommonSort):

    sort_alg = MergeSort