# MS-SQL Command Line Interface (mssqlcli)

MS-SQL CLI is a unix command line tool for accessing and running arbitrary
queries against an Microsoft SQL database.


## Binary Dependencies

- [FreeTDS][1] - Binary Library providing access to MSSQL and Sybase DBs.



## Installation
1. Install the FreeTDS Library
    - Debian/Ubuntu: `sudo apt-get install freetds-dev`
    - Mac OSX: `brew install freetds`
2. Clone this repo locally
3. Install client `python setup.py install`



## Configuration

Configuration is handled with a single YAML configuration file, located by
default at `~/.config/mssqlcli.yml`.

Example Config:
```yaml
keyring_app_name: another_app # Optional, defaults to mssqlcli
username: USE_KEYRING("global:LDAPUser")
password: USE_KEYRING("global:LDAP")
# OR
# username: my_plaintext_username
# password: my_plaintext_password
server: MY_MSSQL.example.com

# The below is optional, and should be used if
# Windows Auth will be used instead of MSSQL Auth.
windows_authentication: true
domain: MY_DOMAIN
```


## Usage
The general usage model is to store your SQL queries in flat files, and
access them with the CLI client. Personally, I store my queries in
~/sql_queries.

From here, you can simply running your queries through the CLI:
```
~ [ mssqlcli --help Usage: mssqlcli [OPTIONS] COMMAND [ARGS]...

Options:
  --help  Show this message and exit.

Commands:
  query
~ [ mssqlcli query --help
Usage: mssqlcli query [OPTIONS] QUERY

Options:
  -o, --output [json|csv]
  -c, --config-file PATH   Config File for use with client. (default:
                           ~/.config/pymssql.yml)
  --help                   Show this message and exit.
  ```

## Examples

Run Query and return results as a json blob
```mssqlcli query {path to query}.sql```

Run query and return results in CSV format
```mssqlcli query -o csv {path to query}.sql```

Redirect csv to File
```mssqlcli query -o csv {path to query}.sql > results.csv```

[1]: http://www.freetds.org/
[2]: http://pymssql.org/en/stable/
[3]: http://click.pocoo.org/5/
