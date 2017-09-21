"""Placeholder pending proper publication of libsolv bindings"""
__version__ = "0.0.1"

import warnings

warning_msg = """\
The libsolv Python bindings are not currently available via PyPI.

Please install them with your distro package manager (typically called
'python3-solv' or 'python2-solv'), and ensure that any virtual
environments needing them are configured to be able to see the system
site packages directory.
"""

warnings.warn(warning_msg)