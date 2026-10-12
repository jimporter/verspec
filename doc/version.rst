Version Handling
================

A core requirement of dealing with packages is the ability to work with
versions. `PEP 440`_ defines the standard version scheme for Python packages
which has been implemented by this module.

Usage
-----

.. doctest::

    >>> from verspec.python import PythonVersion
    >>> v1 = PythonVersion("1.0a5")
    >>> v2 = PythonVersion("1.0")
    >>> v1
    <PythonVersion('1.0a5')>
    >>> v2
    <PythonVersion('1.0')>
    >>> v1 < v2
    True
    >>> v1.epoch
    0
    >>> v1.release
    (1, 0)
    >>> v1.pre
    ('a', 5)
    >>> v1.is_prerelease
    True
    >>> v2.is_prerelease
    False
    >>> PythonVersion("french toast")
    Traceback (most recent call last):
        ...
    InvalidVersion: Invalid version: 'french toast'
    >>> PythonVersion("1.0").post
    >>> PythonVersion("1.0").is_postrelease
    False
    >>> PythonVersion("1.0.post0").post
    0
    >>> PythonVersion("1.0.post0").is_postrelease
    True


Reference
---------

Python Versions
^^^^^^^^^^^^^^^

.. currentmodule:: verspec.python

.. class:: PythonVersion(version)

    This class abstracts handling of a project's versions. It implements the
    scheme defined in `PEP 440`_. A :class:`PythonVersion` instance is
    comparison aware and can be compared and sorted using the standard Python
    interfaces.

    :param str version: The string representation of a version which will be
                        parsed and normalized before use.
    :raises InvalidVersion: If the ``version`` does not conform to PEP 440 in
                            any way then this exception will be raised.

    .. attribute:: public

        A string representing the public version portion of this
        :class:`PythonVersion`.

    .. attribute:: base_version

        A string representing the base version of this :class:`PythonVersion`
        instance. The base version is the public version of the project without
        any pre or post release markers.

    .. attribute:: epoch

        An integer giving the version epoch of this :class:`PythonVersion`
        instance

    .. attribute:: release

        A tuple of integers giving the components of the release segment of this
        :class:`PythonVersion` instance; that is, the ``1.2.3`` part of the
        version number, including trailing zeroes but not including the epoch or
        any prerelease/development/postrelease suffixes

    .. attribute:: major

        An integer representing the first item of :attr:`release` or ``0`` if
        unavailable.

    .. attribute:: minor

        An integer representing the second item of :attr:`release` or ``0`` if
        unavailable.

    .. attribute:: micro

        An integer representing the third item of :attr:`release` or ``0`` if
        unavailable.

    .. attribute:: local

        A string representing the local version portion of this
        :class:`PythonVersion` if it has one, or ``None`` otherwise.

    .. attribute:: pre

        If this :class:`PythonVersion` instance represents a prerelease, this
        attribute will be a pair of the prerelease phase (the string ``"a"``,
        ``"b"``, or ``"rc"``) and the prerelease number (an integer). If this
        instance is not a prerelease, the attribute will be `None`.

    .. attribute:: is_prerelease

        A boolean value indicating whether this :class:`PythonVersion` instance
        represents a prerelease and/or development release.

    .. attribute:: dev

        If this :class:`PythonVersion` instance represents a development
        release, this attribute will be the development release number (an
        integer); otherwise, it will be `None`.

    .. attribute:: is_devrelease

        A boolean value indicating whether this :class:`PythonVersion` instance
        represents a development release.

    .. attribute:: post

        If this :class:`PythonVersion` instance represents a postrelease, this
        attribute will be the postrelease number (an integer); otherwise, it
        will be `None`.

    .. attribute:: is_postrelease

        A boolean value indicating whether this :class:`PythonVersion` instance
        represents a post-release.


.. class:: Version(version)

    An alias for :class:`PythonVersion`.


.. exception:: InvalidVersion

    Raised when attempting to create a :class:`PythonVersion` with a version
    string that does not conform to `PEP 440`_.


.. data:: VERSION_PATTERN

    A string containing the regular expression used to match a valid version.
    The pattern is not anchored at either end, and is intended for embedding
    in larger expressions (for example, matching a version number as part of
    a file name). The regular expression should be compiled with the
    ``re.VERBOSE`` and ``re.IGNORECASE`` flags set.


Loose Versions
^^^^^^^^^^^^^^

.. currentmodule:: verspec.loose

.. class:: LooseVersion(version)

    This class abstracts handling of a version if it is not compatible with the
    scheme defined in `PEP 440`_. It implements a similar interface to that of
    :class:`~.PythonVersion`. In addition to supporting pre-`PEP 440`_ versions,
    this class is useful for handling versions for non-Python projects.

    :param str version: The string representation of a version which will be
                        used as is.

    .. note::

        :class:`LooseVersion` instances can't be compared with
        :class:`~.PythonVersion` instances:

        >>> from verspec.python import PythonVersion
        >>> from verspec.loose import LooseVersion
        >>> v1 = PythonVersion("1.0")
        >>> v2 = LooseVersion("1.0")
        >>> v1 == v2
        False
        >>> v1 >= v2
        Traceback (most recent call last):
          ...
        TypeError: '>' not supported between instances of 'PythonVersion' and 'LooseVersion'

    .. attribute:: public

        A string representing the public version portion of this
        :class:`LooseVersion`. This will always be the entire version string.

    .. attribute:: base_version

        A string representing the base version portion of this
        :class:`LooseVersion` instance. This will always be the entire version
        string.

    .. attribute:: epoch

        This will always be ``0`` since without `PEP 440`_ we do not have the
        concept of version epochs.

    .. attribute:: release

        This will always be ``None`` since without `PEP 440`_ we do not have the
        concept of a release segment or its components. It exists primarily for
        compatibility with :class:`~.PythonVersion`'s interface.

    .. attribute:: local

        This will always be ``None`` since without `PEP 440`_ we do not have the
        concept of a local version. It exists primarily for compatibility with
        :class:`~.PythonVersion`'s interface.

    .. attribute:: pre

        This will always be ``None`` since without `PEP 440`_ we do not have the
        concept of a prerelease. It exists primarily for compatibility with
        :class:`~.PythonVersion`'s interface.

    .. attribute:: is_prerelease

        This will always be ``False`` since without `PEP 440`_ we do not have
        the concept of a prerelease. It exists primarily for compatibility with
        :class:`~.PythonVersion`'s interface.

    .. attribute:: dev

        This will always be ``None`` since without `PEP 440`_ we do not have the
        concept of a development release. It exists primarily for compatibility
        with :class:`~.PythonVersion`'s interface.

    .. attribute:: is_devrelease

        This will always be ``False`` since without `PEP 440`_ we do not have
        the concept of a development release. It exists primarily for
        compatibility with :class:`~.PythonVersion`'s interface.

    .. attribute:: post

        This will always be ``None`` since without `PEP 440`_ we do not have the
        concept of a postrelease. It exists primarily for compatibility with
        :class:`~.PythonVersion`'s interface.

    .. attribute:: is_postrelease

        This will always be ``False`` since without `PEP 440`_ we do not have
        the concept of a postrelease. It exists primarily for compatibility with
        :class:`~.PythonVersion`'s interface.


.. class:: Version(version)

    An alias for :class:`LooseVersion`.


.. _PEP 440: https://www.python.org/dev/peps/pep-0440/
