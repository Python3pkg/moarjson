import os
import sys

from setuptools import setup
from setuptools.command.test import test as TestCommand


def read_file(filename):
    with open(os.path.join(os.path.dirname(__file__), filename)) as f:
        return f.read()


class PyTest(TestCommand):

    def finalize_options(self):
        TestCommand.finalize_options(self)
        self.test_args = []
        self.test_suite = True

    def run_tests(self):
        #import here, cause outside the eggs aren't loaded
        import pytest
        errno = pytest.main(self.test_args)
        sys.exit(errno)


setup(
    name='moarjson',
    version='0.3.4',
    url='https://github.com/Bulv1ne/Moarjson',
    license='MIT',
    author='Niels Lemmens',
    author_email='draso.odin@gmail.com',
    tests_require=['pytest'],
    cmdclass={'test': PyTest},
    description='Easily json dump types and classes',
    long_description=read_file('README.md'),
    packages=['moarjson'],
    platforms='any',
    install_requires=[],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ]
)
