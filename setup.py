# -*- coding: utf-8 -*-
# Copyright (c) 2017 Coders Co.
# Licensed under the MIT License (https://opensource.org/licenses/MIT)

from setuptools import setup

setup(
    name='pygmentsrax',
    version='1.0.0',
    description='Rax Lexer for Pygments',
    author='Gosia Wrzesinska, Jan-Mark Wams',
    author_email='gosia@codersco.com',
    license='MIT',
    keywords='syntax highlighting rax',
    url='https://github.com/chosia/pygments-rax',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: End Users/Desktop',
        'Intended Audience :: Developers',
        'Intended Audience :: Education',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Topic :: Text Processing',
        'Topic :: Utilities',
    ],
    packages=['pygmentsrax'],
    install_requires=['Pygments >= 2'],
    include_package_data=False,
    platforms=['any'],
    entry_points={
        'pygments.lexers': [
            'RaxLexer = pygmentsrax:RaxLexer'
        ],
    },
    zip_safe=False
)
