import os
import subprocess
import re
from setuptools import setup, find_packages, Command

from verspec import __version__

root_dir = os.path.abspath(os.path.dirname(__file__))


class CoverageCommand(Command):
    description = "run unit tests with code coverage"
    user_options = [
        ("test-suite=", "s",
         "test suite to run (e.g. 'some_file::test_suite')"),
    ]

    def initialize_options(self):
        self.test_suite = None

    def finalize_options(self):
        pass

    def run(self):
        subprocess.check_call(
            ["coverage", "run", "-m", "pytest"] +
            (["-q"] if self.verbose == 0 else []) +
            ([self.test_suite] if self.test_suite else [])
        )


class TestCommand(Command):
    description = "run unit tests"
    user_options = [
        ("test-suite=", "s",
         "test suite to run (e.g. 'some_file::test_suite')"),
    ]

    def initialize_options(self):
        self.test_suite = None

    def finalize_options(self):
        pass

    def run(self):
        subprocess.check_call(
            ["pytest"] +
            (["-q"] if self.verbose == 0 else []) +
            ([self.test_suite] if self.test_suite else [])
        )


class LintCommand(Command):
    description = "run linter"
    user_options = []

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        subprocess.check_call(["flake8", "setup.py", "verspec", "test"])


class TypeCheckCommand(Command):
    description = "run static type checker"
    user_options = []

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        subprocess.check_call(["mypy", "verspec", "test"])


class CheckCommand(Command):
    description = "run static checks"
    user_options = []

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        self.run_command("lint")
        self.run_command("typecheck")


with open(os.path.join(root_dir, "README.md"), "r") as f:
    # Read from the file and strip out the badges.
    long_desc = re.sub(r"(^# verspec)\n\n(.+\n)*", r"\1", f.read())

setup(
    name="verspec",
    version=__version__,

    description="Flexible version handling",
    long_description=long_desc,
    long_description_content_type="text/markdown",
    keywords="version handling",
    url="https://github.com/jimporter/verspec",

    author="Jim Porter",
    author_email="itsjimporter@gmail.com",
    license="BSD 2-Clause or Apache-2.0",

    classifiers=[
        "Development Status :: 3 - Alpha",

        "Intended Audience :: Developers",

        "License :: OSI Approved :: Apache Software License",
        "License :: OSI Approved :: BSD License",

        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
    ],

    packages=find_packages(exclude=["test", "test.*"]),
    extras_require={
        'test': ['coverage', 'flake8 >= 3.7', 'mypy', 'pytest', 'pretend'],
    },

    cmdclass={
        "test": TestCommand,
        "coverage": CoverageCommand,
        "check": CheckCommand,
        "lint": LintCommand,
        "typecheck": TypeCheckCommand,
    },
)
