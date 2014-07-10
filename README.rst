.. _Cayley: http://github.com/google/cayley/
.. _Python: http://python.org/
.. _Requests: http://github.com/kennethreitz/requests
.. _Methods: https://github.com/google/cayley/blob/master/docs/HTTP.md

============================
pycayley: Simple Python Cayley Client
============================

pycayley is a simple Python_ client for Cayley_ Graph Database. It is distributed as a single file module and has only one dependency Requests_ other than the `Python Standard Library <http://docs.python.org/library/>`_.

Homepage and documentation: http://github.com/canerbasaran/pycayley


Example: "Hello World" in a bottle
----------------------------------
./cayley http --dbpath=30kmovies.nt

.. code-block:: python

  from pycayley import CayleyDatabase

  c = CayleyDatabase("http://localhost:64210", "v1")
  c.qg("graph.Vertex().GetLimit(5)")


Run this script or paste it into a Python console, then response JSON results:

.. code-block:: json

  {'result': [{'id': ':100000'},
  {'id': '/film/performance/actor'},
  {'id': ':/en/larry_fine_1902'},
  {'id': ':100001'},
  {'id': ':/en/samuel_howard'}]}


Methods_
-------

- query/gremlin    -> qg
- query/mql        -> qm
- shape/gremlin    -> sg
- shape/mql        -> sm
- write            -> w
- write/file/nquad -> wfn
- delete           -> d


Download and Install
--------------------

.. __: https://github.com/canerbasaran/pycayley/raw/master/pycayley.py

Install with ``sudo python setup.py install`` or download `pycayley.py`__ (unstable) into your project directory. There is only one dependency Requests_ other than the Python standard library. PyCayley runs with **Python 2.5+ and 3.x**.


License
-------

.. __: https://github.com/canerbasaran/pycayley/raw/master/LICENSE

Code and documentation are available according to the MIT License (see LICENSE__).
