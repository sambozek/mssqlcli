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

from setuptools import setup

import io

from os import path

import mssqlcli

here = path.abspath(path.dirname(__file__))


def read(*filenames, **kwargs):
    encoding = kwargs.get('encoding', 'utf-8')
    sep = kwargs.get('sep', '\n')
    buf = []
    for filename in filenames:
        with io.open(filename, encoding=encoding) as f:
            buf.append(f.read())
    return sep.join(buf)

setup(
    name='mssqlcli
    version=mssqlcli.__version__,
    description=('Set Supernova Creds based on customer'
                 'information. (DDI&Region or UUID)'),
    long_description=read('README.md'),

    # The project's main homepage.
    url='https://github.rackspace.com/devnull/settemp',

    # Author details
    author='Russell Troxel',
    author_email='russelltroxel@gmail.com',
    license='GPLv3',
    classifiers=[
        'Development Status :: 4 - Beta',

        'Intended Audience :: Administrators',
        'Topic :: Applications :: Supportability',

        'License :: OSI Approved :: GNU General Public License v3.0',

        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.5'
    ],

    keywords=['microsoft', 'sql', 'mssql'],

    packages=["mssqlcli"],
    package_dir={
        "msssqlcli": "mssqlcli"
    },

    install_requires=[
        'pymssql',
        'PyYAML',
        'pygments',
        'click'
    ],

    entry_points={
        'console_scripts': [
            'mssqlcli=mssqlcli.cli:cli',
        ],
    },
)
