# inversion

[![PyPi version][pypi-image]][pypi-link]
[![Build status][ci-image]][ci-link]
[![Coverage status][codecov-image]][codecov-link]

**inversion** is a Python library for handling software versions and specifiers,
adapted from the [`packaging`][packaging] package.

## An Example

```python
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
```

## Credits

The real credit for this package goes to the [Python Packaging Authority][pypa].

## License

This project is dual-licensed under the BSD and Apache licenses.

[pypi-image]: https://img.shields.io/pypi/v/inversion.svg
[pypi-link]: https://pypi.python.org/pypi/inversion
[ci-image]: https://github.com/jimporter/inversion/actions/workflows/build.yml/badge.svg
[ci-link]: https://github.com/jimporter/inversion/actions/workflows/build.yml?query=branch%3Amaster
[codecov-image]: https://codecov.io/gh/jimporter/inversion/branch/master/graph/badge.svg
[codecov-link]: https://codecov.io/gh/jimporter/inversion

[packaging]: https://github.com/pypa/packaging
[pypa]: https://www.pypa.io/
