# pypi-solv

Placeholder package to make the libsolv Python bindings available through PyPI.

The libsolv build process generates Python bindings with SWIG, and then installs
the built extension module directly to its final destination, without
generating a pip-installable Python wheel file for use in virtual environments.

Right now, this package just reserves the `solv` name on PyPI to avoid the
potential for a name conflict with the ubiquitous `python2-solv` and
`python3-solv` packages on RPM-based Linux distros.

However, I eventually hope to replace it with a CMake-dependent PEP 517 backend
that runs the full libsolv build process, and then emits a statically linked
completely self-contained extension module in a wheel file.
