#!/usr/bin/env python

# Landsat Util
# License: CC0 1.0 Universal

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

from landsat_util import __version__


def readme():
    with open('README.rst') as f:
        return f.read()

test_requirements = [
  'nose>=1.3.7',
  'mock>=1.3.0'
]

setup(
    name='landsat-util',
    version=__version__,
    description='A utility to search, download and process Landsat 8' +
    ' satellite imagery',
    long_description=readme(),
    author='Development Seed, icooke',
    author_email='icooke@ags.io',
    scripts=['bin/landsat_util'],
    url='https://github.com/ircwaves/landsat-util',
    packages=['landsat_util'],
    include_package_data=True,
    license='CCO',
    platforms='Posix; MacOS X; Windows',
    install_requires=[
        'requests==2.2.0',
        'python-dateutil>=1.5.0',
        'numpy>=1.8',
        'termcolor>=1.1.0',
        'rasterio>=0.26.0',
        'six==1.9.0',
        'homura>=0.1.2',
        'boto>=2.38.0'
    ],
    test_suite='nose.collector',
    test_require=test_requirements
)
