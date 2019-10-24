#!/usr/bin/env python3
# coding=utf-8

from setuptools import setup, find_packages

setup(
    name='fengyong',
    version='1.3.0',
    description=(
        'Run MIPS with python!'
    ),
    long_description=open('README.rst').read(),
    author='CQU-AI',
    author_email='peter@mail.loopy.tech',
    maintainer='loopyme',
    maintainer_email='peter@mail.loopy.tech',
    license='MIT License',
    packages=find_packages(),
    platforms=["all"],
    url='https://github.com/CQU-AI/pymips',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Operating System :: OS Independent',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: Implementation',
        'Programming Language :: Python :: 3.6',
        'Topic :: Software Development :: Libraries'
    ],
    entry_points={
        'console_scripts': [
            'mips-shell=fengyong:Simulator.run_shell',
        ]
    }
)
