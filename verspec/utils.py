import re

from .baseversion import UnparsedVersion


def canonicalize_version(_version: str) -> UnparsedVersion:
    """
    This is very similar to PythonVersion.__str__, but has one subtle
    difference with the way it handles the release segment.
    """

    from .python import InvalidVersion, PythonVersion

    try:
        version = PythonVersion(_version)
    except InvalidVersion:
        # Loose versions cannot be normalized
        return _version

    parts = []

    # Epoch
    if version.epoch != 0:
        parts.append("{0}!".format(version.epoch))

    # Release segment
    # NB: This strips trailing '.0's to normalize
    parts.append(re.sub(r"(\.0)+$", "", ".".join(
        str(x) for x in version.release
    )))

    # Pre-release
    if version.pre is not None:
        parts.append("".join(str(x) for x in version.pre))

    # Post-release
    if version.post is not None:
        parts.append(".post{0}".format(version.post))

    # Development release
    if version.dev is not None:
        parts.append(".dev{0}".format(version.dev))

    # Local version segment
    if version.local is not None:
        parts.append("+{0}".format(version.local))

    return "".join(parts)
