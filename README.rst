==============================================================================
 Hackathon Django Project
==============================================================================

Requirements
------------

* python >= 2.5
* pip
* django >= 1.4

Installation
------------

Virtualenvwrapper
~~~~~~~~~~~~~~~~~

.. code:: bash

    mkvirtualenv hackathon
    cd $PROJECT_HOME
    # Get the code
    git clone git@github.com:yarbelk/redwire.git redwire
    git submodule init
    git submodule update
    mkdir {db,tmp}


Install the Requirements

.. code:: bash

    cd redwire
    pip install -r requirements.txt

update the activate script to set the correct Django settings module and
PYTHONPATH

.. code:: bash

    # $VIRTUAL_ENV/bin/activate
    ...
    export DJANGO_SETINGS_MODULE="hackathon.config.settings.devel"


Gunicorn/nginx
~~~~~~~~~~~~~~

copy/link the configuration  from `conf.d/etc/nginx/sites-available/redwire.sg`
into the nginx sites-available.  update as needed, reload nginx.

Sync DB
~~~~~~~

.. code:: bash

    ./manage.py syncdb
    ./manage.py migrate --all
