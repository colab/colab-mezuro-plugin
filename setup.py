#!/usr/bin/env python
"""
colab-mezuro plugin
===================

A Mezuro plugin for Colab.
"""
from setuptools import setup, find_packages

install_requires = [
    'colab',
    'kalibro_client==1.3.0.1',
]

tests_require = [
    'mock',
    'kalibro_client==1.3.0.1',
]


setup(
    name="colab-mezuro",
    version='0.1.4',
    author='Rafael Manzo',
    author_email='rr.manzo@gmail.com',
    url='https://github.com/colab/colab-mezuro-plugin',
    description='A Mezuro plugin for Colab',
    long_description=__doc__,
    license='GPLv3',
    package_dir={'': 'src'},
    packages=find_packages('src'),
    zip_safe=False,
    install_requires=install_requires,
    test_suite="tests.runtests.run",
    tests_require=tests_require,
    extras_require={'test': tests_require},
    include_package_data=True,
    classifiers=[
        'Framework :: Django',
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'Operating System :: OS Independent',
        'Topic :: Software Development'
    ],
)
