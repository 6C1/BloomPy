import sys

from bitarray import bitarray
from mmh3 import hash as h


class BloomFilter(object):

    def __init__(self, m=sys.maxint, k=7):

        # Create underlying array
        self._ar = bitarray(m)
        self._ar.setall(False)
        # Generate k salted hash functions, using murmur
        self._hashes = map(
            lambda i: (                                     # for i from 0 to k-1
                lambda j:                                   # make an anonymous hash function
                    h(str(j)+str(i*len(str(j))%(i+1))) % m  # seeded based on i
            ),
            xrange(k),
        )
        # Set up counter
        self.len = 0

    def store(self, x):
        """Store arbitrary data"""
        for f in self._hashes: self._ar[f(x)] = True
        self.len += 1

    def wipe(self):
        """Zero all data"""
        self._ar.setall(False)
        self.len = 0

    def collisions(self):
        """Approximate number of collisions"""
        return self.len - self._ar.count()

    def __contains__(self, item):

        # Check that hash of item
        # is present for all hashes
        missing_hashes = filter(
            lambda i: not self._ar[i], 
            [ f(item) for f in self._hashes ],
        )

        return not bool(missing_hashes)

    def __len__(self):
        return self.len
