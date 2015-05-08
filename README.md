# BloomPy

BloomPy is a simple [bloom filter](http://en.wikipedia.org/wiki/Bloom_filter) implementation. A bloom filter is an efficient way to track and test for set membership. It is a probabilistic data structure, with a nonzero false positive rate and a strictly zero false negative rate.

## How it works

A bloom filter contains an array of `m` bits, zero-initialized, along with `k` hash functions, mapping data onto the integers `(0,1,...,m-1)`. When a piece of data is stored in the bloom filter, it is run through each of the hash functions, and the bit in the bloom filter's array corresponding to the result of each hash function is set to 1. To check if a piece of data is in the bloom filter, it is again run through each of the hash functions, and the corresponding array elements are checked; if any are zero, then the data is not in the bloom filter.

BloomPy uses [Murmur](http://code.google.com/p/smhasher/) for hashing, with many thanks to Austin Appleby and Hajime Senuma.

## Installation

Clone this repository and run `sudo python setup.py install`. (Skip the `sudo` if you're on Windows.)

    git clone git@github.com:6C1/BloomPy.git
    cd BloomPy
    sudo python setup.py install

## Usage

BloomPy is just one class: `BloomFilter`.

Make a bloom filter, or make one specifying `m`, or `k`, or both:

    b = BloomFilter()
    c = BloomFilter(8675309)
    d = BloomFilter(k=7)
    e = BloomFilter(867530,9)

Add some data to the bloom filter:

    b.store(moby_dick.text)
    b.store("The cake is a Lie algebra")

And verify its membership:

    assert moby_dick.text in b
    assert "The cake is a Lie algebra" in b
    assert "Cheep cheep cheep!" not in b

Wipe it clean to start over:

    b.wipe()

## License

This is licensed under the MIT license, both in the LICENSE file in this directory and, hey look! Here's a copy as well.

    The MIT License (MIT)

    Copyright (c) 2015 Cooper Stimson
    
    Permission is hereby granted, free of charge, to any person obtaining a copy
    of this software and associated documentation files (the "Software"), to deal
    in the Software without restriction, including without limitation the rights
    to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
    copies of the Software, and to permit persons to whom the Software is
    furnished to do so, subject to the following conditions:

    The above copyright notice and this permission notice shall be included in
    all copies or substantial portions of the Software.

    THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
    IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
    FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
    AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
    LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
    OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
    THE SOFTWARE.
