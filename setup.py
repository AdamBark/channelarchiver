#!/usr/bin/env python

from channelarchiver import __version__
from setuptools import setup

setup(
    name='channelarchiver',
    version=__version__,
    description='Python client for the EPICS Channel Archiver.',
    long_description=open('README.md').read(),
    author='Robbie Clarken',
    author_email='robbie.clarken@gmail.com',
    url='https://github.com/RobbieClarken/channelarchiver',
    packages=['channelarchiver'],
    install_requires=[],
    license=open('LICENSE.md').read(),
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Topic :: Scientific/Engineering',
        'Intended Audience :: Developers',
        'Intended Audience :: Science/Research',
        'Natural Language :: English',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'License :: OSI Approved :: MIT License',
    ],
)