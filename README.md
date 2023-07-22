# Redamp_assignment

CLI application for processing IOC and storing it in a database.

## Instructions to run the application

For running application you need to have python3 installed on your system.
To install required dependencies in environment, run script:

```
./setup_project.sh
```

Application has following usage:

```
python3 app.py <url> <delimiter> <ioc_index>"
```

e.g.:

```
python3 app.py 'https://openphish.com/feed.txt' '' 0
python3 app.py 'https://urlhaus.abuse.ch/downloads/csv_recent/' ',' 2
python3 app.py 'http://reputation.alienvault.com/reputation.data' '#' 0

```

## Instructions to run the tests

To run the tests, run following command:

```
python3 tests/tests.py
```

If you get error with paths, try running following command:

```
export PYTHONPATH=.
```
