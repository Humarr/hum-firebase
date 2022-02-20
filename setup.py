#!/usr/bin/env python
import os

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

with open(os.path.join(os.path.dirname(__file__), 'README.rst')) as readme:
    long_description = readme.read()


setup(name='hum-firebase',
      version='1.2.1',
      description="Python interface to the Firebase's REST API.",
      long_description=long_description,
      classifiers=[
          'Development Status :: 5 - Production/Stable',
          'Environment :: Console',
          'Intended Audience :: Developers',
          'License :: OSI Approved :: MIT License',
          'Operating System :: OS Independent',
        #   'Programming Language :: Python :: 2.6',
        #   'Programming Language :: Python :: 2.7',
          'Programming Language :: Python :: 3',
          'Natural Language :: English',
      ],
      keywords='hum-firebase',
      author='Umar',
      author_email='ozgurvt@gmail.com',
      maintainer='Umar',
      maintainer_email='saaduumar42@gmail.com',
      url='https://github.com/Humarr/hum-firebase/',
    #   license='MIT',
      packages=['firebase'],
    #   test_suite='tests.all_tests',
      install_requires=['requests>=1.1.0'],
      zip_safe=False,
      )
