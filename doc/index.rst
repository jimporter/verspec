inversion Documentation
=======================

**inversion** is a Python library for handling software versions and specifiers,
adapted from the `packaging`_ package.

Installation
------------

You can install inversion with ``pip``:

.. code-block:: console

    $ pip install inversion


An Example
----------

.. doctest::

   >>> from inversion import python
   >>> v1 = python.Version('1.0')
   >>> s1 = python.SpecifierSet('~=1.0')
   >>> v1 in s1
   True

   >>> from inversion import loose
   >>> v2 = loose.Version('1.0')
   >>> s2 = loose.SpecifierSet('>=1.0')
   >>> v2 in s2
   True

API
---

.. toctree::
    :maxdepth: 3

    version
    specifiers

Credits
-------

The real credit for this package goes to the `Python Packaging Authority`_.


.. _packaging: https://github.com/pypa/packaging
.. _Python Packaging Authority: https://www.pypa.io/
