.. moarjson documentation master file, created by
   sphinx-quickstart on Fri Jan 31 13:40:49 2014.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to moarjson's documentation!
====================================

Contents:

.. toctree::
   :maxdepth: 2


Install
-------

Simply install *moarjson* with ``pip``::

   pip install moarjson

or ``easy_install``::

   easy_install moarjson

Basic usage
-----------

Use *moarjson* just like you would use json::

   import moarjson as json

   json.dumps('Some string')


Add types to encode into json::

   from datetime import datetime

   json.dumps(datetime.now()) # Fails

   # Tell json to convert datetime objects to str first
   json.register(datetime, str)

   json.dumps(datetime.now()) # Success


Use register as a decorator::

   @json.register(datetime)
   def convert_datetime(obj):
       return obj.strftime(format='%Y-%m-%d %H:%M')



Contribution
------------

The code is valid if it passes **flake8**.
Imports are sorted with **isort**.

For testing **py.test** is used.


.. Indices and tables
.. ==================

.. * :ref:`genindex`
.. * :ref:`modindex`
.. * :ref:`search`

