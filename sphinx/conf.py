"""
Functions and routines associated with rawberth Oh-nope IRC Services.

This file is part of Enasis Network software eco-system. Distribution
is permitted, for more information consult the project license file.
"""
# pylint: disable=import-error



from os import path as os_path
from sys import path as sys_path

sys_path.insert(0, os_path.abspath('../'))

from ohnope import VERSION  # noqa: E402



project = 'ohnope'
copyright = '2024, rawberth'
author = 'rawberth'
nitpicky = True
version = VERSION

# autodoc and viewcode disabled
# because is private repository
extensions = [
    'sphinx.ext.doctest',
    'sphinx.ext.intersphinx',
    'sphinxcontrib.autodoc_pydantic']

html_theme = 'pydata_sphinx_theme'

always_document_param_types = True

intersphinx_mapping = {
    'encommon': ('https://enasisnetwork.github.io/encommon/sphinx', None),
    'enconnect': ('https://enasisnetwork.github.io/enconnect/sphinx', None),
    'enrobie': ('https://enasisnetwork.github.io/enrobie/sphinx', None),
    'jinja2': ('https://jinja.palletsprojects.com/en/latest', None),
    'netaddr': ('https://netaddr.readthedocs.io/en/latest', None),
    'pydantic': ('https://docs.pydantic.dev/latest', None),
    'pytest': ('https://docs.pytest.org/latest', None),
    'python': ('https://docs.python.org/3', None),
    'sqlalchemy': ('https://docs.sqlalchemy.org/en/20', None)}
