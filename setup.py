from setuptools import setup, Command

import os

import losito._version

description = 'The LOFAR Simulation Tool'
long_description = description
if os.path.exists('README.md'):
    with open('README.md') as f:
        long_description=f.read()

setup(
    name='LoSiTo',
    version=losito._version.__version__,
    url='http://github.com/darafferty/losito/',
    author='David Rafferty and Herik Edler',
    description=description,
    long_description=long_description,
    platforms='any',
    classifiers = [
        'Programming Language :: Python',
        'Development Status :: Stable',
        'Natural Language :: English',
        'Intended Audience :: Science/Research',
        'Operating System :: POSIX :: Linux',
        'Topic :: Scientific/Engineering :: Astronomy',
        'Topic :: Software Development :: Libraries :: Python Modules',
        ],
    python_requires='>3.6.0',
    install_requires=['numpy', 'scipy', 'astropy', 'RMextract'],
    scripts = ['bin/losito', 'bin/skymodel', 'bin/synthms', 'bin/tecscreen'],
    packages=['losito','losito.operations'],
    package_data={'losito': ['./data/*','./data/*/*','./data/*/*/*','./data/*/*/*/*']},
    include_package_data=True
    )
