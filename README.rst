.. _Cayley: http://github.com/google/cayley/
.. _Python: http://python.org/
.. _Requests: http://github.com/kennethreitz/requests
.. _Methods: http://github.com/google/cayley/blob/master/docs/HTTP.md

.. image:: https://github.com/canerbasaran/pycayley/raw/master/pycayley.png?raw=true

============================
pycayley: Simple Python Cayley Client
============================

pycayley is a simple Python_ client for Cayley_ Graph Database. It is distributed as a single file module and has only one dependency Requests_ other than the `Python Standard Library <http://docs.python.org/library/>`_.

Homepage and documentation: http://github.com/canerbasaran/pycayley


Example
-------
./cayley http --dbpath=30kmovies.nt

**Get the list of actors in the film**

.. code-block:: python

  from pycayley import Graph

  c = Graph("http://localhost:64210", "v1")
  c.qg('g.V().Has("name","Casablanca").Out("/film/film/starring").Out("/film/performance/actor").Out("name").All()')


Run this script or paste it into a Python console, then response JSON results:

.. code-block:: json

  {u'result': [{u'id': u'Humphrey Bogart'},
  {u'id': u'Ingrid Bergman'},
  {u'id': u'Paul Henreid'},
  {u'id': u'Claude Rains'},
  {u'id': u'Conrad Veidt'},
  {u'id': u'Sydney Greenstreet'},
  {u'id': u'Peter Lorre'},
  {u'id': u'S.Z. Sakall'},
  {u'id': u'Madeleine LeBeau'},
  {u'id': u'Dooley Wilson'},
  {u'id': u'Joy Page'},
  {u'id': u'John Qualen'},
  {u'id': u'Leonid Kinskey'},
  {u'id': u'Helmut Dantine'},
  {u'id': u'Lou Marcelle'}]}


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
