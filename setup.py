from setuptools import setup
from setuptools_rust import RustExtension


setup_requires = [
    "setuptools-rust>=0.10.1", "wheel"
]
install_requires = []

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
    install_requires=install_requires,
    setup_requires=setup_requires,
    include_package_data=True,
    zip_safe=False,
)
