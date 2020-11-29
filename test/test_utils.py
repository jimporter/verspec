import pytest

from verspec.utils import canonicalize_version


@pytest.mark.parametrize(
    ("version", "expected"),
    [
        ("1.4.0", "1.4"),
        ("1.40.0", "1.40"),
        ("1.4.0.0.00.000.0000", "1.4"),
        ("1.0", "1"),
        ("1.0+abc", "1+abc"),
        ("1.0.dev0", "1.dev0"),
        ("1.0.post0", "1.post0"),
        ("1.0a0", "1a0"),
        ("1.0rc0", "1rc0"),
        ("100!0.0", "100!0"),
        ("1.0.1-test7", "1.0.1-test7"),  # LooseVersion is unchanged
    ],
)
def test_canonicalize_version(version, expected):
    assert canonicalize_version(version) == expected
