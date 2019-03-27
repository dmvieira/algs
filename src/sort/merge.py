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
            stage = last_a = last_b = 0
            k = i = j = 0
            while len(a) > i and len(b) > j:
                curr_a = a[i]
                curr_b = b[j]
            
                if curr_a < curr_b or len(b) <= j:
                    sample[k] = curr_a
                    i += 1
                else:
                    sample[k] = curr_b
                    j += 1
                k += 1
                
            return sample[:k] + a[i:] + b[j:]


        