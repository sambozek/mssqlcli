"""Keyring Access for python-mssqlclient."""
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

import keyring
import re
import yaml


class Config(object):
    matcher = re.compile(r'^USE_KEYRING\([\'\"](.*)[\'\"]\)$')

    def __init__(self, config_file):
        with open(config_file, "r") as f:
            self.object = yaml.load(f.read())
        self.object = self.get_from_keyring(self.object)
        self.set_attrs()

    def set_attrs(self):
        for k, v in self.object.items():
            setattr(self, k, v)

    def check_keyring(self, string):
        app_name = self.object.get("keyring_app_name", "mssqlcli")
        match = self.matcher.match(string)
        if match is not None:
            return keyring.get_password(app_name, match.group(1))
        return string

    def get_from_keyring(self, obj):
        if type(obj) == list:
            iterable = enumerate(obj)
        if type(obj) == dict:
            iterable = obj.items()
        for k, v in iterable:
            if type(v) == str:
                obj[k] = self.check_keyring(v)
            if type(v) in [list, dict]:
                obj[k] = self.get_from_keyring(v)
        return obj

    def get_username(self):
        if self.windows_authentication:
            return '\\'.join([self.domain, self.username])
        return self.get_username

    def __dict__(self):
        return self.object
