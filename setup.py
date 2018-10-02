# -*- coding: utf-8 -*-

# Learn more: https://github.com/kennethreitz/setup.py

from setuptools import setup, find_packages

setup(
    name='lottery_bill_generator',
    version='0.1.0',
    description='Package to generate lottery bills with names.',
    author='Juan Ignacio Ubeira',
    author_email='ji.ubeira@gmail.com.com',
    url='https://github.com/jubeira/lottery_bill_generator',
    license=license,
    packages=find_packages(exclude=('tests', 'docs'))
)

