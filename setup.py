#!/usr/bin/env python
from setuptools import setup, find_packages

try:
    README = open('README.rst').read()
except:
    README = None

try:
    REQUIREMENTS = open('requirements.txt').read()
except:
    REQUIREMENTS = None

setup(
    name = 'django-portfolio',
    version = "0.1",
    description = 'An artist\'s portfolio as a pluggable Django app.',
    long_description = README,
    install_requires = REQUIREMENTS,
    author = 'Mathijs de Bruin',
    author_email = 'mathijs@mathijsfietst.nl',
    url = 'http://github.com/dokterbob/django-portfolio/',
    packages = find_packages(),
    include_package_data = True,
    classifiers = [
      'Development Status :: 3 - Alpha',
      'Environment :: Web Environment',
      'Framework :: Django',
      'Intended Audience :: Developers',
      'License :: OSI Approved :: GNU Affero General Public License v3 or later (AGPLv3+)',
      'Operating System :: OS Independent',
      'Programming Language :: Python',
      'Topic :: Utilities'
    ],
    test_suite='setuptest.setuptest.SetupTestSuite',
    tests_require=(
        'django-setuptest',
        'argparse',  # apparently needed by django-setuptest on python 2.6
    ),
)
