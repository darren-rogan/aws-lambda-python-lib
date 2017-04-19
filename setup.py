import os
import setuptools
import sys

from setuptools import setup

# Set external files
try:
    from pypandoc import convert
    README = convert('README.md', 'rst')	 
except ImportError:
    README = open(os.path.join(os.path.dirname(__file__), 'README.md')).read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='aws_lambda_python_lib',
    version='0.0.1',
    packages=['aws_lambda_python_lib'],
    include_package_data=True,
    license='MIT License',
    description='AWS Lambda Pre-compiled Python Library',
    long_description=README,
    url='https://github.com/liangrog/aws-lambda-python-lib',
    download_url='https://github.com/liangrog/aws-lambda-python-lib/tarball/0.0.1',
    author='Roger Liang',
    author_email='pinguroger@gmail.com',
    classifiers=[
        'Environment :: Console',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
)
