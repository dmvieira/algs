from src.sort import Sort

class QuickSort(Sort):
    
    def sort(self, sample=None):
        sample = self.sample if sample is None else sample
        
        if len(sample) == 0: return []
        
        pivot = sample[-1]

        if len(sample) == 1: return [pivot]
        
        left = []
        right = []
        for i in range(0, len(sample)-1):
            if sample[i] > pivot:
                right.append(sample[i])
            else:
                left.append(sample[i])
        
        l = self.sort(left)
        r = self.sort(right)


        return l + [pivot] + r