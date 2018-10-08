import os
import sys
import subprocess
from setuptools import setup
from setuptools_rust import RustExtension
from setuptools.command.test import test as TestCommand


class PyTest(TestCommand):

    def run(self):
        self.run_command("test_rust")

        subprocess.check_call(["pytest", "tests"])


_root = os.path.abspath(os.path.dirname(__file__))

with open(os.path.join(_root, 'requirements.txt')) as f:
    install_requires = f.readlines()

with open(os.path.join(_root, 'README.md')) as f:
    readme = f.read()

with open(os.path.join(_root, 'test-requirements.txt')) as f:
    tests_require = install_requires + f.readlines()

setup_requires = [
    "setuptools-rust>=0.10.1", "wheel"
]

setup(
    name="ticket",
    version="0.1.0",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
        "Programming Language :: Rust",
        "Operating System :: POSIX",
    ],
    packages=["ticket"],
    rust_extensions=[
        RustExtension("ticket.ticket", "Cargo.toml")
    ],
    setup_requires=setup_requires,
    install_requires=install_requires,
    tests_require=tests_require,
    include_package_data=True,
    zip_safe=False,
    cmdclass=dict(test=PyTest),
)
