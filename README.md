# verspec

[![Github build status][gh-actions-image]][gh-actions-link]
[![Coverage status][codecov-image]][codecov-link]

**verspec** is a Python library for handling software versions and specifiers,
adapted from the [`packaging`][packaging] package.

## An Example

```python
from verspec import loose, python

v1 = loose.Version('1.0')
s1 = loose.SpecifierSet('~=1.0')
assert v1 in s1

v2 = python.Version('1.0')
s2 = python.SpecifierSet('~=1.0')
assert v2 in s2
```

## Documentation

Forthcoming! (Sorry about that...)

## Credits

The real credit for this package goes to the [Python Packaging Authority][pypa].

## License

This project is dual-licensed under the BSD and Apache licenses.

[gh-actions-image]: https://github.com/jimporter/verspec/workflows/build/badge.svg
[gh-actions-link]: https://github.com/jimporter/verspec/actions?query=branch%3Amaster+workflow%3Abuild
[codecov-image]: https://codecov.io/gh/jimporter/verspec/branch/master/graph/badge.svg
[codecov-link]: https://codecov.io/gh/jimporter/verspec

[packaging]: https://github.com/pypa/packaging
[pypa]: https://www.pypa.io/
