from mmh3 import hash as h
from sys import maxint
from bitarray import bitarray

class BloomFilter(object):
    def __init__(self,m=maxint,k=7):
        # Create underlying array
        self._ar = bitarray(m)
        self._ar.setall(False)
        # Generate k salted hash functions, using murmur
        self._hashes = map(lambda i:                            # for i from 0 to k-1
                           (lambda j:                           # make an anonymous hash function
                            h(str(j)+str(i*len(str(j))%(i+1))) % m), # seeded based on i
                           xrange(k))
        # Set up counter
        self.len = 0

    # Store arbitrary data
    def store(self, x):
        for f in self._hashes: self._ar[f(x)] = True
        self.len += 1
    # Zero all data
    def wipe(self):
        self._ar.setall(False)
        self.len = 0
    # Approximate number of collisions
    def collisions(self):
        return self.len - self._ar.count()
    # Implementing membership test operations
    def __contains__(self, item):
        return filter(lambda i: not self._ar[i], [ f(item) for f in self._hashes])==[]
    # Implementing builtin function len()
    def __len__(self): return self.len
