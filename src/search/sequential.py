from src.search import Search, NOT_FOUND

class SequentialSearch(Search):

    def search(self, element):

        for i, el in enumerate(self.sample):
            if el == element:
                return i
            
        return NOT_FOUND
