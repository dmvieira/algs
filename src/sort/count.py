from src.sort import Sort, MAX_NUMBER_SIZE
import copy

class CountSort(Sort):
    
    def sort(self):

        if len(self.sample) == 0:
            return self.sample

        count_list = [0]*(MAX_NUMBER_SIZE + 1)

        sample = copy.deepcopy(self.sample)
        for element in self.sample:
            count_list[element] += 1
        
        for key, counter in enumerate(count_list):
            if key > 0:
                count_list[key] += count_list[key-1]
        
        for element in self.sample:
            index = count_list[element] - 1
            sample.pop(index)
            sample.insert(index, element)
            count_list[element] -= 1

        return sample