#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup
import re


with open('after_response/__init__.py', 'r') as init_file:
    version = re.search(
        '^__version__ = [\'"]([^\'"]+)[\'"]',
        init_file.read(),
        re.MULTILINE,
    ).group(1)


setup(
    name='django-after-response',
    description='Simple asynchronous execution',
    url='http://github.com/defrex/django-after-response/',
    license='MIT',
    author='Aron Jones',
    author_email='aron.jones@gmail.com',
    packages=['after_response'],
    version=version,
    install_requires=[
        'Django>=1.5',
    ],
)
