Marketplace using DRF
=======================================

It's a project using DRF to provides some resources to real state marketplace. All documentation about the resources its available in development mode or here:
http://www.mypy-lang.org/

Requirements
------------

You need Python >= 3.6 or later to run the app.  You can have multiple Python
versions (2.x and 3.x) installed on the same system without problems.

In Ubuntu, Mint and Debian you can install Python 3 like this:

    $ sudo apt-get install python3 python3-pip

For other Linux flavors, OS X and Windows, packages are available at

  http://www.python.org/getit/


Quick start
-----------

Create your env using virtualenv:

    $ virtualenv venv -p python3

Activate your env:

    $ source venv/bin/activate


Now, you should install development dependencies using pip:

    $ pip install -r requirements_dev.txt

Run migrations:

    $ python manage.py migrate
    
Run server in development mode:

    $ python manage.py runserver

Import fixtures
-----

To import fixtures in project:

    $ python manage.py import_data ./fixtures/data.csv
    $ pytest -v

Tests
-----

The basic way to run tests:

    $ pip install -r requirements_test.txt
    $ pytest -v
