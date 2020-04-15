# ESPN Testing With Pytest-bdd

## Setup
It must mandatory use Python3 to run this project.

[Firefox](https://www.mozilla.org/es-ES/firefox/new/) must be installed and 
[Geckodriver](https://github.com/mozilla/geckodriver/releases) downloaded and added to the system path

The packages are manage with [pipenv](https://pipenv.readthedocs.io/).
Clone the current repo and run `pipenv install` from the command line in the project's root directory.

## Running Tests
Run full tests with `python -m pytest`.
If you prefer to run an specific test you can filter using tags, e.g. `python -m pytest -k "login"`