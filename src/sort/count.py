from src.sort import Sort, MAX_NUMBER_SIZE
import copy

class CountSort(Sort):
    
    def sort(self, count_size=MAX_NUMBER_SIZE+1, exp=1, division=MAX_NUMBER_SIZE+1):

        if len(self.sample) == 0:
            return self.sample

        count_list = [0]*count_size

        sample = copy.deepcopy(self.sample)
        for element in self.sample:
            count_list[int(element/exp%division)] += 1
        
        for key, counter in enumerate(count_list):
            if key > 0:
                count_list[key] += count_list[key-1]
        
        for element in reversed(self.sample):
            index = count_list[int(element/exp%division)] - 1
            sample.pop(index)
            sample.insert(index, element)
            count_list[int(element/exp%division)] -= 1
        
        return sample