"""Python CLI for Microsoft SQL."""
# Copyright (C) 2016 Russell Troxel

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

import io

from os import path

import mssqlcli

from setuptools import setup

here = path.abspath(path.dirname(__file__))


def read(*filenames, **kwargs):
    """
    Read file contents into string.

    Used by setup.py to concatenate long_description.

    :param string filenames: Files to be read and concatenated.
    :rtype: string

    """
    encoding = kwargs.get('encoding', 'utf-8')
    sep = kwargs.get('sep', '\n')
    buf = []
    for filename in filenames:
        with io.open(filename, encoding=encoding) as f:
            buf.append(f.read())
    return sep.join(buf)


def long_description():
    long_description = ('Python CLI for Microsoft SQL.'),
    for readme_path in ["README.rst", "README.txt"]:
        if path.exists(readme_path):
            return read(readme_path)
    return long_description


setup(
    name='mssqlcli',
    version=mssqlcli.__version__,
    description=('Python CLI for Microsoft SQL.'),
    long_description=long_description(),

    # The project's main homepage.
    url='https://github.com/rtrox/mssqlcli',

    # Author details
    author='Russell Troxel',
    author_email='russelltroxel@gmail.com',
    license='GPLv3',
    classifiers=[
        'Development Status :: 4 - Beta',

        'Intended Audience :: System Administrators',

        'Topic :: Database :: Front-Ends',

        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',

        'Operating System :: MacOS :: MacOS X',
        'Operating System :: Unix',
        'Operating System :: POSIX',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.5'
    ],

    keywords=['microsoft', 'sql', 'mssql'],

    packages=['mssqlcli'],
    package_dir={
        'msssqlcli': 'mssqlcli'
    },

    install_requires=[
        'pymssql',
        'PyYAML',
        'pygments',
        'click',
        'keyring',
        'prettytable'
    ],

    entry_points={
        'console_scripts': [
            'mssqlcli=mssqlcli.cli:cli',
        ],
    },
)
