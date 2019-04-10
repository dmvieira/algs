import unittest
from test.sort import CommonSort
from src.sort.radix import RadixSort

class TestRadixSort(unittest.TestCase, CommonSort):

    sort_alg = RadixSort