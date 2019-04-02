import unittest
from test.search import CommonSearch
from src.search.binary import BinarySearch

class TestBinarySearch(unittest.TestCase, CommonSearch):

    search_alg = BinarySearch