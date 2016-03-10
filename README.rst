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


Download sample video::

    wget http://download.blender.org/peach/bigbuckbunny_movies/BigBuckBunny_320x180.mp4 bunny.mp4


Running the event source backend::

  python event_source.py
  open localhost:8080
