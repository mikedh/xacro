#!/usr/bin/env python
import os
from setuptools import setup

# load __version__
version_file = 'xacro/version.py'
exec(open(version_file).read())

# load README.md as long_description
try:
    with open('README.md', 'r') as f:
        long_description = f.read()
except BaseException:
    long_description = ''

# call the setuptools setup
setup(name='xacro',
      version=__version__,
      description='Xacro is an XML macro languaged, used in ROS',
      long_description=long_description,
      long_description_content_type='text/markdown',
      author='',
      author_email='',
      license='',
      url='http://github.com/mikedh/xacro',
      keywords='robotics XML macro',
      classifiers=[
          'Development Status :: 4 - Beta',
          'License :: OSI Approved :: MIT License',
          'Programming Language :: Python',
          'Programming Language :: Python :: 2.7',
          'Programming Language :: Python :: 3.3',
          'Programming Language :: Python :: 3.4',
          'Programming Language :: Python :: 3.5',
          'Programming Language :: Python :: 3.6',
          'Programming Language :: Python :: 3.7',
          'Natural Language :: English',
          'Topic :: Scientific/Engineering'],
      packages=['xacro'],
      scripts=['scripts/xacro']
      )
