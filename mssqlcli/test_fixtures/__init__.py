"""Testing Fixtures for MSSQL-CLI."""
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

import os

from datetime import datetime

FIXTURES_PATH = os.path.dirname(os.path.realpath(__file__))


def get_file_contents(filename):
    filepath = os.path.join(FIXTURES_PATH, filename)
    with open(filepath, 'r') as f:
        return f.read()


def populate_isolated_filesystem(configfile, queryfile):
    with open('config.yml', 'w') as f:
        f.write(get_file_contents(configfile))
    with open('query.sql', 'w') as f:
        f.write(get_file_contents(queryfile))


class MockPyMSSQLCursor(object):

    def __init__(self, as_dict=False):
        self.as_dict = as_dict
        self.results = []

    def __iter__(self):
        return iter(self.results)

    def execute(self, query):
        self.results = [
            {"a": "one", "b": "two"},
            {"a": "three", "b": datetime(2016, 10, 20, 21, 10, 36, 621341)}
        ]


class MockPyMSSQLConnection(object):

    def __init__(self, server, username, password):
        self.server = server
        self.username = username
        self.password = password

    def cursor(self, as_dict=False):
        return MockPyMSSQLCursor(as_dict)
