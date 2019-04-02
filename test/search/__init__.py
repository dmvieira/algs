import random
from src.search import NOT_FOUND

class CommonSearch(object):

    search_alg = None

    def test_search_one_element(self):
        sample = [3]
        expected = 0
        alg = self.search_alg(sample.copy())
        self.assertEqual(expected, alg.search(3))

    def test_search_empty_list(self):
        sample = []
        expected = NOT_FOUND
        alg = self.search_alg(sample.copy())
        self.assertEqual(expected, alg.search(3))

    def test_search_list(self):
        sample = [1, 2, 3, 4, 5, 6, 7, 8]
        expected = 2
        alg = self.search_alg(sample.copy())
        self.assertEqual(expected, alg.search(3))

    def test_search_list_couple(self):
        sample = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        expected = 2
        alg = self.search_alg(sample.copy())
        self.assertEqual(expected, alg.search(3))

    def test_search_list_unsequential(self):
        sample = [1, 3, 5, 6, 9]
        expected = 1
        alg = self.search_alg(sample.copy())
        self.assertEqual(expected, alg.search(3))

    def test_search_list_random(self):
        sample = []

        for i in range(0,1000):
            x = random.randint(1,1000)
            sample.append(x)
            expected = x
        
        sample = sorted(sample)
        indices = [i for i, x in enumerate(sample) if x == expected]
        alg = self.search_alg(sample.copy())
        self.assertIn(alg.search(expected), indices)
