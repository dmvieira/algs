import copy
from src.sort import Sort, MAX_NUMBER_SIZE
from src.sort.count import CountSort

class RadixSort(Sort):
    
    def sort(self, count_size=None):

        if len(self.sample) < 2:
            return self.sample
        exp = 1
        count_size = count_size or max(self.sample)
        numbers = len(str(count_size))
        sample = copy.deepcopy(self.sample) 
        while numbers > 0:
            count = CountSort(sample)
            sample = count.sort(count_size+1, exp, 10)
            exp *= 10
            numbers -= 1
        return sample

        
