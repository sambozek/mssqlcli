"""Jsonification Functions for python-mssqlclient."""
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

import csv
import json
import datetime

import StringIO


def stringify(obj):
    if type(obj) == list:
        iterable = enumerate(obj)
    if type(obj) == dict:
        iterable = obj.items()
    for k, v in iterable:
        if type(v) == datetime.datetime:
            obj[k] = str(v)
        if type(v) in [list, dict]:
            obj[k] = stringify(v)
    return obj


def jsonify(obj):
    formatted_json = json.dumps(stringify(obj), indent=4)

    try:
        from pygments import highlight, lexers, formatters
        colorful_json = highlight(
            unicode(formatted_json, 'UTF-8'),
            lexers.JsonLexer(),
            formatters.TerminalFormatter()
        )
    except ImportError:
        return formatted_json

    return colorful_json


def csvify(obj):
    output = StringIO.StringIO()
    fieldnames = obj[0].keys()
    writer = csv.DictWriter(output, fieldnames=fieldnames)

    writer.writeheader()
    for item in stringify(obj):
        writer.writerow(item)
    out = output.getvalue()
    output.close()
    return out



FORMAT_OPTIONS = {
    "csv": csvify,
    "json": jsonify
}
