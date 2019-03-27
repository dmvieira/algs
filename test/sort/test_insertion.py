import unittest
from test.sort import CommonSort
from src.sort.insertion import InsertionSort

class TestInsertionSort(unittest.TestCase, CommonSort):

    sort_alg = InsertionSort