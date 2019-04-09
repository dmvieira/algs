import random
from src.sort import MAX_NUMBER_SIZE

class CommonSort(object):

    sort_alg = None

    def test_sort_one_element(self):
        sample = [3]
        expected = [3]
        alg = self.sort_alg(sample.copy())
        self.assertEqual(expected, alg.sort())

    def test_sort_empty_list(self):
        sample = []
        expected = []
        alg = self.sort_alg(sample.copy())
        self.assertEqual(expected, alg.sort())

    def test_sort_list(self):
        sample = [3, 4, 7, 8, 2, 1, 5, 6]
        expected = [1, 2, 3, 4, 5, 6, 7, 8]
        alg = self.sort_alg(sample.copy())
        self.assertEqual(expected, alg.sort())

    def test_already_sort_list(self):
        sample = [1, 2, 3, 4, 5, 6, 7, 8]
        expected = [1, 2, 3, 4, 5, 6, 7, 8]
        alg = self.sort_alg(sample.copy())
        self.assertEqual(expected, alg.sort())

    def test_inverse_sort_list(self):
        sample = [8, 7, 6, 5, 4, 3, 2, 1]
        expected = [1, 2, 3, 4, 5, 6, 7, 8]
        alg = self.sort_alg(sample.copy())
        self.assertEqual(expected, alg.sort())

    def test_random_numbers(self):

        sample = []

        for i in range(0,1000):
            x = random.randint(1, MAX_NUMBER_SIZE)
            sample.append(x)
        
        alg = self.sort_alg(sample.copy())
        self.assertEqual(sorted(sample), alg.sort())