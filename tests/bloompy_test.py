from nose import *
from bloompy.bloom import *
from random import choice as rc
from string import printable as ascii
from string import digits

def basic_test():
    k = 16180
    
    b = BloomFilter()
    for i in xrange(k):
        s = "".join([rc(ascii) for j in xrange(64)])
        b.store(s)
        assert s in b

def int_test():
    k = 16180
    
    b = BloomFilter()
    for i in xrange(k):
        s = int("".join([rc(digits) for j in xrange(64)]))
        b.store(s)
        assert s in b
    
