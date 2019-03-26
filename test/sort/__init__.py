
class CommonSort(object):

    sort_alg = None

    def test_sort_list(self):
        sample = [3, 4, 7, 8, 2, 1, 5, 6]
        expected = [1, 2, 3, 4, 5, 6, 7, 8]
        alg = self.sort_alg(sample)
        self.assertEqual(expected, alg.sort())