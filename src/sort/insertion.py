from src.sort import Sort

class InsertionSort(Sort):
    
    def sort(self):
        sample = self.sample
        safe = -1
        for i in range(1, len(sample)):
            k = i
            j = k - 1
            while sample[k] < sample[j] and j > safe:
                tmp = sample[j]
                sample[j] = sample[k]
                sample[k] = tmp
                k -= 1
                j -= 1
        return sample

        