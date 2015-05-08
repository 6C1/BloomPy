try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'name' : 'BloomPy',
    'description' : 'A quick, simple bloom filter',
    'version' : '0.1.0',
    'author' : 'Cooper Stimson',
    'author_email' : 'cooper@cooperstimson.com',
    'url' : 'https://github.com/6C1/BloomPy',
    'packages' : ['bloompy'],
    'install_requires': ['nose','bitarray'],
    'license' : 'The MIT License',
}

setup(**config)
