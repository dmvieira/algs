import unittest
from test.sort import CommonSort
from src.sort.count import CountSort

class TestCountSort(unittest.TestCase, CommonSort):

    sort_alg = CountSort