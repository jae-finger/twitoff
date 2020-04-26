# App: twitoff
Author: Jonathan Finger

## Installation

TODO instructions for git clone

## Setup

TODO instructions for virtual environment

## Usage


```sh
# Mac:
FLASK_APP=web_app flask run

# Windows:
# ? Export FLASK_APP=hello.py # one time set of environmental variable
# ? flask run
```

Also setup a database:

```sh
FLASK_APP=web_app flask db init
FLASK_APP=web_app flask db migrate
FLASK_APP=web_app flask db upgrade
```