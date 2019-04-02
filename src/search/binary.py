from src.search import Search, NOT_FOUND
from math import floor

class BinarySearch(Search):

    def search(self, element, pivot_left=None, pivot_right=None):

        pivot_right = pivot_right or len(self.sample)
        pivot_left = 0 if pivot_left is None else pivot_left


        if pivot_left < pivot_right:        
            pivot = pivot_left + floor((pivot_right - pivot_left) / 2)
            
            if self.sample[pivot] == element:
                return pivot
            elif self.sample[pivot] > element:
                return self.search(element, pivot_left, pivot)
            elif self.sample[pivot] < element:
                return self.search(element, pivot, pivot_right)

        else:
            return NOT_FOUND
        