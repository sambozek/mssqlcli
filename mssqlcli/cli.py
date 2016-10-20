"""MSSQL Cli Client written in python."""
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
import click
import pymssql
from config import Config

import formats


@click.group()
def cli():
    pass


@click.option("--config-file", "-c", type=click.Path(),
              default=os.path.expanduser("~/.config/mssqlcli.yml"),
              help=("Config File for use with client."
                    " (default: ~/.config/pymssql.yml)"))
@click.option("--output", "-o",
              type=click.Choice(formats.FORMAT_OPTIONS.keys()),
              default="json")
@click.argument("query", type=click.File('r'))
@cli.command()
def query(config_file, output, query):
    query = query.read()
    config = Config(config_file)
    conn = pymssql.connect(
        config.server,
        config.get_username(),
        config.password
    )
    cursor = conn.cursor(as_dict=True)
    cursor.execute(query)

    results = [row for row in cursor]

    output = formats.FORMAT_OPTIONS[output](results)
    click.echo(output)


if __name__ == "__main__":
    cli()
