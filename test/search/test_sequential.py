import unittest
from test.search import CommonSearch
from src.search.sequential import SequentialSearch

class TestSequentialSearch(unittest.TestCase, CommonSearch):

    search_alg = SequentialSearch