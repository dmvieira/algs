from src.sort import Sort

class MergeSort(Sort):
    
    def sort(self, sample=None):
        sample = sample or self.sample
        size = len(sample)
        if size == 1:
            return sample
        else:
            pivot = int(size/2)
            a = self.sort(sample[:pivot])
            b = self.sort(sample[pivot:])
            print(a, b)
            if a > b:
                return b+a
            else:
                return a+b
                


        