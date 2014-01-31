from setuptools import setup

def read_file(filename):
    try:
        f = open(filename)
        return f.read()
    finally:
        f.close()


setup(
    name='moarjson',
    version='0.2.1',
    url='https://github.com/Bulv1ne/Moarjson',
    license='MIT',
    author='Niels Lemmens',
    author_email='draso.odin@gmail.com',
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
