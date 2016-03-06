XXX
===

Requirements
~~~~~~~~~~~~

Requires Python 3.4+

Usage
~~~~~

Setup::

  pyvenv env
  source env/bin/activate
  pip install -r requirements.txt


Running the event source backend::

  python event_source.py


Serving the example page::

  python -m SimpleHTTPServer 8080
  open localhost:8080
