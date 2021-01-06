import random
from functools import lru_cache

class LazyLoader:
    def __init__(self):
        pass
    
    @lru_cache(maxsize=None)
    def idx_to_data(self, idx):
        raise NotImplementedError
        
    def to_stream(self, batch_size=1):
        raise NotImplementedError


class Cipher(LazyLoader):
    def __init__(self):
        self.offset = random.randint(0, 25)
        
    def idx_to_data(self, idx):
        alpha_idx = (idx + self.offset) % 26
        return chr(ord('A') + alpha_idx)
    
    def to_stream(self, batch_size=4):
        counter = 0
        while True:
            batch = []
            for _ in range(batch_size):
                data = self.idx_to_data(counter)
                counter += 1
                batch.append(data)
            yield batch